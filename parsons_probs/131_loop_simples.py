tamanhos = [10, 20, 40, 50, 100, 110, 220, 230] # 0given

def setup(): #0given
    size(400, 400) #1given
    no_fill() # sem preenchimento
    for t in tamanhos:
        circle(200, 200, t)

### fim do código do quebra-cabeças - gerando metadados
def exiting():
    file = Path(__file__).stem
    save(file + '.png')
    print(file)
    nome = 'Pares e ímpares'
    subt = 'Usando o resto da divisão para alternar cores.'
    categoria = '130 - laços de repetição'
    instructions = (
"Organize os blocos para desenhar as linhas corretamente. "
"Note como a primeira linha é branca."
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
    
    
    

