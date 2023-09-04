def setup():
    size(400, 400)
    for i in range(80):
        if i % 2 == 0:
            stroke(255)
        else:
            stroke(0)
        y = 10 + i * 20
        line(0, y, width, y)
        

### fim do código do quebra-cabeças - gerando metadados
def exiting():
    file = Path(__file__).stem
    save(file + '.png')
    print(file)
    nome = 'Pares e ímpares'
    subt = 'Usando o resto da divisão para alternar cores.'
    categoria = 'funções'
    instructions = "Organize os blocos para desenhar as linhas corretamente."
    
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
    def setup(): 
    size(400, 400)
    for i in range(80):
    if i % 2 == 0:
    stroke(255)
    else:
    stroke(0)
    y = 10 + i * 20
    line(0, y, width, y) 
  
test_fn: setup
"""
    with open(file + '.yaml', 'w') as f:
        f.write(yaml)
    
    
    

