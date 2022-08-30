#15. A partir de três valores que serão digitados, verificar se formam ou não um triângulo. 
# Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”. 
# Um triângulo escaleno possui todos os lados diferentes, o isósceles, dois lados iguais e o 
# eqüilátero, todos os lados iguais. Para existir triângulo é necessário que a soma de dois lados 
# quaisquer seja maior que o outro, isto, para os três lados.
#16. Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo 
# retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))
if l1 == l2 and l2 == l3:
    print("O triângulo é equilátero")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("O triângulo é escaleno")
else:
    print("O triângulo é isóceles")
if l1 ** 2 == ((l2 ** 2) + (l3 ** 2)):
    print("Formam um triângulo retangulo")
else:
    print("Não formam um triângulo retangulo")



