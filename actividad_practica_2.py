# 1Declara dos variables, llamadas nombre y edad.
#   Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.

"""Punto 1"""
nombre = "Tony Soprano"
edad = 51


# 2 Crea tres variables:
    #nombre
    #apellido
    #nombrecompleto
# A nombre, asígnale el valor "Julia", y en apellido, 
#asigna el valor "Roberts". Finalmente, 
#construye la variable nombrecompleto concatenando 
#las variables (recuerda sumar un espacio intermedio).


"""Punto 2"""
nombre = "Julia"
apellido = "Roberts"
nombreCompleto = nombre + apellido


# 3) Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:
#Estás tomando un curso de curso
#Para ello deberás concatenar la primera parte de la 
# frase con el valor que asumirá la variable. 
# Recuerda agregar un espacio antes de concatenar la 
# variable al resto del texto.


"""Punto 3"""
curso = "Python"
print('Estás tomando un curso de ' + curso)


# 4)Práctica con Integers
# Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.

# Imprime el tipo de dato de dicha variable.

"""Punto 4"""
num_entero = 21
print(type(num_entero))


# 5)Práctica con Floats
# Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.

# Imprime el tipo de dato de dicha variable.

"""Punto 5"""
num_decimal = 50.7
print(type(num_decimal))


# 6)Práctica con Tipos de Datos Numéricos
# ¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.

# Para ello, crea dos variables:

# num1 = 7.5

# num2 = 2.5

# A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.

"""Punto 6"""
num1 = 7.5
num2 = 2.5
resultado = num1 + num2
print(type(resultado))


# 7) Práctica con Conversiones 1
# Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
# num1 = 7.5

"""Punto 7"""
num1 = 7.5
int(num1)
print(type(num1))


# 8)Práctica con Conversiones 2
# Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
# num2 = 10

"""Punto 8"""
num2 = 10
int(num2)
print(type(num2))


# 9) Práctica con Conversiones 3
# Suma los valores de num1 y num2.
# No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().

# num1 = "7.5"
# num2 = "10"

# print(num1 + num2)

"""Punto 9"""
print(num1 + num2)


# 10) Práctica Formatear Cadenas 1
# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.

# nombre_asociado = "Jesse Pinkman"
# numero_asociado = 399058

"""Punto 10"""
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print('Estimado {}, su numero de asociado es: {}'.format(nombre_asociado,numero_asociado))


# 11) Práctica Formatear Cadenas 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto
# puntos_nuevos = 350
# puntos_totales = 1225

"""Punto 11"""
puntos_nuevos = 350
puntos_totales = 1225
print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos')


# 12)Práctica Formatear Cadenas 3
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos

"""Punto 12"""
puntos_anteriores = puntos_totales
puntos_totales = puntos_anteriores + puntos_nuevos
print('Has ganado {} puntos! En total, acumulas {} puntos'.format(puntos_nuevos,puntos_totales))


# 13)Práctica Operadores Matemáticos 1
# Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.

# Debes mostrar solo el valor numérico que resulta de esta operación.

"""Punto 13"""
resultado = 824 / 27
print(resultado)


# 14) Práctica Operadores Matemáticos 2
# Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.

# Debes mostrar solo el valor numérico que resulta de esta operación.

"""Punto 14"""
modulo = 456 % 33
print(modulo)


# 15)Práctica Operadores Matemáticos 3
# Calcula y muestra en pantalla la raíz cuadrada de 783.

# Debes mostrar solo el valor numérico que resulta de esta operación.

"""Punto 15"""
raiz = 783**0.5
print(raiz)


# 16) Práctica Redondeo 1
# Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.

"""Punto 16"""
resultado = 10/3
print(round(resultado,2))


# 17) Práctica Redondeo 2
# Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.

"""Punto 17"""
print(round(10.676767))


# 18) Práctica Redondeo 3
# Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.

"""Punto 18"""
raiz = 5**0.5
print(round(raiz))