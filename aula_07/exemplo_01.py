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
def somar(a, b):
    soma = a + b
    #print(soma)
    return soma # podeia usa somente 's' pra facilitar o entendimento pois o RETURN leva o python volte para o início isola o que veio antes do return

soma = somar(4, 5)
print (f'O valor da variável soma é {soma}')