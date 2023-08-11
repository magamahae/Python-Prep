#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def FcPrimo(num):
    es_primo = True 
    for i in range(2, num):
        if num % i == 0:  
            es_primo = False 
            break 
    
    return es_primo 



# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:


def ListaPrimos(lista):
    extra=[]
    for elemento in lista:
        if FcPrimo(int(elemento)):
            extra.append(elemento)
    return extra

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def MasRepetido(lista):
    unicos = []
    repeticiones = []
    if len(lista) == 0:
        return None
    
    for elemento in lista:
        if elemento in unicos:
            i = unicos.index(elemento)
            repeticiones[i] += 1
        else:
            unicos.append(elemento)
            repeticiones.append(1)
    
    moda = unicos[0]
    maximo = repeticiones[0]
    for i, elemento in enumerate(unicos):
        if repeticiones[i] > maximo:
            moda = unicos[i]
            maximo = repeticiones[i]
    return moda, maximo



# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def CambiaGrados(valor, origen, destino):
    if origen == 'celsius':
        if destino == 'celsius':
            valor_destino = valor 
        elif destino == 'farenheit':
            valor_destino = (valor * 9 / 5) + 32 
        elif destino == 'kelvin':
            valor_destino = valor + 273.15  
        else:
            print('Parámetro de Destino incorrecto')  
    elif origen == 'farenheit':
        if destino == 'celsius':
            valor_destino = (valor - 32) * 5 / 9
        elif destino == 'farenheit':
            valor_destino = valor 
        elif destino == 'kelvin':
            valor_destino = ((valor - 32) * 5 / 9) + 273.15  
        else:
            print('Parámetro de Destino incorrecto')
    elif origen == 'kelvin':
        if destino == 'celsius':
            valor_destino = valor - 273.15  
        elif destino == 'farenheit':
            valor_destino = ((valor - 273.15) * 9 / 5) + 32  
        elif destino == 'kelvin':
            valor_destino = valor  
        else:
            print('Parámetro de Destino incorrecto')  
    else:
        print('Parámetro de Origen incorrecto')  
    
    return valor_destino


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

print('1 grado Celsius a Celsius:', CambiaGrados(1, 'celsius', 'celsius'))
print('1 grado Celsius a Kelvin:', CambiaGrados(1, 'celsius', 'kelvin'))
print('1 grado Celsius a Farenheit:', CambiaGrados(1, 'celsius', 'farenheit'))
print('1 grado Kelvin a Celsius:', CambiaGrados(1, 'kelvin', 'celsius'))
print('1 grado Kelvin a Kelvin:', CambiaGrados(1, 'kelvin', 'kelvin'))
print('1 grado Kelvin a Farenheit:', CambiaGrados(1, 'kelvin', 'farenheit'))
print('1 grado Farenheit a Celsius:', CambiaGrados(1, 'farenheit', 'celsius'))
print('1 grado Farenheit a Kelvin:', CambiaGrados(1, 'farenheit', 'kelvin'))
print('1 grado Farenheit a Farenheit:', CambiaGrados(1, 'farenheit', 'farenheit'))


# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

metricas = ['celsius', 'kelvin', 'farenheit']  # Lista de las unidades métricas

for i in range(0, 3):
    for j in range(0, 3):  
       
        print('1 grado', metricas[i], 'a', metricas[j], ':', CambiaGrados(1, metricas[i], metricas[j]))



