import py5_tools  #!REMOVE

# setup: configurações iniciais #0given
def setup(): #0given
    size(400, 400) #1given    
    global particula_0 #1given
    particula_0 = Particula(80, 10, 30) 
    #!REMOVE code to capture animation
#     py5_tools.animated_gif(file + '.gif', #!REMOVE
#                            duration=0.1,  #!REMOVE 
#                            frame_numbers=range(10,240,2)) #!REMOVE

def draw(): 
    background(0)  # atualização do desenho, fundo preto
    particula_0.desenha() 
    particula_0.atualize() 
# definição da classe #0given
class Particula(): #0given
    def __init__(self, x, y, tamanho): #1given
        self.x = x #2given
        self.y = y #2given
        self.tam = tamanho  #2given
        self.vx = random(-2, 2)  #2given
        self.vy = random(-2, 2)  #2given
        self.cor = color(random(128, 256),  # R  #2given
                         random(128, 256),  # G  #2given
                         random(128, 256),  # B #2given
                         200)  # alpha #2given

    def desenha(self):  #1given
        fill(self.cor)  #2given
        circle(self.x, self.y, self.tam)  #2given

    def atualize(self):  #1given
        self.x += self.vx  #2given
        self.y += self.vy  #2given
        if self.x > width + self.tam / 2: #2given
            self.x = -self.tam / 2 #3given
        if self.y > height + self.tam / 2: #2given
            self.y = -self.tam / 2 #3given
        if self.x < -self.tam / 2: #2given
            self.x = width + self.tam / 2 #3given
        if self.y < -self.tam / 2: #2given
            self.y = height + self.tam / 2 #3given



    
# END OF PUZZLE - GENERATING METADATA
file = Path(__file__).stem
name = 'Uma partícula'
subt = 'Exemplo de Orientação a Objetos'
dcat = '400 - Orientação a Objetos'
desc = (
f"""<h6>{name}</h6></br>"""
f"""<img src="parsons_probs/{file}.gif"></br>"""
f"""<code>{subt}</code></br>"""
f"""Organize os blocos para fazer um sketch como este."""
# f"""Note que o círculo, com a posição controlada pela ponta do mouse"""
# f""" não tem traço de contorno, e que o quadrado, sempre redesenhado"""
# f""" no mesmo lugar, tem um traço de contorno amarelo mais espesso."""
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
    