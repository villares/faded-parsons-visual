fill_colors = ['red', 'green', 'blue', 'pink'] #0given

def setup(): #0given
    size(400, 400) #1given
    x = 50 #1given
    for fc in fill_colors:
        fill(fc)
        circle(x, 200, 100)
        x = x + 100

# END PUZZLE
file = Path(__file__).stem
name = 'Círculos coloridos'
subt = 'Iterando por uma lista de nomes de cores.'
dcat = '130 - laços de repetição'
desc = (
f"""<h6>{name}</h6>"""
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code> """
f"""Organize os blocos para desenhar os círculos coloridos.</br>"""
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
    
    
