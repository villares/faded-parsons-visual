def setup(): #0given
    size(400, 400) #1given
    background(0, 200, 0) # verde 
    rect_mode(CENTER)
    circle(200, 50, 50) #1given
    fill(0)  # preto
    ellipse(200, 150, 100, 50)
    fill(0, 0, 200)  # azul
    no_stroke() # desliga traço
    square(200, 250, 50)
    stroke(255, 255, 0) # amarelo
    fill(255, 0, 0)  # vermelho
    rect(200, 350, 100, 50)
    
# END OF PUZZLE - GENERATING METADATA
file = Path(__file__).stem
name = 'Desenho, formas e cores'
subt = 'Formas básicas, cores de preenchimento e traço'
dcat = '100 Primeiros passos'
desc = (
f"""<h6>{name}</h6></br>"""
f"""<img src="parsons_probs/{file}.gif"></br>"""
f"""<code>{subt}</code></br>"""
f"""Organize os blocos para desenhar as figuras."""
f"""Preste atenção nas cores dos elementos e das linhas de contorno."""
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
    #save(file + '.png')  # save image result
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
    
