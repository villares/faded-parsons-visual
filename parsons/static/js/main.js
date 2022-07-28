
// Credit to https://stackoverflow.com/questions/1248849/converting-sanitised-html-back-to-displayable-html
function replaceEntities(str) {
    var ret = str.replace(/&gt;/g, '>');
    ret = ret.replace(/&lt;/g, '<');
    ret = ret.replace(/&quot;/g, '"');
    ret = ret.replace(/&apos;/g, "'");
    ret = ret.replace(/&amp;/g, '&');
    return ret;
};

function decodeHtmlEntity(x) {
    return x.replace(/&#(\d+);/g, function(match, dec) {
        return String.fromCharCode(dec);
    });
}

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

function cleanupDoctestResults(lines) {
    let keptLines = [];
    let inKeepRange = false;
    lines.forEach((line) => {
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

function getSolutionCode() {
    // Removes line numbers so they don't pollute solutionCode
    $(".line-number").remove();

    var [solutionCode, codeMetadata] = parsonsWidget.solutionCode();
    solutionCode = decodeHtmlEntity(replaceEntities(solutionCode));
    codeMetadata = decodeHtmlEntity(replaceEntities(codeMetadata));

    setLineNumbers();

    return JSON.stringify({
        'code': solutionCode,
        'code_metadata': codeMetadata,
    })
}

function setLineNumbers() {
    // Removes all line numbers
    $(".line-number").remove();
    var lines = $("#ul-parsons-solution").children('li');
    lines.each(function() {
        var line = $(this);
        var lineNumber = line.index() + 1;
        line.append('<code class="line-number"> ' + lineNumber + '</code>')
    })
}

var LS_CODE = '-code';
var LS_REPR = '-repr';
var parsonsWidget;
var pyodide;
let outputLines = [];

async function initPyodide() {
    pyodide = await loadPyodide({
        indexURL : "https://cdn.jsdelivr.net/pyodide/v0.19.0/full/",
        stdout: handlePyodideResults,
    });
    document.getElementById("submit").removeAttribute("disabled");
};

function initWidget() {
    const fetchConf = fetch(`../../parsons_probs/${PROBLEM_NAME}.yaml`).then((res) => res.text());
    const fetchFunc = fetch(`../../parsons_probs/${PROBLEM_NAME}.py`).then((res) => res.text());
    const allData = Promise.all([fetchConf, fetchFunc]);

    allData.then((res) => {
        const [config, func] = res;
        console.log(config);
        const configYaml = jsyaml.load(config);
        const probDescription = configYaml['problem_description'];
        let codeLines = configYaml['code_lines'] +
            '\nprint(\'DEBUG:\', !BLANK)' + '\nprint(\'DEBUG:\', !BLANK)' +
            '\n# !BLANK' + '\n# !BLANK';
        const localRepr = get(PROBLEM_NAME + LS_REPR);
        if (localRepr) {
            codeLines = localRepr;
        }
        PYTHON_FUNC = func;

        parsonsWidget = new ParsonsWidget({
            'sortableId': 'parsons-solution',
            'onSortableUpdate': (event, ui) => {
                setLineNumbers();
            },
            'trashId': 'starter-code',
            'max_wrong_lines': 1,
            'syntax_language': 'lang-py',
        });
        parsonsWidget.init(codeLines);
        parsonsWidget.alphabetize();
        document.getElementById("submit").addEventListener("click", submitParsons);
        document.getElementById("problem-description").innerHTML = probDescription;
    });
}


function submitParsons() {
    $("#test_description").hide();
    $("#errors").show();
    $("#errors_body").html('<div id="loader"></div>');

    var submittedCode = JSON.parse(getSolutionCode())['code'] + '\n'
    let lines = PYTHON_FUNC.split('\n');
    const startLine = countDocstringLines(lines);
    const codeLines = submittedCode.split("\n");
    if (!(codeLines[0].includes("def") || codeLines[0].includes("class"))) {
        alert("First code line must be `def` or `class` declaration");
        return;
    }
    // Remove function def or class declaration statement, is relied on elsewhere
    codeLines.shift();

    let line = findNextUnindentedLine(codeLines, 0);
    if (line != codeLines.length) {
        alert("All lines in a function or class definition should be indented at least once. It looks like you have a line that has no indentation.");
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
    finalCode.push('');
    finalCode.push('import doctest');
    finalCode.push('doctest.testmod(verbose=True)');
    finalCode = finalCode.join('\n');

    outputLines = [];
    try {
        pyodide.runPython(finalCode);
    } catch(error) {
        // Handle syntax errors
        if (error.message.startsWith('Traceback')) {
            const errorMsg = extractError(error.message, startLine);
            let testResults = '<div class="testcase fail"><span class="msg">Syntax error</span></div>';
            testResults += '<span style="white-space: pre-line"><pre><code>' + errorMsg +  '  <pre></code></span></div>';
            $("#errors").show();
            $("#errors_body").html(testResults);
        }
    }
    set(PROBLEM_NAME + LS_CODE, submittedCode);
    set(PROBLEM_NAME + LS_REPR, parsonsWidget.parsonsReprCode());
}


function handlePyodideResults(outputLine) {
    let testResults;
    outputLines.push(outputLine);
    if (outputLine == 'Test passed.') {
        testResults = '<div class="testcase pass"><span class="msg">All tests passed</span></div>';
    } else {
        const summaryRe = /(\d+)\spassed\sand\s(\d+)\sfailed./;
        const summaryMatches = outputLine.match(summaryRe);
        if (summaryMatches) {
            const successCount = parseInt(summaryMatches[1], 10);
            const failCount = parseInt(summaryMatches[2], 10);
            const totalCount = successCount + failCount;
            const doctestResults = cleanupDoctestResults(outputLines);
            testResults = `<div class="testcase fail"> Passing ${successCount} of ${totalCount} total cases</div>`;
            testResults += '<span style="white-space: pre-line"><pre><code>' + doctestResults + '<pre></code></span></div>';
        }
    }
    $("#errors").show();
    $("#errors_body").html(testResults);
}

