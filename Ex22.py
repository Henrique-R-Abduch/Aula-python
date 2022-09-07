#22. Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os dados necessários para o 
# cálculo da respectiva área. Enviar mensagem de erro se o usuário escolher uma opção inexistente.


while True:
    o = str(input("""
    1 - Triângulo 
    2 - Quadrado
    3 - Retângulo
    4 - Círculo
    5 - Fim de processo
    Selecione a opção desejada: """))
    while o not in "1" and o not in "2" and o not in "3" and o not in "4" and o not in "5":
        o = str(input("""
        1 - Triângulo
        2 - Quadrado
        3 - Retângulo
        4 - Círculo
        5 - Fim de processo
        Selecione a opção desejada: """))
    if (o == "1"):
        l1 = int(input("Digite o primeiro valor: "))
        l2 = int(input("Digite o segundo valor: "))
        l3 = (l1 * l2) / 2
        print(f"A área do triângulo é de {l3}")
    elif (o == "2"):
        l1 = int(input("Digite o lado: "))
        l2 = (l1 ** 2)
        print(f"A área do quadrado é de {l2}")
    elif (o == "3"):
        l1 = int(input("Digite o primeiro valor: "))
        l2 = int(input("Digite o segundo valor: "))
        l3 = (l1 * l2)
        print(f"A área do retângulo é de {l3}")
    elif (o == "4"):
        r = int(input("Digite o valor do raio: "))   
        a = 3.14 . r 
        print(f"A área do circulo é de {a}")
    elif (o == "5"):
        print("Programa finalizado.")
        break
    







