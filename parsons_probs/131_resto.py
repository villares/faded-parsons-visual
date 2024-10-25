def setup(): #0given
    size(400, 400) #1given
    background(120, 120, 240) #1given
    stroke_weight(2) #1given
    for i in range(2, 18):
        if i % 2 == 0:
            stroke(255) # white
        else:
            stroke(0) # black
        y = 10 + i * 20
        line(50, y, width - 50, y)
        


  


# END PUZZLE
file = Path(__file__).stem
ext = '.png'
name = 'Pares e ímpares'
subt = 'Usando o resto da divisão para alternar cores.'
dcat = '130 - laços de repetição'
dins = (
"Organize os blocos para desenhar as linhas corretamente. "
"Note como a primeira linha é branca."
)  
desc = (
f"""<h6>{name}</h6>"""
f"""<img src="parsons_probs/{file}{ext}"></br>"""
f"""<code>{subt}</code> """
f"""{dins}.</br>"""
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
    
    
    
    

