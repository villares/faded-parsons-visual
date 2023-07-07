/* global ParsonsWidget */

import {LitElement, html, css} from 'lit';
import {unsafeHTML} from 'lit/directives/unsafe-html.js';
import {ref, createRef} from 'lit/directives/ref.js';

import './loader-element.js';
import './test-results-element.js';
import {set} from './user-storage.js';
import {LS_REPR} from './main.js';

export class ProblemElement extends LitElement {
	static properties = {
		name: {type: String},
		description: {type: String},
		codeLines: {type: String},
		codeHeader: {type: String},
		isLoading: {type: Boolean},
		enableRun: {type: Boolean, state: true},
		runStatus: {type: String},
		resultsStatus: {type: String},
		resultsHeader: {type: String},
		resultsDetails: {type: String},
	};

	static styles = css`
		.starter {
			width: 40%;
		}
		.solution {
			width: 58%;
			margin-left: 2%;
		}
	`;

	starterRef = createRef();
	solutionRef = createRef();

	constructor() {
		super();
		this.enableRun = false;

		window.addEventListener('pyodideReady', () => {
			this.enableRun = true;
		});
	}

	createRenderRoot() {
		return this;
	}

	clearStorage() {
		set(this.name + LS_REPR, '');
		window.location.reload();
	}

	render() {
		return html`
			<div class="row mt-3">
				<div class="col-sm-12">
					<div class="card">
						<div class="card-header">
							<h3>Problem Statement</h3>
						</div>
						<div class="card-body">${unsafeHTML(this.description)}</div>
					</div>
				</div>
			</div>

			<div class="row mt-4">
				<div class="col-sm-12">
					<div class="card">
						<div class="card-body">
							<div ${ref(this.starterRef)} class="sortable-code starter"></div>
							<div ${ref(this.solutionRef)} class="sortable-code solution"></div>
							<div style="clear:both"></div>
							<div class="row float-right">
								<div class="col-sm-12">
									<span style="margin-right: 8px">
										${this.runStatus && html` <loader-element></loader-element>`}
										${this.runStatus}
									</span>
									<button
										@click=${this.clearStorage}
										type="button"
										class="btn btn-outline-danger"
									>
										Reset code
									</button>
									<button
										@click=${this.onRun}
										type="button"
										class="btn btn-primary"
										?disabled=${!this.enableRun}
									>
										${this.enableRun ? 'Run code' : 'Loading...'}
									</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="row mt-4">
				<div class="col-sm-12">
					<div class="card">
						<div class="card-header">
							<h4>Result</h4>
						</div>
						<div id="test_description">
							<div class="card-body">
								${!this.resultsStatus
									? 'The resulting image will be rendered here when you click "Run code".'
									: ''}
								${html`
									<test-results-element
										status=${this.resultsStatus}
										header=${this.resultsHeader}
										details=${this.resultsDetails}
									/>
								`}
							</div>
						</div>
					</div>
				</div>
			</div>
		`;
	}

	firstUpdated() {
		this.parsonsWidget = new ParsonsWidget({
			sortableId: this.solutionRef.value,
			trashId: this.starterRef.value,
		});
		this.parsonsWidget.init(this.codeLines);
		this.parsonsWidget.alphabetize();
	}

	onRun() {
		this.runStatus = 'Running code...';
		this.dispatchEvent(
			new CustomEvent('run', {
				detail: {
					code: this.parsonsWidget.solutionCode(),
					repr: this.parsonsWidget.reprCode(),
				},
			})
		);
	}
}

customElements.define('problem-element', ProblemElement);
