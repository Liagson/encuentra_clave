"""
-Python 2.7-
Recomiendo ejecutarlo como: $> python main.py > fichero
"""
import funciones as f

fichero = "p059_cipher.txt"
lista_caracteres_fichero = f.lectura_fichero(fichero)
clave = ["a", "a", "a"]

while (clave != "X"):
		clave_extendida = f.extensor_clave(clave, len(lista_caracteres_fichero))
		resultado = f.operacion_xor(clave_extendida, lista_caracteres_fichero)
		resultado_merged = f.merge_resultado(resultado)
		
		concentracion_e = f.contar_letra_e(resultado_merged)
		if (concentracion_e):
			print "Clave:", clave
			print resultado_merged		

		clave = f.generador_clave(clave)