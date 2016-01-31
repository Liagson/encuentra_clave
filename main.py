#Python 2.7#

import enchant

#fichero = nombre del fichero a descifrar

def lectura_fichero(nombre_fichero):
	#Lectura y separacion de caracteres en una lista
	fichero = open(nombre_fichero, "r")
	lista_caracteres_ascii_fichero = []

	contenido_fichero = fichero.read()
	lista_caracteres_fichero = contenido_fichero.replace("\n", "").split(",")
	
	#Pasamos de string de numeros a un int
	for posicion in lista_caracteres_fichero: lista_caracteres_ascii_fichero.append(int(posicion))

	return lista_caracteres_ascii_fichero

def generador_clave(clave_anterior):
	#Actualiza la clave a la siguiente combinacion
	#Cuando completamos todas las combinaciones devolvemos un "X"
	clave_nueva = clave_anterior[:]
	if (clave_anterior[2] != "z"):
		clave_nueva[2] = chr(ord(clave_anterior[2]) + 1)
		return clave_nueva
	elif (clave_anterior[1] != "z"):
		clave_nueva[2] = "a"
		clave_nueva[1] = chr(ord(clave_anterior[1]) + 1)
		return clave_nueva
	elif (clave_anterior[0] != "z"):
		clave_nueva[2] = "a"
		clave_nueva[1] = "a"
		clave_nueva[0] = chr(ord(clave_anterior[0]) + 1)
		return clave_nueva
	else:
		return "X" 

def extensor_clave(clave, tamano_fichero):
	#Deja la clave tan larga como el fichero (a base de repetir la clave)
	nueva_clave = clave[:]
	for contador in range(0, (tamano_fichero /  len(clave))): 
		nueva_clave+=clave
		
	for contador in range(0, len(nueva_clave) % tamano_fichero): 
		nueva_clave.pop()
	return nueva_clave

def operacion_xor(clave, lista_caracteres_fichero):
	#Saca un array con todas las letras descifradas
	resultado = []
	for posicion in range(len(lista_caracteres_fichero)):
		letra_descifrada = ord(clave[posicion]) ^ lista_caracteres_fichero[posicion]
		resultado.append(chr(letra_descifrada))
	return resultado


def merge_resultado(array_resultado):
	#Une las letras del array resultado que ha dado la operacion_xor()
	resultado_en_palabras = ""
	for letra in array_resultado: resultado_en_palabras+=letra

	return resultado_en_palabras

def comprobar_palabra(palabra, diccionario):
	return diccionario.check(palabra)



"""
-Programa Principal-
Recomiendo ejecutarlo como: $> python main.py > fichero
"""

lista_caracteres_fichero = lectura_fichero(fichero)
clave = ["a", "a", "a"]
diccionario = enchant.Dict("en_US")

while (clave != "X"):
		clave_extendida = extensor_clave(clave, len(lista_caracteres_fichero))
		resultado = operacion_xor(clave_extendida, lista_caracteres_fichero)
		resultado_merged = merge_resultado(resultado)
		if (resultado_merged.find("and") != -1) and (resultado_merged.find("the") != -1):
			print "Clave:", clave
			print resultado_merged		
		clave = generador_clave(clave)