#Um programa que, dado o número calcule o dobro, o triplo e o quadrado desse número para agilizar seus orçamentos
    #O dobro da quantidade solicitada (para ofertas promocionais)
    #O triplo (para grandes eventos)
    #E a area total de um adesivo considerando que o número informado e o lado do adesivo em centímetros 
#Crie uma função que faça esses calculos e apresente na tela os resultados

requisitos
#criar um função que receba um número;
#calcular o dobro,triplo e quadrado;
#retornar esses três valores para serem apresentados no programa principal


def calcula_numero(x):
    dob = x *2
    trip = x * 3
    quad = x ** 2

    return dob, trip, quad
n = int(input('informe o numero: '))

#chamdada de função

d, t, q = calcula_numero (n)
print (f'Dobro {d},tripl{t }, quadraduplo{q}')
