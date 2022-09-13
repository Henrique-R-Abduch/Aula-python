print("Digite 10 valores positivos")
i = 0
soma = 0
maior = 0
while i < 10:
    valor = int(input("Digite um valor: "))
    if valor > 0:
        i = i + 1
        soma = soma + valor
        if valor > maior:
            maior = valor
    else:
        print("Valor inválido!")
print("O maior valor é: ", maior)
print("A soma dos valores é: ", soma)
print("A média aritmética dos valores é: ", soma / 10)