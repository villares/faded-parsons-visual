/* global loadPyodide */
import yaml from 'js-yaml';

import {get, set} from './user-storage.js';
import {
	prepareCode,
	processTestResults,
	processTestError,
} from './doctest-grader.js';
import './problem-element.js';

const LS_REPR = '-repr';
let probEl;
let pyodide;

export async function initPyodide() {
	pyodide = await loadPyodide({
		indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.19.0/full/',
	});
	probEl.setAttribute('enableRun', 'enableRun');
}

export function initWidget() {
	let params = new URL(document.location).searchParams;
	let problemName = params.get('name');

	const fetchConf = fetch(`parsons_probs/${problemName}.yaml`).then((res) =>
		res.text()
	);
	const fetchFunc = fetch(`parsons_probs/${problemName}.py`).then((res) =>
		res.text()
	);
	const allData = Promise.all([fetchConf, fetchFunc]);

	allData.then((res) => {
		const [config, func] = res;
		const configYaml = yaml.load(config);
		const probDescription = configYaml['problem_description'];
		let codeLines =
			configYaml['code_lines'] +
			"\nprint('DEBUG:', !BLANK)" +
			"\nprint('DEBUG:', !BLANK)" +
			'\n# !BLANK' +
			'\n# !BLANK';
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
	let testResults = prepareCode(submittedCode, codeHeader);

	if (testResults.code) {
		try {
			pyodide.runPython(testResults.code);
			testResults = processTestResults(
				pyodide.runPython('sys.stdout.getvalue()')
			);
		} catch (error) {
			testResults = processTestError(error, testResults.startLine);
		}
	}
	console.log(testResults);
	probEl.setAttribute('resultsStatus', testResults.status);
	probEl.setAttribute('resultsHeader', testResults.header);
	probEl.setAttribute('resultsDetails', testResults.details);

	set(probEl.getAttribute('name') + LS_REPR, reprCode);
}
