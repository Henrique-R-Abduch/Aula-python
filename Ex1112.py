#11. Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão 
# digitados. Se a área for maior que 100, exibir a mensagem “Terreno grande”.
#12. Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão 
# digitados. Se a área for maior que 100, exibir a mensagem “Terreno grande”, caso contrário, 
# exibir a mensagem “Terreno pequeno”.



b = int(input("Digite o valor da base: "))
a = int(input("Digite o valor da altura: "))
area = b * a
if area > 100:
    print("Terreno grande")
else:
    print("Terreno pequeno")

