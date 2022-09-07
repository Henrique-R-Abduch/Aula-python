#29. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))
if (v3 < v2 < v1):
    print(f"{v1} {v2} {v3}")
elif (v1 < v2 < v3):
    print(f"{v3} {v2} {v1}")
elif (v3 < v1 < v2):
    print(f"{v2} {v1} {v3}")
elif (v1 < v3 < v2):
    print(f"{v2} {v3} {v1}")
elif (v2 < v1 < v3):
    print(f"{v3} {v1} {v2}")
elif (v2 < v3 < v1):
    print(f"{v1} {v3} {v2}")


    