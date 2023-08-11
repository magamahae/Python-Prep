#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

num1=4
print (num1)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(num1))



# 4) Crear una variable que contenga tu nombre

# In[2]:


nombre='Maria Gabriela'

# 5) Crear una variable que contenga un número complejo

# In[3]:


complejo= 6+8j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


print(type(complejo))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:


booleano='True'
boolenado2=True
#no porque uno es str y el otro bool


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(booleano))
print(type(boolenado2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

resultado= 5 + 7.2



# 11) Realizar una operación de suma de números complejos

# In[2]:

suma_complejo= (5+4j) +(7+6j)
print(suma_complejo)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

suma_e_c= 4 + (8+4j)
print(suma_e_c)



# 13) Realizar una operación de multiplicación

# In[5]:

multiplica= 6*4
print(multiplica)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

eleva=2**8
print(eleva )


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

division=27/4
print(division)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

b= 27//4
print(int(division))
print(b)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
a=27%4
print(a)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

c=4*b+a
print(c)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

libro = 'la caperucita '
color = 'roja 2'
cuento = libro + color
print(cuento)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

'2' ==2
#porque uno es str y el otro int



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

int('2')==2



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float('3,8')
#xq no se puede convertir un str en float



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

var1=3
var1-=1
print(var1)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1<<2
#porque corre a la  izquierda 2 lugares o sea 100(binario)=4(decimal)



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


2+'2'
#xq int + str no se puede sumar
var2=2+2
var3='2'+'2'
#si son del mismo tipo, se puede +



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

num1= 3
var1='hola'
res= str(num1)+ var1
print(res)
#concatena


# %%
