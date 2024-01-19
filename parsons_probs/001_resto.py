def setup():
    size(400, 400)
    for i in range(2, 18):
        if i % 2 == 0:
            stroke(255)
        else:
            stroke(0)
        y = 10 + i * 20
        line(50, y, width - 50, y)
        

### fim do código do quebra-cabeças - gerando metadados
def exiting():
    file = Path(__file__).stem
    save(file + '.png')
    print(file)
    nome = 'Pares e ímpares'
    subt = 'Usando o resto da divisão para alternar cores.'
    categoria = 'laços de repetição'
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
    
    
    

