#39. Exibir os trinta primeiros valores da série de Fibonacci. A série: 1, 1, 2, 3, 5, 8, ...
a = 0
b = 1
cont = 3
print(a)
print(b)
while (cont <= 30):
    c = a + b
    print(c)
    a = b
    b = c
    cont += 1




