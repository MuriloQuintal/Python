numero = input("digite o valor a ser identificado: ")

adjacente = False
i = 0

while i < len(numero) - 1 and not adjacente:
    if numero[i] == numero[i+1]:
        adjacente = True
    i += 1    
