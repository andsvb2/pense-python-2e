
#!/usr/bin/env python3

import math
import turtle

# Definições das funções
def square(x, comprimento):
    for i in range(4):
        x.fd(comprimento)
        x.lt(90)

def polygon(x, n, comprimento):
    angulo = 360 / n
    # print(comprimento*n)
    for i in range(n):
        x.fd(comprimento)
        x.lt(angulo)

def circle(x, r):
    circunferencia = 2 * math.pi * r
    # print(circunferencia)
    n = 50
    comprimento = circunferencia /n
    polygon(x, n, comprimento)

# Cria 'bob'.
bob = turtle.Turtle()

# Chama a função
# square(bob, 150)
# polygon(bob, 5, 150)
circle(bob, 50)

turtle.mainloop()
