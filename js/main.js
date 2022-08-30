import yaml from 'js-yaml';

import {get, set} from './user-storage.js';
import {
	prepareCode,
	processTestResults,
	processTestError,
} from './doctest-grader.js';
import './problem-element.js';
import {FiniteWorker} from './worker-manager.js';

const LS_REPR = '-repr';
let probEl;

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
		probEl.setAttribute('runStatus', 'Loading Pyodide...');
		probEl.addEventListener('run', (e) => {
			handleSubmit(e.detail.code, e.detail.repr, func);
		});
		probEl.setAttribute('enableRun', 'enableRun');
		probEl.setAttribute('runStatus', '');
		document.getElementById('problem-wrapper').appendChild(probEl);
	});
}

async function handleSubmit(submittedCode, reprCode, codeHeader) {
	let testResults = prepareCode(submittedCode, codeHeader);

	if (testResults.code) {
		try {
			const code = testResults.code + '\nsys.stdout.getvalue()';
			const {results, error} = await new FiniteWorker(code);
			if (results) {
				testResults = processTestResults(results);
			} else {
				testResults = processTestError(error, testResults.startLine);
			}
		} catch (e) {
			console.warn(
				`Error in pyodideWorker at ${e.filename}, Line: ${e.lineno}, ${e.message}`
			);
		}
	}

	probEl.setAttribute('runStatus', '');
	probEl.setAttribute('resultsStatus', testResults.status);
	probEl.setAttribute('resultsHeader', testResults.header);
	probEl.setAttribute('resultsDetails', testResults.details);

	set(probEl.getAttribute('name') + LS_REPR, reprCode);
}
