
#!/usr/bin/env python3

import turtle

# Definições das funções
def square(x, comprimento):
    for i in range(4):
        x.fd(comprimento)
        x.lt(90)


# Cria 'bob'.
bob = turtle.Turtle()


# Chama a função
square(bob, 150)

turtle.mainloop()
