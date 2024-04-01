""" "# calculador comisiones:
nombre = input('Dime tu nombre:')
ingresos = float(input('Dime tus ingresos:'))
comision = ((ingresos * 13)/100)
print(f'El trabajador {nombre} ha logrado una comisión de {round(comision, 2)}')

# Analizador de texto:

texto = input("Por favor, ingresa un texto: ").lower()
letra1 = input("Ingresa la primera letra: ").lower()
letra2 = input("Ingresa la segunda letra: ").lower()
letra3 = input("Ingresa la tercera letra: ").lower()

print('Calcular la cantidad de letras:')
print(f"La letra '{letra1}' aparece {texto.count(letra1)} veces en el texto.")
print(f"La letra '{letra2}' aparece {texto.count(letra2)} veces en el texto.")
print(f"La letra '{letra3}' aparece {texto.count(letra3)} veces en el texto.")
print('--------------------------')

print('Calcular la cantidad de palabras:')
lista_texto = list(texto)
print(f"A lo largo del texto hay {len(lista_texto)} palabras.")
print('--------------------------')

print('Letras de inicio y fin')
print(f"La primera letra a lo largo del texto es {texto[0]} y la última letra a lo largo del texto es {texto[-1]}.")
print('--------------------------')

print('Letras de inicio y fin:')
print(f' el texto invertido es {texto[::-1].split()}')
print('-------------------------------')

print('Buscando la palabra python')
print(f"La palabra 'Python' se encuentra en en el texto: {'Python' in texto}.")"""



