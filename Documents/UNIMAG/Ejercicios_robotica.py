
#Ejercicio 1
def max_dos(A,B):
    if A>B:
        C = A
    else:
        C = B
    return C

A = 84
B = 34
C = max_dos(A,B)
print(C)

#Ejercicio 2

def max_tres(A,B,C):
    if A>B and A>C:
        D = A
    elif B>A and B>C:
        D = B
    else:
        D = C
    return D

A = 10
B = 3
C = 8
D = max_tres(A,B,C)
print(D)

#Ejercicio 3

def long_list(Lista):
    long = 0
    for i in Lista:
        long += 1
    return long

Lista = [1, 2, 3, 4, 5, 6, 7, 8]
long = long_list(Lista)
print(long)

#Ejercicio 4

def carac_fun(vocal):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if vocal in vocales:
        return True
    return False

vocal = 'r'
sal = carac_fun(vocal)
print(sal)

#Ejercicio 5

def fun_sum(lista):
    resul = 0
    for i in lista:
        resul += i
    return resul

lista = [1, 2, 3]
resul = fun_sum(lista)
print(resul)

def fun_mul(lista):
    resul = 1
    for i in lista:
        resul *= i
    return resul

lista = [1, 2, 3, 4]
resul = fun_mul(lista)
print(resul)

#Ejercicio 6

def fun_super(lista1,lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False
    
lista1 = ['x', 'l']
lista2 = ['a', 'b', 'c', 'd']
print(fun_super(lista1,lista2))

#Ejercicio 7

def gen_carac(A,B):
    resul = B*A
    return resul

A = 10
B = 'x'
print(gen_carac(A,B))

#Ejercicio 8
def max_n_num(lista):
    c = 0
    for i in lista:
        if i>c:
           c = i
    return c

lista = [1, 24, 34, 56, 2, 1, 59]
print(max_n_num(lista))

#Ejercicio 9
def mas_larga(lista):
    palabra = len(lista[0]) 
    mostrar = lista[0]      
    for i in lista:
        if palabra <= len(i):  
            mostrar = i   
            palabra = len(i) 
        else:
             mostrar = mostrar
    return mostrar

lista = ['david', 'Guerrero', 'educacionfisica']
print(mas_larga(lista))

#Ejercicio 10
def filtrar_palabras(lista, n):
    mostrar = []
    for i in lista:
        if len(i) >= n:
            mostrar.append(i)
    return mostrar

lista = ['davi', 'Guerrero', 'caro']
n = 5
print(filtrar_palabras(lista,n))

#Ejercicio 11
def c_mayus():
    cadena = input('Ingrese una cadena: ')
    mayus = 0
    for i in cadena:
        if i.isupper():
            mayus += 1
    print('La cadena tiene',mayus, 'Mayusculas')
             
c_mayus()

#Ejercicio 12
def bintoint(binario): #101
    bin = str(binario) # '101'
    entero = 0
    exp = len(bin) -1  # 3
    for i in bin:
        entero += int(i) * 2 ** exp 
        exp -= 1
    return entero

binario = 1111111111111101110101
print(bintoint(binario))

#Ejercicio 13
def tup():
    t = []
    tu = ()
    print('Ingrese 10 edades')
    for i in range(10):
        e = int(input())
        t.append(e)
        tu = t
        
    con = 0
    for j in tu:
            if j > 20:
                con += 1
    return con


print(tup())

#Ejercicio 14
def B_letra(lista): # ['david', 'andres', 'ana', 'isaac']
    letra = input('Ingrese la letra de los nombres que quiere buscar: ')
    cont = 0
    for i in lista:
        nombre = list(i)
        if letra == nombre[0]:
            cont += 1
    return cont

lista = ['DAvid', 'Andres', 'Ana', 'Jose', 'Alejo']
print(B_letra(lista))

#Ejercicio 15
def contar_vocales():
    palabra = input('Ingrese una palabra: ')
    pal = list(palabra)
    conta = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for i in palabra:
        if i == 'a' or i == 'A':
            conta['a'] += 1
        elif i == 'e' or i == 'E':
            conta['e'] += 1
        elif i == 'i' or i == 'I':
            conta['i'] += 1
        elif i == 'o' or i == 'O':
            conta['o'] += 1
        elif i == 'u' or i == 'U':
            conta['u'] += 1
    return conta

print(contar_vocales())