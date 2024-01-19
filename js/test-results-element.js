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
		return html`
			<div id="sketch-holder" class="${this.status !== 'pass' ? this.status : ''}">
				${this.header.length
					? html`<div class="testcase ${this.status !== 'pass' ? this.status : ''}">
							<span class="msg">${this.header}</span>
					  </div>`
					: ''}
				${this.details.length
					? html`<div class="testcase">
							<pre><code>${this.details}</code></pre>
					  </div>`
					: ''}
			</div>
		`;
	}
}

customElements.define('test-results-element', TestResultsElement);
