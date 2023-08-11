#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

ciudades=['Roma', 'Mendoza', 'Junin', 'Madrid', 'Miami']
print(ciudades)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(ciudades[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:


print (ciudades[1:4])


# 4) Visualizar el tipo de dato de la lista

# In[12]:


type(ciudades)


# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print (ciudades[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:


print(ciudades[:4])
    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:


ciudades.append('San Rafael')
ciudades.append('Madrid')
print(ciudades)





# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

ciudades.insert(3,'New York')
print(ciudades)



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

paises=['Argentina', 'Chile', 'Paraguay']
#ciudades = ciudades + paises
ciudades.extend(paises)
print(ciudades)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

ciudades.index('Madrid')



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:


ciudades.index('Santa Fe')


# 12) Eliminar un elemento de la lista

# In[25]:


ciudades.remove('New York')


# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:


ciudades.remove('New York')


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:


print(ciudades)
a = ciudades.pop()
print(a)


# 15) Mostrar la lista multiplicada por 4

# In[29]:


print(ciudades *4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

numeros_tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:


print(numeros_tupla[10:16])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in numeros_tupla)
print(30 in numeros_tupla)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

ciudades=['Roma', 'Mendoza', 'Junin', 'Madrid', 'Miami']
if not 'Paris' in ciudades:
    ciudades.append('Paris')
    print ('agregada')
else:
    print('ya existe')



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:


print(ciudades.count('Paris'))
print(numeros_tupla.count(4))


# 21) Convertir la tupla en una lista

# In[52]:


list(numeros_tupla)


# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


tuplas=(1,2,3,4,5,6)
v1, v2, v3= tuplas[:3]
print(v1)
print(v2)
print(v3)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:



dicc_ciudad={'ciudad': ciudades, 'pais':['Argentina', 'Brasil'], 'continente': ['America', 'Europa']}
print(dicc_ciudad)


# 24) Imprimir las claves del diccionario

# In[59]:

for clave in dicc_ciudad:
    print (clave)

print (dicc_ciudad.keys())


# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(dicc_ciudad['ciudad'])


