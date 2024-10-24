from itertools import product #0given
n = 8
def setup(): #0given
    size(400, 400) #1given
    background(0) # fundo preto
    text_align(CENTER, CENTER)
    d = width / n
    k = 0
    for i, j in product(range(n), repeat=2):
        x, y = j * d + d / 2,  i * d + d / 2
        fill(255) # branco
        circle(x, y, d)
        fill(0, 0, 200) # azul
        text(str(k), x, y)
        k = k + 1
# END OF PUZZLE - GENERATING META DATA
file = Path(__file__).stem
name = 'Grade numerada'
subt = 'Usando itertools.product e text() para os números'
dcat = '130 - laços de repetição'
desc = (
f"""<h6>{name}</h6></br>"""
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code></br>"""
f"""Organize os blocos para o obter um desenho como este."""
    )

def format_source():
    with open(__file__) as f:
        code_lines = ''
        for lin in f.readlines():
            if lin.startswith('# END'):
                break
            elif '!REMOVE' in lin:
                continue
            elif '!BLANK' in lin:
                lin.lstrip('#')  # to add comments with !BLANK to puzzle
            lin = lin.strip(' ') # this preserves \n
            if lin.strip(): # skip empty lines as .strip() removes \n
                code_lines += '  ' + lin
    return code_lines

def exiting():
    save(file + '.png')  # save image result
    print(file)
    code_lines = format_source()
    yaml = f"""\
problem_name: {name} 

problem_subtitle: {subt}

problem_category: {dcat}

problem_description: |
  {desc}
   
code_lines: |
{code_lines}
  
test_fn: setup
"""
    with open(file + '.yaml', 'w') as f:
        f.write(yaml)
