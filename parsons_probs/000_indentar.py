
def setup(): #0given
    size(400, 400) # sempre primeiro
    background(0, 100, 00)
    rect(100, 100, 50, 50)
    
# END OF PUZZLE - GENERATING METADATA
file = Path(__file__).stem
name = 'indentação e um retângulo'
subt = 'usando a função size() dentro do setup()'
dcat = '100 - primeiros passos'
desc = (
f"""<h6>{name}</h6></br>"""
f"""<img src="parsons_probs/{file}.gif"></br>"""
f"""<code>{subt}</code></br>"""
f"""Organize os blocos de tal forma que size() fique indentada"""
f"""e esteja bem no começo da função setup()."""
f"""background() que faz o fundo deve vir antes da chamada a rect(),"""
f"""ambas estão "dentro" de setup(), e por isso indentadas."""
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
    