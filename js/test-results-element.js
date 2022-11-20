import {LitElement, html} from 'lit';

export class TestResultsElement extends LitElement {
	createRenderRoot() {
		return this;
	}

	render() {
		return html`
			<div id="sketch-holder">
				<!-- You sketch will go here! -->
			</div>
		`;
	}
}

customElements.define('test-results-element', TestResultsElement);
