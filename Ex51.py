#51. Armazenar dez números na memória do computador. Exibir os valores na ordem inversa à da digitação.
num = []
for numeros in range(1,11):
    num.append(int(input("Digite um número: ")))
print(num[::-1])