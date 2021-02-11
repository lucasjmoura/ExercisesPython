""""
Resolution of a list of decision structure python exercises

author lucas jesus de moura
lucas.j.m@outlook.com 
version: 0.1
"""

'''
Make a Program that asks for two numbers and prints the largest one.
'''
def questionOne():
    valores = input('digite dois numeros ').split()
    lista = []
    for x in valores:
        lista.append(int(x))
    return max(lista)
#questionOne()   

'''
Make a Program that asks for a value and shows on the screen whether the value is positive or negative.
'''
def questionTwo():
    number = int(input('digite um numero '))
    if number >=  0:
        return 'O numero é positivo'
    else:
        return 'O numero é negativo'
#questionTwo()

'''
Make a Program that checks if a letter typed is "F" or "M". As the letter writes: F - Female, M - Male, Invalid Gender.
'''
def questionThree():  
    letra = input('digite F ou M: ').lower()
    if letra == 'f':
        return 'F - Feminino'
    elif letra == 'm':
        return 'M - Masculino'
    else:
        return 'Sexo invalido'
    
#questionThree()  

'''
Make a Program that checks if a typed letter is a vowel or consonant.
'''
def questionFour():
    letra = input('Digite uma letra: ').lower()
    if letra in 'a,e,i,o,u':
        return 'Está letra é vogal'
    else:
        return 'Está letra é consoante'

#questionFour()    
        

'''
Make a program for reading a student's two partial grades. The program should calculate the average achieved by
student and present: The message "Approved", if the average achieved is greater than or equal to seven; The "Disapproved" message,
if the average is less than seven; The message "Approved with Distinction", if the average is equal to ten.
'''
def questionFive():
    valores = input('Digite 3 numeros com espaços: ').split()
    lista = []
    for x in valores:
        lista.append(int(x))
    soma= sum(lista)/2
    if soma == 10:
        return 'Aprovado com Distinção'
    elif soma >= 7:
        return 'Aprovado'
    elif soma < 7:
        return 'Reprovado'

#questionFive()    
'''
Make a Program that reads three numbers and shows the biggest one.
'''
def questionSix():
    valores = input('Digite 3 numeros com espaços: ').split()
    lista = []
    for x in valores:
        lista.append(int(x))
    return max(lista)   

#questionSix()

'''
Make a Program that reads three numbers and shows them in descending order.
'''
def questionSeven():
    valores = input('Digite 3 numeros com espaços: ').split()
    lista = []
    for x in valores:
        lista.append(int(x))
    return sorted(lista, reverse=True)

#questionSeven()

'''
Make a program that reads 2 numbers and then ask the user which operation he wants to perform.
The result of the operation must be accompanied by a sentence that says whether the number is: even or odd;
positive or negative; integer or decimal.
'''

  
num1, num2 = input('Digite um 2 valores: ').split()
operador = input('Digite um operador: div, adi, sub, mul...')


def validaPos(valor):
    valor = valor
    if valor >=  0:
        print ('O numero é positivo!')
    else:
        print ('O numero é negativo!')

def validaDeci(valor):
    valor = valor
    if(valor // 1 == valor): 
        print ('Número Inteiro!')
    else:
        return ('Número Decimal!')

def validaImp(valor):
    valor = valor
    if(valor % 2 == 0): 
        print ('Número Par!')
    else:
        print ('Número Impar!')


num1 = float(num1)
num2 = float(num2)

if operador == 'div':
    resultado = num1 / num2
    print(resultado)
    validaPos (resultado)
    validaDeci(resultado)
    validaImp(resultado)
    print(resultado)

if operador == 'mul':
    resultado = num1 * num2
    validaPos (resultado)
    validaDeci(resultado)
    validaImp(resultado)
    print(resultado)

if operador == 'sub':
    resultado = num1 - num2
    print(resultado)
    validaPos (resultado)
    validaDeci(resultado)
    validaImp(resultado)
    print(resultado)

if operador == 'adi':
    resultado = num1 - num2
    print(resultado)
    validaPos (resultado)
    validaDeci(resultado)
    validaImp(resultado)
    print(resultado)
