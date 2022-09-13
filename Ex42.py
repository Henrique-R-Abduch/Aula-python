#41. Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cem. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. A seqüência: 2, 5, 10, 17, 26, ....
a = 2
b = 5
v = (b - a) + 2
c = 2
n = 10
r = 5
while (c < n):
    n = int(input( "Digite o valor de n: " ))
    print(a)
    print(b)
    if n > 0 and n < 100:
        for i in range(1, n):
            r = v + r
            v = 2 + v 
            print(r)
            
    else:
        print( "Valor inválido" )
    c += 1
    