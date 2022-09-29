#52. Armazenar dez valores na memória do computador. Após a digitação dos valores, criar uma rotina para ler os valores e achar e exibir o maior deles.

lista = []

for i in range(1, 11):
    lista.append(int(input(f"Digite o valor {i}: ")))

print(f"{max(lista)}")
print(f"{min(lista)}")

