# pescador só pode pescar até 100 kg sem pagar multa. Passando de 100 kg deverá pagar multa de 4 reais por kg
#logo o sistema só vai calcular o valor da multa se  antes o sistema identificar que o peso excedeu o limite


# limite = 100
# multa = 4
# peso = int(input('Informe o peso: '))
# if peso > 100:
#     multa = peso *0,4

'''Tentativa de resolver o problema em casa'''
#limite=100
#excesso=qualquer valor acima de 100
    # nesse caso informar o valor, calculado por quilo, da multa 
    # do contrário informar que não foi ultrapasado o peso limite

peso = float(input(f'Informe o peso da pescado em quilos: '))
'''abaixo: se peso for maior que xyz, (saiba que excesso é = peso - 100 e multa é = excesso *4) imprima... se não imprima...'''
if peso > 100:
    excesso = peso - 100
    multa = excesso * 4
    print(f'peso máximo excedido, sua multa será de: {multa:.2f}') #''' chvs multa:.2f chvs explicação no fim'''
else:
    print('peso limite NÃO excedido, NÃO há multa')

''' {multa}: Insere o valor da variável multa na string

    :.2f: Especifica como formatar o número:

        : → Indica que vem uma especificação de formato

        .2 → Define 2 casas decimais

        f → Indica que é um número float (ponto flutuante)'''