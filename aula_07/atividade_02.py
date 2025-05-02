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

# peso = float(input(f'Informe o peso do que foi pescado em quilos: '))
#     '''abaixo: se peso for maior que xyz, (saiba que excesso é = peso - 100 e multa é = excesso *4) imprima... se não imprima...'''
# if peso > 100:
#     excesso = peso - 100
#     multa = excesso * 4
#     print(f'peso máximo excedido, sua multa será de: {multa:.2f}') #''' chvs multa:.2f chvs explicação no fim'''
# else:
#     print('peso limite NÃO excedido, NÃO há multa')

''' {multa}: Insere o valor da variável multa na string

    :.2f: Especifica como formatar o número:

        : → Indica que vem uma especificação de formato

        .2 → Define 2 casas decimais

        f → Indica que é um número float (ponto flutuante)'''

''' tentando implementar utilizando "def"
A explicação simples de def seria definição e pode ser usado para definir um bloco de código a ser reutilizavel.

Quando em uso estou DEFININDO para o python que a seguir vou apresentar uma função que ele executará somente quando eu chamar por ela na linha de código. Como o programa é lido de cima pra baixo é importante que a função venha antes do processamento pois nessa etapa ao ser chamada o python já guardou a função na memoria.
Eu só vou apresentar as variáveis depois estabelecer def, então em def eu me refiro a uma variável que o python ainda não conhece
'''
def calc_multa(peso):
    if peso > 100:
        return (peso - 100) * 4  #se peso for maior que 100 então retorne e e calcule peso - 100 e multplique esse resultado por 4'
    return 0
#apresentando variáveis
#1ª Com input do usuário informando o peso
peso = float(input('Informe o peso do que foi pescado em quilos: '))
#sem input somente definindo o calculo  que a variável vai realizar quando chamada
multa = calc_multa(peso) #ou seja multa é igual ao que foi definido e ensnado no começo.

#processamento e resultados
if multa:
    print(f'Peso máximo excedido, sua multa será de:R$ {multa:.2f}') #insere valor da variavel multa,explica que haverá uma formatação do resultado, como formatar esse resultado (duas casas decimais), explica que git é um float
else:
    print('Peso limite NÃO excedido, NÃO há multa')

