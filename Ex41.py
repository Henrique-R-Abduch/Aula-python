# 40. Exibir os vinte primeiros valores da série de Bergamaschi. A série: 1, 1, 1, 3, 5, 9, 17, ...
a = 1
b = 1
c = 1
print(a)
print(b)
print(c)
for i in range(3,20):
    d = a + b + c
    print(d)
    a = b
    b = c
    c = d
 
