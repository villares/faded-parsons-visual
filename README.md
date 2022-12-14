# Python Faded Parsons Problems with Visual Output 
## (Work in Progress!)

This website should allow you to run Faded Parsons Problems in the browser.
It will use Pyodide to show *pyp5js* sketch results.

Based on https://github.com/pamelafox/faded-parsons-static/

Check out at https://abav.lugaralgum.com/faded-parsons-visual/

## Running the website

From the download directory:

`python -m http.server 8000`  because I can't even type `npm`

## Deploying the website

This website can be deployed anywhere since it's entirely static, and is currently deployed on Github Pages. You can enable Pages on your own fork of the repo to host on Github.

## Adding a new problem

Add files to the `parson_probs` folder:

* ~~problem_name.py: This should be a Python function that _only_ has the function header, docstring, and doctests. It shouldn't contain the solution.~~
* `problem_file.yaml`: This is a YAML file that includes the problem description (HTML) and code lines with blanks.
    - You can add an image to the description, I have to figure where to keep the images.
		- Example:
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
