def setup():
    size(400, 400)
    olho(100, 150, 100)
    olho(250, 250, 200)
        
def olho(x, y, tamanho):
    no_stroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho * 0.40)
    fill(200, 200, 0)
    circle(x, y, tamanho * 0.40)
    fill(0)
    circle(x, y, tamanho * 0.10)
    
### fim do código do quebra-cabeças - gerando metadados
def exiting():
    file = Path(__file__).stem
    save(file + '.png')
    print(file)
    nome = 'Função olho'
    subt = 'Definindo uma função de desenho e a chamando.'
    categoria = 'funções'
    descrição = (
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code> """
f"""Organize o bloco de definição da função olho para que ela """
f"""possa ser chamada no setup() e os olhos desenhados.</br>"""
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
  olho(100, 150, 100) #1given
  olho(250, 250, 200) #1given
  # definição do olho  #0given  
  def olho(x, y, tamanho): #0given
  no_stroke()  # sem contorno
  fill(255)  # branco
  ellipse(x, y, tamanho, tamanho * 0.40)
  fill(200, 200, 0) # amarelo
  circle(x, y, tamanho * 0.40)  # iris
  fill(!BLANK)   # preto (0)
  circle(x, y, tamanho * 0.10)  # pupila
  
test_fn: setup
"""
    with open(file + '.yaml', 'w') as f:
        f.write(yaml)
    
    
    
