# Registro de ideias e anotações de processo


## WIP

- página de rosto: Fazer em inglês e em português
- script para premarar código pro yaml automaticamente
   - problema com o !BLANK, pensar solução.

### Ideias para criar puzzles

series: 

100
110
120
130
140
150

200 ?
- Listas
- Dicts 
- Sets
- Compreensões ?????
- removendo itens

300 ?
- Random
- Perlin ?
- Mais atributos ???
- seno e cosseno
- remap e lerp
- easing

### Capítulo 1.0 do material-aulas (série 100)

- Nota, no momento "static mode" não funciona, então indentação tem que começar junto com size e formas básicas


#### 100 desenho básico

- setup, size e rect 

```python
def setup():
	size(400, 400)
    rect(100, 40, 150, 200)
```        

- formas

```python
rect(20, 10, 40, 80)     # retângulo (x, y, largura, altura)
ellipse(10, 20, 50, 50)  # oval (x, y, largura, altura)
line(10, 10, 50, 50)     # linha do ponto 1 ao ponto 2 (x1, y1, x2, y2)
point(100, 50)           # ponto em (x, y)
square(100, 50, 40)      # quadrado na posição x:100 y:50 e lado:40
circle(50, 100, 40)      # círculo na posição x:50 y:100 e diâmetro:40
```

- preenchimento verde

```python
fill(0, 255, 0)  # preenchimento verde
ellipse(50, 50, 50, 50)  # produz um círculo verde
```

- ligando e desligando traço e preenchimento

```python
no_fill()  # sem preenchimento, formas vazadas
stroke(0, 0, 255)  # exemplo de cor do traço azul cor (R, G, B)
stroke_weight(10)  # espessura do traço de contorno 10 pixels
no_stroke()  # sem traço de contorno
```

- fundo apaga o desenho anterior
```python

background(0, 255, 0)  # fundo verde, limpa a tela background(R, G, B)

#### 101 variávies

https://raw.githubusercontent.com/villares/material-aulas/main/Processing-Python-py5/variaveis.md

#### 102 Polígonos

- triângulo e quad

![](https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/assets/triangle_quad.png)


- Polígono com vértices

```python
size(400, 200)

begin_shape()  # inicia o desenho do polígono da esquerda
vertex(10, 10)
vertex(50, 50)
vertex(190, 30)
vertex(90, 150)
vertex(30, 100)
end_shape()  # encerra o desenho de um polígono aberto

begin_shape()  # inicia o desenho do polígono da direita
vertex(210, 10)
vertex(250, 50)
vertex(390, 30)
vertex(290, 150)
vertex(230, 100)
end_shape(CLOSE)  # encerra o desenho de um polígono fechado
```

- estrela de quatro pontas

```python
size(400, 400)
background(0, 0, 200)  # um fundo azul
x, y = width / 2, height / 2  # coordenadas do centro

largura_total, largura_menor = 250, 150
a = largura_total / 2
b = largura_menor / 2

begin_shape()
vertex(x - a, y - a)
vertex(x - b, y)
vertex(x - a, y + a)
vertex(x, y + b)
vertex(x + a, y + a)
vertex(x + b, y)
vertex(x + a, y - a)
vertex(x, y - b)
end_shape(CLOSE)
```


#### 103 cores

https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/mais_sobre_cores.html

