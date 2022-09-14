n1 = int(input("Digite o número inicial: "))
n2 = int(input("Digite o número final: "))
soma = 0

while (n1 <= n2):
    soma = soma + n1
    n1 = n1 + 1

print("A soma dos valores do intervalo é igual a: {}".format(soma))