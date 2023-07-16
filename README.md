# Python Faded Parsons Problems with Visual Output

## (Work in Progress!)

This website should allow you to run Faded Parsons Problems in the browser.
It will use Pyodide to show _pyp5js_ sketch results.

Based on https://github.com/pamelafox/faded-parsons-static/

Check out at https://abav.lugaralgum.com/faded-parsons-visual/

## Setting up the website

Be sure to have `nodejs` installed. To install `nodejs`, go to their download page and download the installer for your operating system: https://nodejs.org/en/download/

We will assume you have at least some familiarity with the command line. After installing, open a terminal, go to the project's folder using `cd` (the one you're in right now) and run:

`npm install`

This will install all the dependencies for the website.

If you don't have `npm` installed, double check the installation instructions for `nodejs` for your operating system.

## Running the website

From the download directory:

`npm run dev`

This will start a local server at http://localhost:8000/ where you can see the website. Also, whenever you change something in the code, reload the page to see the changes.

## Building the website

To make the site ready for deployment, run:

`npm run build`

This will recreate the `dist` folder with the website ready to be deployed.

## Deploying the website

This website can be deployed anywhere since it's entirely static, and is currently deployed on Github Pages. You can enable Pages on your own fork of the repo to host on Github.

## Adding a new problem

Add files to the `parson_probs` folder:

- `problem_file.yaml`: This is a YAML file that includes the problem description (HTML) and code lines with blanks.

- You should add an image to the description, like `problem_file.png`, in the same folder.

- Example `000_variables.yaml` that uses `000_variables.png` in the same folder:

```yaml

problem_name: Variables

problem_subtitle: assignement

problem_category: Getting Started

problem_description: |
	<code>Variáveis </code>
		Organize as linhas para formar o desenho abaixo
		</br>
		<img src="parsons_probs/000_variables.png">
		</br>


code_lines: |
	 def setup(): #0given
	 size(400, 400) #1given
	 background(200) # fundo cinza
	 nome = '!BLANK'
	 text(nome, 20, 180)  # desenha o texto de `nome`
	 # Se tentar usar a variável `a` antes de criar...
	 # ... vai ter um erro do tipo NameError (não conheço `a`)
	 a = 10  # cria a variável `a` que aponta para o valor 10
	 square(a, 10, 140)  # desenha um quadrado de lado 140 em x:10, y:10
	 a = a + 145  # calcula o valor de `a + 145` e muda a variável `a`
	 square(a, 10, !BLANK)  # desenha um quadrado de lado 140

```

Then you can access the new problem at **`.../problem.html?name=problem_file`**

There is a [Python script](https://github.com/villares/faded-parsons-visual/blob/hack/update_index.py) that will look for YAML problems, check the category and update the `index.html` with links to all the problems found in `parsons_probs`.
