
# Práctica Loop For 1
# Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

# Por ejemplo: "Hola María"

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for i in alumnos_clase:
    print(f'Hola {i}')
print('Fin del bucle')


# Práctica Loop For 2
# Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros= 0
for i in lista_numeros:
    suma_numeros += i
print(f'El resultado de la suma de todos los numeros es: {suma_numeros}')
print('Fin')

# Práctica Loop For 3
# Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:


# *Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar

# num % 2 == 0 (valores pares)

# num % 2 == 1 (valores impares)

numeros_pares = 0
numeros_impares = 0

for i in lista_numeros:
    if (i%2 == 0):
        numeros_pares += i
    elif (i%2 == 1):
        numeros_impares += i

print(f'La suma de los numeros pares da: {numeros_pares}')
print(f'La suma de los numeros impares da: {numeros_impares}')
print('Fin')


# -------------------------------------------------------------------------------------------------------------------------------------
# Práctica Loop While 1
# Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.

numero = 10
while (numero > 0):
    numero -= 1
    print(numero)
print('Fin del bucle')


# Práctica Loop While 2
# Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:

# - Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

# - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).

numero = 50
print(numero)
while (numero > 0):
    numero -= 1
    if (numero%5 == 0):
        print(numero)
    else:
        continue
print('Fin del bucle')


# ----------------------------------------------------------------------------------------------------------------------------------
# Práctica Interrupción de Flujo
# Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# No debes cambiar el orden de la lista.

for i in lista_numeros:
    if (i>0):
        print(i)
    else:
        break
print('Fin del bucle')