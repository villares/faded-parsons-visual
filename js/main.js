/* global loadPyodide */
import yaml from 'js-yaml'

import { get, set } from "./user-storage.js";
import './problem-element.js';

function findNextUnindentedLine(lines, start) {
    /*
    Finds the next piece of unindented code in the file. Ignores empty lines and lines
    that start with a space or tab. Returns len(lines) if no unindented line found.
    */
    let lineNum = start;
    while (lineNum < lines.length) {
        const line = lines[lineNum];
        if (!(line == '' || line[0] == ' ' || line[0] == '\t' || line[0] == '\n')) {
            break;
        }
        lineNum++;
    }
    return lineNum;
}


function countDocstringLines(lines) {
    let startLine = -1;
    let inDocstring = false;
    lines.forEach((line, i) => {
        if (line.trim().includes('"""')) {
            if (inDocstring) {
                startLine = i + 1;
                return;
            }
            inDocstring = true;
        }
    });
    return startLine;
}

function extractError(error, numDocstringLines) {
    let startI = -1;
    let endI = -1;
    let lineNum;
    const errorLines = error.split('\n');
    for (var i = errorLines.length - 1; i >= 0; i--) {
        let line = errorLines[i];
        if (line.startsWith("SyntaxError") || line.startsWith("IndentationError")) {
            endI = i;
        } else if (line.includes('File "<exec>", line')) {
            lineNum = parseInt(line.split(', line ')[1], 10);
            lineNum -= (numDocstringLines - 1);
            startI = i;
            break;
        }
    }
    if (startI == -1 || endI == -1) {
        return 'No error report found.';
    } else {
        return `Error at line ${lineNum}:\n` + errorLines.slice(startI + 1, endI + 1).join('\n');
    }
}

function cleanupDoctestResults(resultsStr) {

    let keptLines = [];
    let inKeepRange = false;
    resultsStr.split('\n').forEach((line) => {
        if (line.startsWith('File "__main__"')) {
            inKeepRange = true;
            return;
        } else if (line.startsWith("Trying:") || line.startsWith('1 items had no tests:')) {
            inKeepRange = false;
        }
        if (inKeepRange) {
            line = line.replace('Failed example:', '\n❌ Failed example:');
            keptLines.push(line);
        }
    });
    return keptLines.join("\n");
}


var LS_REPR = '-repr';
let probEl;
var pyodide;

export async function initPyodide() {
    pyodide = await loadPyodide({
        indexURL : "https://cdn.jsdelivr.net/pyodide/v0.19.0/full/"
    });
    probEl.setAttribute("enableRun", "enableRun");
}

export function initWidget() {
    let params = (new URL(document.location)).searchParams;
    let problemName = params.get("name");

    const fetchConf = fetch(`parsons_probs/${problemName}.yaml`).then((res) => res.text());
    const fetchFunc = fetch(`parsons_probs/${problemName}.py`).then((res) => res.text());
    const allData = Promise.all([fetchConf, fetchFunc]);

    allData.then((res) => {
        const [config, func] = res;
        const configYaml = yaml.load(config);
        const probDescription = configYaml['problem_description'];
        let codeLines = configYaml['code_lines'] +
            '\nprint(\'DEBUG:\', !BLANK)' + '\nprint(\'DEBUG:\', !BLANK)' +
            '\n# !BLANK' + '\n# !BLANK';
        const localRepr = get(problemName + LS_REPR);
        if (localRepr) {
            codeLines = localRepr;
        }
        probEl = document.createElement('problem-element');
        probEl.setAttribute('name', problemName);
        probEl.setAttribute('description', probDescription);
        probEl.setAttribute('codeLines', codeLines);
        probEl.setAttribute('codeHeader', func);
        probEl.addEventListener('run', (e) => {
            handleSubmit(e.detail.code, e.detail.repr, func);
        });
        document.getElementById('problem-wrapper').appendChild(probEl);
    });
}


function handleSubmit(submittedCode, reprCode, codeHeader) {
    submittedCode += "\n";
    let lines = codeHeader.split('\n');
    const startLine = countDocstringLines(lines);
    const codeLines = submittedCode.split("\n");
    if (!(codeLines[0].includes("def") || codeLines[0].includes("class"))) {
        probEl.setAttribute("results", "First code line must be `def` or `class` declaration");
        return;
    }
    // Remove function def or class declaration statement, is relied on elsewhere
    codeLines.shift();

    let line = findNextUnindentedLine(codeLines, 0);
    if (line != codeLines.length) {
        probEl.setAttribute("results", "All lines in a function or class definition should be indented at least once. It looks like you have a line that has no indentation.");
        return;
    }
    const linesToPreserve = lines.slice(0, startLine);
    const endOfReplaceLines = findNextUnindentedLine(lines, startLine);
    const extraLinesToPreserve = lines.slice(endOfReplaceLines);
    let finalCode = [];
    linesToPreserve.forEach((line) => {
        finalCode.push(line);
    });
    codeLines.forEach((line) => {
        finalCode.push(line);
    });
    extraLinesToPreserve.forEach((line) => {
        finalCode.push(line);
    });
    // Redirects stdout so we can return it
    finalCode.push('import sys');
    finalCode.push('import io');
    finalCode.push('sys.stdout = io.StringIO()');
    // Runs the doctests
    finalCode.push('import doctest');
    finalCode.push('doctest.testmod(verbose=True)');
    finalCode = finalCode.join('\n');

    try {
        pyodide.runPython(finalCode);
        handlePyodideOutput(pyodide.runPython('sys.stdout.getvalue()'));
    } catch(error) {
        // Handle syntax errors
        if (error.message.startsWith('Traceback')) {
            const errorMsg = extractError(error.message, startLine);
            let testResults = '<div class="testcase fail"><span class="msg">Syntax error</span></div>';
            testResults += '<span style="white-space: pre-line"><pre><code>' + errorMsg +  '  <pre></code></span></div>';
            probEl.setAttribute("results", testResults);

        }
    }
    set(probEl.getAttribute('name') + LS_REPR, reprCode);
}


function handlePyodideOutput(outputStr) {
    let testResults;

    if (outputStr.endsWith('Test passed.')) {
        probEl.setAttribute("results", "All lines in a function or class definition should be indented at least once. It looks like you have a line that has no indentation.");
    } else {
        const summaryRe = /(\d+)\spassed\sand\s(\d+)\sfailed./;
        const summaryMatches = outputStr.match(summaryRe);
        if (summaryMatches) {
            const successCount = parseInt(summaryMatches[1], 10);
            const failCount = parseInt(summaryMatches[2], 10);
            const totalCount = successCount + failCount;
            const doctestResults = cleanupDoctestResults(outputStr);
            testResults = `<div class="testcase fail"> Passing ${successCount} of ${totalCount} total cases</div>`;
            testResults += '<span style="white-space: pre-line"><pre><code>' + doctestResults + '<pre></code></span></div>';
            probEl.setAttribute("results", testResults);
        }
    }
}

