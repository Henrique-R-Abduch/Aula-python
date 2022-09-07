#27. Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, 
# imprimir o resultado desta operação.
v = int(input("Digite um número: "))
if (v % 2 == 0):
    v += 5
    print(v)
elif (v % 2 == 1):
    v += 8
    print(v)

    
