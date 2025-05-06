#Funções em python inicia com a palavra
#reservada def.
#Funções são rotinas em seu conceito
# Um algorítmo é composte de várias funções associadas
#rotina - fazem sentido pra algo que eu vou ter qque fazer toda hora (tirar media ex)


# def mostrar_linha():
#     print(30*"=") # VAI ESCREVER 30X O QUESTÁ DENTRO DA STRING # 

# mostrar_linha()
# print('MODULO 01')
# mostrar_linha()
# print('ALGORÍTMOS')
# mostrar_linha()
# print('ANÁLISE DE DADOS')


# def saudacao(nome):
#     print(f'Olá {nome}!')

# nome = input('Informe o nome: ')
# saudacao(nome)

# def somar(a, b):
#     s = a + b
#     print(soma)

# soma = 0 # da forma como está aqui essa variável não será manipulada então o programa não realizará a adição esperada 
# somar(4, 5)
# print (f'O valor da variável soma é {soma}')


#BOAS PRÁTICAS CADA FUNÇÃO FAZ UMA COISA
# def somar(a, b):
#     soma = a + b
#     #print(soma)
#     return soma # poderia usa somente 's' pra facilitar o entendimento pois o RETURN leva o python volte para o início iso 

# soma = somar(4, 5)
# print (f'O valor da variável soma é {soma}')


#o programa vai fazer a leitura entender que precisar retornar / ao entender que a função existe vai para a segunda parte

def somar_numeros(x, y): # abre a função / importante colocar sempre a função no começo do código
    s = x + y
    return s
#obriga o usuário a digitar 3x o que está em n1 e n2 números

for i in range(3): 
    n1 = int(input('Informe o 1º número: '))
    n2 = int(input('Informe o 2º número: '))

    soma = somar_numeros(n1, n2)
print(soma)