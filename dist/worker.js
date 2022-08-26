/* global loadPyodide, importScripts */

importScripts("https://cdn.jsdelivr.net/pyodide/v0.21.1/full/pyodide.js");

async function loadPyodideAndRemember() {
  self.pyodide = await loadPyodide();
}
let pyodideReadyPromise = loadPyodideAndRemember();

self.onmessage = async (event) => {
  await pyodideReadyPromise;
  const { id, python } = event.data;
  try {
    let results = await self.pyodide.runPythonAsync(python);
    self.postMessage({ results, id });
  } catch (error) {
    self.postMessage({ error: error, id });
  }
};