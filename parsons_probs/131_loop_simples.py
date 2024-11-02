tamanhos = [10, 20, 40, 50, 100, 110, 220, 230] # 0given

def setup(): #0given
    size(400, 400) #1given
    no_fill() # sem preenchimento
    for t in tamanhos:
        circle(200, 200, t)

# END PUZZLE
file = Path(__file__).stem
name = 'Círculos concentricos'
subt = 'Iterando por uma lista de tamanhos.'
dcat = '130 - laços de repetição'
desc = (
f"""<h6>{name}</h6>"""
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code> """
f"""Organize os blocos para desenhar os círculos corretamente.</br>"""
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
    
    