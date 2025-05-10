# TP 4 - Estructuras Repetitivas
# Autor: Javier Gomez Frey

# Actividad 1: Imprimir los números del 0 al 100 (inclusive)
for i in range(101):
    print(i)

# Actividad 2: Contar cuántos dígitos tiene un número ingresado
numero = input("Ingresa un número entero: ")
print("Cantidad de dígitos:", len(numero.lstrip('-')))

# Actividad 3: Sumar todos los números entre dos valores, sin incluirlos
a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("La suma es:", suma)

# Actividad 4: Sumar números hasta que el usuario ingrese un 0
total = 0
while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    total += num
print("Total acumulado:", total)

# Actividad 5: Juego para adivinar un número entre 0 y 9
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break

# Actividad 6: Imprimir los números pares del 100 al 0 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Actividad 7: Sumar desde 0 hasta un número positivo ingresado
n = int(input("Ingresa un número positivo: "))
suma = sum(range(n + 1))
print("Suma:", suma)

# Actividad 8: Ingresar 100 números y clasificar par/impar y positivos/negativos
pares = impares = positivos = negativos = 0
for _ in range(100):  # Cambia 100 por un valor menor si querés probar
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# Actividad 9: Calcular la media de 100 números ingresados
total = 0
for _ in range(100):  # Cambia 100 por un valor menor si querés probar
    total += int(input("Ingresa un número: "))
print("Media:", total / 100)

# Actividad 10: Invertir los dígitos de un número ingresado
numero = input("Ingresa un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)
