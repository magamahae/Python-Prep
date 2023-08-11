#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

num= 7
if(num >0):
    print('el numero ' + str(num) + ' es mayor a 0')
elif(num <0):
    print('el numero ' + str(num) + ' es menor a 0')
else:
    print('el numero ' + str(num) + ' es igual a 0')



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

var1= 'hola'
var2 = 6+2j

if type(var1) == type(var2):
    print('las variables son del mismo tipo')
else:
    print('las variables son de distinto tipo')



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1,21):
    if(i%2==0):
        print ('el numero '  + str(i) + 'es primo')
    else:
        print ('el numero ' + str(i) + 'no es primo') 



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6):
    print('la potencia de ' + str(i) + ' elevado a la 3 es:' + str(i**3))



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

var = 4
for i in range(0,4):
    print('ciclo for ' + str(i) + 'cantidad de veces')



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

num= -4
if (type(num) == int):
    if (num ==0 or num<0):
        None
    if (num > 0):
        factorial = num
        while (num > 2):
            num = num - 1
            factorial = factorial * num
        print('El factorial es'+ str(factorial))
    
else:
    print('La variable no es un entero')



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

x=1
while x <5:
    for i in range (2,4):
        print(x+i)
    x+=1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:


for i in range(2,8):
    print ('hola, ni num es: ' + str(i))
    while i <5:
        print(i)
        i+=1


# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

rango0=0
rango1=30
primo = True

while (rango0 < rango1):
    for i in range(2, rango0):
        if (rango0 % i == 0):
            primo = False
    if (primo):
        print('es primo' + str(rango0))
    else:
        primo = True
    rango0 += 1


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
rango0=0
rango1=30
primo = True

while (rango0 < rango1):
    for i in range(2, rango0):
        if (rango0 % i == 0):
            primo = False
            break
    if (primo):
        print('es primo' + str(rango0))
    else:
        primo = True
    rango0 += 1



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:


#sin break
rango0=0
rango1=30
primo = True
bbreak=0

while (rango0 < rango1):
    for i in range(2, rango0):
        bbreak+=1
        if (rango0 % i == 0):
            primo = False
    if (primo):
        print('es primo' + str(rango0)+ 'ciclo sin break: ' + str(bbreak))
    else:
        primo = True
    rango0 += 1



    #con break
rango0=0
rango1=30
primo = True
brbeak=0

while (rango0 < rango1):
    for i in range(2, rango0):
        brbeak+=1
        if (rango0 % i == 0):
            primo = False
            break
    if (primo):
        print('es primo' + str(rango0)+ 'ciclos break:'+ str(brbeak))
    else:
        primo = True
    rango0 += 1


# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:


n=99
while (n<=300):
    if(n%12==0):
        print(n)
    n+=1


# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:


m=100
while n <= 300:
    if m % 6==0:
        print(m)
        break
    m+=1

