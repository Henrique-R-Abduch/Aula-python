# Entrar via teclado com “N” valores quaisquer. O valor “N” (que representa a quantidade de números) será digitado, deverá ser positivo, mas menor que vinte. Caso a quantidade não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. Após a digitação dos “N” valores, exibir: a) O maior valor, b) O menor valor, c) A soma dos valores, d) A média aritmética dos valores, e) A porcentagem de valores que são positivos, f) A porcentagem de valores negativos;

print("Digite N valores positivos")
i = 0
soma = 0
maior = 0
menor = 0
pos = 0
neg = 0
n = int(input("Digite a quantidade de valores: "))
while i < n:
    valor = int(input("Digite um valor: "))
    if valor > 0:
        if i == 1:
            menor = valor
        i = i + 1
        soma = soma + valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        pos = pos + 1
    if valor < 0:
        if i == 1:
            menor = valor
        i = i + 1
        soma = soma + valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        neg = neg + 1
print("O maior valor é: ", maior)
print("O menor valor é: ", menor)
print("A soma dos valores é: ", soma)
print("A média aritmética dos valores é: ", soma / n)
print("A porcentagem de valores que são positivos é: ", pos / n * 100)
print("A porcentagem de valores negativos é: ", neg / n * 100)