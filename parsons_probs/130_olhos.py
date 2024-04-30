def setup(): #0given
    size(400, 400) #1given
    olho(100, 150, 100) #1given
    olho(250, 250, 200) #1given
# definição do olho  #0given
def olho(x, y, tamanho): #0given
    no_stroke() # sem contorno
    fill(255)   # branco
    ellipse(x, y, tamanho, tamanho * 0.40) # branco do olho
    fill(200, 200, 0) # amarelo
    circle(x, y, tamanho * 0.40) # iris
    fill(0) # preto (0) 
    circle(x, y, tamanho * 0.10) # pupila
    
# END PUZZLE
file = Path(__file__).stem
name = 'Função olho'
subt = 'Definindo uma função de desenho e a chamando.'
dcat = 'funções'
desc = (
f"""<h6>{name}</h6>"""
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code> """
f"""Organize o bloco de definição da função olho para que ela """
f"""possa ser chamada no setup() e os olhos desenhados.</br>"""
    )

def format_source():
    with open(__file__) as f:
        code_lines = ''
        for lin in f.readlines():
            if lin.startswith('# END'):
                break
            fline = '  ' + lin.strip(' ') # preserves \n
            if fline.strip():  # skip empty lines
                code_lines += fline
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
    
    
    
