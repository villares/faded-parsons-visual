
def setup(): #0given
    size(400, 400) #1given
    background(240, 240, 200)  #1given
    translate(200, 300) # muda a origem#1given
    galho(60) #1given
# defina a função galho() #0given
def galho(tamanho):
    # uma linha vertical #1given
    line(0, 0, 0, -tamanho)
    # 30 graus em radianos #1given
    angulo = radians(30)
    # fator para encurtar 20% o galho #1given
    encurtamento = 0.8
    # o "if" limita chamadas recursivas pelo tamanho #1given
    if tamanho > 5:
        # desloca origem para ponta da linha #2given
        translate(0, -tamanho)
        # gira o sistema de coordenadas do canvas 30° #2given
        rotate(angulo)
        # chamando um dos lados #2given
        galho(tamanho * encurtamento)
        # gira o sistema de coordenadas 2 x -30° #2given
        rotate(2 * -angulo)     
        # chamando o outro lado #2given
        galho(tamanho * encurtamento)  # desenha outra linha
        # gira 30° o canvas o deixando como no início #2given
        rotate(angulo)
        # translação final que desfaz o deslocamento inicial #2given
        translate(0, tamanho)   # translação final que desfaz o deslocamento
        
# END PUZZLE
file = Path(__file__).stem
name = 'Função árvore'
subt = 'Definindo uma função recursiva.'
dcat = '120 - funções'
desc = (
f"""<h6>{name}</h6>"""
f"""<img src="parsons_probs/{file}.png"></br>"""
f"""<code>{subt}</code> """
f"""Organize o bloco de definição da função galho para que ela"""
f"""possa ser chamada no setup() e a árvore desenhada.</br>"""
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
    
    
    
