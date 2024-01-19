def setup():
    size(400, 400)
    background(0, 200, 0) # verde
    rect_mode(CENTER)
    circle(200, 50, 50)
    fill(0)  # preto
    ellipse(200, 150, 100, 50)
    fill(0, 0, 200)  # azul
    no_stroke() # desliga traço
    square(200, 250, 50)
    stroke(255, 255, 0) # amarelo
    fill(255, 0, 0)  # vermelho
    rect(200, 350, 100, 50)
    
### fim do código do quebra-cabeças - gerando metadados
def exiting():
    file = Path(__file__).stem
    save(file + '.png')
    print(file)
    nome = 'Desenho e cor'
    subt = 'Formas básicas, preenchimento e traço.'
    categoria = '100 Primeiros passos'
    instructions = "Organize os blocos para desenhar as figuras."

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
    background(0, 200, 0) # verde
    rect_mode(CENTER)
    circle(200, 50, 50)
    fill(0)  # preto
    ellipse(200, 150, 100, 50)
    fill(0, 0, 200)  # azul
    no_stroke() # desliga traço
    square(200, 250, 50)
    stroke(255, 255, 0) # amarelo
    fill(255, 0, 0)  # vermelho
    rect(200, 350, 100, 50)
  
test_fn: setup
"""
    with open(file + '.yaml', 'w') as f:
        f.write(yaml)
    
    
    
