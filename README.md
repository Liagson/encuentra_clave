# Encuentra la clave

##Descripción
Inspirado en un ejercicio del *proyecto Euler*, el programa busca la contraseña con la que se ha cifrado un texto en inglés. El proceso de cifrado se realiza mediante un [XOR](https://en.wikipedia.org/wiki/Exclusive_or) con la clave. El programa busca todas las posibles claves y hace un XOR con cada una sobre el texto cifrado, devolviendo los resultados más probables (*ver Detalles*)

##Detalles
El cifrado [one-time pad](https://en.wikipedia.org/wiki/One-time_pad) resulta imposible de descifrar siempre y cuando no se repita la clave o la clave no sea mas corta que el texto a cifrar. En el caso que trato aquí se trabaja este último punto ya que se opera sobre claves cortas (pocos carácteres) que se repiten hasta coincidir con el string de texto sin cifrar. 

Actualmente el programa tarda unos 8 segundos para probar todas las combinaciones de 3 carácteres en minúsculas. Cada carácter adicional multiplicaría por 26 el tiempo necesario.

El programa da por posible éxito la combinación que de más de un 10% de letras **e** sobre el texto descifrado. (Siendo la densidad aproximada en un texto escrito en inglés)
