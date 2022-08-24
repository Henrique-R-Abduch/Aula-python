#7. Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um valor referente ao pagamento da somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.
lista = []
for n in range(1, 6):
    p = float(input(f"Digite o valor do produto {n}: "))
    lista.append(n)
v = float(input("Quanto você vai pagar? "))
r = v - sum(lista)
print(f"O troco será de: {r*-1}")
