import random #Libreria para llamar y crear numeros randoms


numeros = [] #Coleccion vacia

for i in range(100): #Ciclo para repetir 100 veces las iteraciones
    n = random.randint(1,100) #Crea el numero entre 1 y 100
    numeros.append(n) #Guardamos en la lista el numero


print(numeros) #Vizualizamos lista

#Contador de numeros pares
contador = 0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        contador+=1
print(f"Cantidad de numeros pares : {contador}")