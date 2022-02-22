#!/usr/bin/env python3

def right_justify(x):
    tamanho_antes = 70 - len(x)
    espacos = " " * tamanho_antes
    string_exibir = espacos + x
    print(string_exibir)

entrada = input("Texto a ser justificado: ")
right_justify(entrada)
