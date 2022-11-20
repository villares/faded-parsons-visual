# Python Faded Parsons Problems with Visual Output (Work in Progress!)

This website allows you to run Faded Parsons Problems in the browser.
It uses Pyodide for executing Python doctests and localStorage for storing user progress.

Based on https://github.com/pamelafox/faded-parsons-static/

Check out at ttps://abav.lugaralgum.com/faded-parsons-visual/

## Running the website

From the download directory:

`python -m http.server 8000`

## Deploying the website

This website can be deployed anywhere since it's entirely static, and is currently deployed on Github Pages. You can enable Pages on your own fork of the repo to host on Github.

## Adding a new problem

Add two files to the `parson_probs` folder:

* problem_name.py: This should be a Python function that _only_ has the function header, docstring, and doctests. It shouldn't contain the solution.
* problem_name.yaml: This is a YAML file that includes the problem description (HTML) and code lines with blanks.

Then you can access the new problem at problem.html?name=problem_name
