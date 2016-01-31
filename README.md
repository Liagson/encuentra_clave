# Encuentra la clave (Beta)

##Descripción
Inspirado en un ejercicio del proyecto Euler, el programa busca la contraseña con la que se ha cifrado un texto. El proceso de cifrado se realiza mediante un XOR con la clave, por lo que el programa busca claves a fuerza bruta y hace un XOR sobre el texto cifrado. 
El cifrado one-time pad resulta imposible de descifrar siempre y cuando no se repita la clave o la clave no sea mas corta que el texto a cifrar. En el caso que trato aquí se trabaja este último punto ya que se opera sobre claves cortas (pocos carácteres) que se repiten hasta coincidir con el string de texto sin cifrar. 
