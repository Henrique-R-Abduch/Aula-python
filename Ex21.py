#21. Entrar via teclado com dois valores quaisquer. Após a digitação, exibir um seletor de opções (“menu”) 
# com as seguintes opções: (Fazer esse exercício utilizando If..Else e/ou Case)
while True:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    opcao = str(input("""Selecione uma opção:
            1 - Multiplicação
            2 - Adição
            3 - Divisão
            4 - Subtração
            5 - Fim de processo (sair do programa)"""))
    while opcao not in "1" and opcao not in "2" and opcao not in "3" and opcao not in "4" and opcao not in "5":
        print('-=' * 20)
        print("Opção inválida")
        opcao = str(input("""Selecione uma opção:
        1 - Multiplicação
        2 - Adição
        3 - Divisão
        4 - Subtração
        5 - Fim de processo (sair do programa)"""))

    if (opcao == "1"):
        n3 = n1 * n2
        print(f"O resultado foi {n3}")
    elif (opcao == "2"):
        n3 = n1 + n2
        print(f"O resultado foi {n3}")
    elif (opcao == "3"):
        if (n1 == 0 and n2 == 0):
            print("Erro!")
        else:
            n3 = n1 / n2
            print(f"O resultado foi {n3}")
    elif (opcao == "4"):
        n3 = n1 - n2
        print(f"O resultado foi {n3}")
    elif (opcao == "5"):
        print("Finalizando o programa...")
        break
  
print("Programa finalizado")



