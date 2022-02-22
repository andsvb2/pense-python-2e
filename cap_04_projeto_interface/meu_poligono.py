
#!/usr/bin/env python3

import turtle

# Definições das funções
def square(x, comprimento):
    for i in range(4):
        x.fd(comprimento)
        x.lt(90)

def polygon(x, n, comprimento):
    angulo = 360 / n
    for i in range(n):
        x.fd(comprimento)
        x.lt(angulo)


# Cria 'bob'.
bob = turtle.Turtle()


# Chama a função
# square(bob, 150)

polygon(bob, 5, 150)

turtle.mainloop()
