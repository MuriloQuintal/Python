meuCartão = int(input("digite o num cartão: "))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
    cartãoLido = int(input("digite o proximo num cartão: "))
    if cartãoLido == meuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
    print("encontrei")
else:
    print("ainda nao econtrei")
