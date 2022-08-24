#4. Calcular e exibir a média aritmética de quatro valores quaisquer que serão digitados.
num = []
for n in range(1, 5):
    n = int(input(f"Digite o valor {n}: "))
    num.append(n)
med = sum(num) / len(num)
print(f"A média aritmética é igual a {med}")
