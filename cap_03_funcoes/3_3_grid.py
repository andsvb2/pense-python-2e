#!/usr/bin/env python3

# Feito consultando o código disponível em: https://github.com/AllenDowney/ThinkPython2/blob/master/code/grid.py
# Achei as definições de linhas e colunas um pouco frouxas.
# A grade gerada me parece ser uma grade 2x2, e não uma grade com 4 linhas e 4 colunas.

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def l_horizontal():
    print('+ - - - -', end=' ')

def l_vertical():
    print('|        ', end=' ')

def horizontais():
    do_twice(l_horizontal)
    print('+')

def verticais():
    do_twice(l_vertical)
    print('|')

def linha():
    horizontais()
    do_four(verticais)

def grade():
    do_twice(linha)
    horizontais()

grade()
