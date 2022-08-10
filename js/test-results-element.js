import {LitElement, html} from 'lit';

export class TestResultsElement extends LitElement {
	static properties = {
		status: {type: String},
		header: {type: String},
		details: {type: String},
	};

	createRenderRoot() {
		return this;
	}

	render() {
		return html`<div class="testcase ${this.status}">
						<span class="msg">${this.header}</span>
						</div>
						<pre><code>${this.details}</code></pre></div>
					</div>`;
	}
}

customElements.define('test-results-element', TestResultsElement);
