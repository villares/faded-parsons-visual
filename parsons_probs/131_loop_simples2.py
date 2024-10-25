fill_colors = ['red', 'green', 'blue', 'pink'] # 0given

def setup(): #0given
    size(400, 400) #1given
    x = 50 #1given
    for fc in fill_colors:
        fill(fc)
        circle(x, 200, 100)
        x = x + 100

### fim do código do quebra-cabeças - gerando metadados
def exiting():
    file = Path(__file__).stem
    save(file + '.png')
    print(file)
    nome = 'Círculos coloridos'
    subt = 'Iterando por uma lista de nomes de cores.'
    categoria = '130 - laços de repetição'
    instructions = (
"Organize os blocos para desenhar os círculos coloridos."
)    
    descrição = (
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code> {instructions}</br>"""
    )
    yaml = f"""\
problem_name: {nome} 

problem_subtitle: {subt}

problem_category: {categoria}

problem_description: |
  {descrição}
   
code_lines: |
    def setup(): #0given
    size(400, 400) #1given
    for i in range(2, 18):
    if i % 2 == 0:
    stroke(255)
    else:
    stroke(0)
    y = 10 + i * 20
    line(50, y, width - 50, y) 
  
test_fn: setup
"""
    with open(file + '.yaml', 'w') as f:
        f.write(yaml)
    
    
    

