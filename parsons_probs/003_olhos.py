def setup():
    size(400, 400)
    olho(100, 150, 100)
    olho(250, 250, 200)
        
def olho(x, y, tamanho):
    no_stroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho * 0.4)
    fill(0)
    circle(x, y, tamanho * 0.4)
    
    ### fim do código do quebra-cabeças
def exiting():
    file = Path(__file__).stem
    print(file)
    nome = 'Desenhando olhos'
    subt = 'Definindo uma função olho'
    categoria = 'funções'
    descrição = f"""<code>{subt}</code>
  Organize as linhas para formar o desenho abaixo</br>
  <img src="parsons_probs/{file}.png"></br>"""
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
  # definição do olho   
  def olho(x, y, tamanho): #1given
  no_stroke()
  fill(255)
  ellipse(x, y, !BLANK, tamanho * 0.4)
  fill(0)
  circle(x, y, !BLANK * 0.4)   
  
test_fn: setup
"""
    with open(file + '.yaml', 'w') as f:
        f.write(yaml)
    save(file + '.png')
    
    
