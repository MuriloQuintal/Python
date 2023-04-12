import math
x1 = int(input("Insira o valor de x1: "))
y1 = int(input("Insira o valor de y1: "))
x2 = int(input("Insira o valor de x2: "))
y2 = int(input("Insira o valor de y3: "))
distancia = math.sqrt(((x1-x2)**2)+((y1-y3)**2))
if distancia >= 10:
    print("longe")
else:
    print("perto")
