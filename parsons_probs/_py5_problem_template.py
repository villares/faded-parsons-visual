
# setup: configurações iniciais #0given
def setup(): #0given
    size(400, 400) #1given
    square(200, 250, 50) #1given
    
# END OF PUZZLE - GENERATING METADATA
file = Path(__file__).stem
name = 'Exemplo estático'
subt = 'Quadradinho'
dcat = '100 - primeiros passos'
desc = (
f"""<h6>{name}</h6></br>"""
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code></br>"""
f"""Organize os blocos para fazer um sketch como este."""
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
