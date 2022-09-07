#30. Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço 
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir 
# para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado e exibir o valor a ser pago no final.
cod = int(input("""
Código Condição de pagamento
1 -	À vista em dinheiro ou cheque, recebe 10% de desconto
2 -	À vista no cartão de crédito, recebe 15% de desconto
3 -	Em duas vezes, preço normal de etiqueta sem juros
4 -	Em quatro vezes, preço normal de etiqueta mais juros de 10%
"""))
valor = float(input("Digite quanto deseja pagar: "))
if (cod == 1):
    valor *= 0.9
    print(f"O valor a ser pago será de {valor}")
elif (cod == 2):
    valor *= 0.85

