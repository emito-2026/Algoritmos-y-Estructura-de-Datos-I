# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

# Si la suma es menor o igual a 6:

# "La suma de tus dados es {suma_dados}. Lamentable"

# Si la suma es mayor a 6 y menor a 10:

# "La suma de tus dados es {suma_dados}. Tienes buenas chances"

# Si la suma es mayor o igual a 10:

# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.

from random import*

def lanzar_dados():
    dado_uno = randint(1,6)
    dado_dos = randint(1,6)
    return dado_uno,dado_dos

def evaluar_jugada(dado_uno,dado_dos):
    suma_dados = dado_uno+dado_dos
    if suma_dados <= 6:
        print(f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados > 6 and suma_dados < 10:
        print(f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    elif suma_dados >= 10:
        print(f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora')

dado_uno,dado_dos = lanzar_dados()
evaluar_jugada(dado_uno,dado_dos)


# Práctica sobre Interacción entre Funciones 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

def reducir_lista(lista_numeros):
    lista_numeros.sort()
    cant = len(lista_numeros)
    lista_numeros.pop(cant-1)
    
    for i in lista_numeros:
        cantidad = lista_numeros.count(i)
        if cantidad > 1:
            lista_numeros.pop(i)

    print(lista_numeros)

def promedio(lista_numeros):
    promedio = sum(lista_numeros)/len(lista_numeros)
    
    return f'Promedio: {promedio}'

lista_numeros = [1,2,15,7,2]
reducir_lista(lista_numeros)

resultado = promedio(lista_numeros)
print(resultado)


# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.


from random import*

def lanzar_moneda():
    resultado = choice(['Cara','Cruz'])
    return resultado

def probar_suerte(resultado,lista_numeros):
    if resultado == 'Cara':
        print('La lista se autodestruira')
        lista_numeros.clear()
        print(lista_numeros)
    elif resultado == 'Cruz':
        print('La lista fue salvada')
        print(lista_numeros)
    
resultado = lanzar_moneda()
probar_suerte(resultado,[1,2,3,4,5,6,7,8,9])


# -------------------------------------------------------------------------------------------------------------------------------------


# Práctica sobre Argumentos Indefinidos (*args) 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

def suma_cuadrados(*args):
    total = 0
    for i in args:
        i**2
        total += i
    return f'La suma de los cuadrados da: {total}'

resultado = suma_cuadrados(3,6,9)
print(resultado)


# Práctica sobre Argumentos Indefinidos (*args) 2
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    total = sum(args)
    return f'La suma de los numeros da: {total}'

resultado = suma_absolutos(3,5,7,9)
print(resultado)

# Práctica sobre Argumentos Indefinidos (*args) 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

# La función debe devolver el siguiente mensaje:

# "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    
    return f'{nombre}, la suma de tus numeros es {suma_numeros}'

resultado = numeros_persona('Emiliano',2,4,6,9)
print(resultado)


# -------------------------------------------------------------------------------------------------------------------------------------


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    cont = 0
    for i in kwargs:
        cont += 1
    
    print(f'Hay {cont} atributos')

cantidad_atributos(color='rojo',marca='ferrari')

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)

    print(lista)

lista_atributos(nombre='Gladiador',genero='Acción',anio=2000)

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:

# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# Mostrará en pantalla:

# Características de María:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(nombre,**kwargs):
    print(f'Caracteristicas de {nombre}')
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')

describir_persona('Maria',pais='Argentina',color_pelo='negro',altura=1.70,edad=20)