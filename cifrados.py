# Declaramos la variable cifrado para almacenar el texto
cifrado = ""

# Se solicita una frase para cifrarla
frase = input("Ingresa una frase: ")

# Definimos el numero de posiciones que se desplazaran las letras
desplazamiento = 3

# Se hace la iteracion sobre cada caracter de la frase ingresada
for caracter in frase:

    # Verificacion si el caracter es una letra
    if caracter.isalpha():

        # Se obtiene el valor ASCII del caracter
        valor_ascii = ord(caracter)

        # Determinamos las letras minusculas y mayusculas
        if 'a' <= caracter <= 'z':  
            inicio = ord('a')
            limite = ord('z')
        elif 'A' <= caracter <= 'Z':
            inicio = ord('A')
            limite = ord('Z')
        
        # Aplicamos el desplazamiento
        valor_ascii += desplazamiento

        # Si la letra sale del rango se regresa al inicio restando 26 caracteres
        if valor_ascii > limite:  
            valor_ascii -= 26  
        
        # Se convierte el valor ASCII a caracter y lo agregamos al texto cifrado
        cifrado += chr(valor_ascii)
    else:
        # Si no es una letra se deja igual
        cifrado += caracter  

# Mostramos el texto cifrado
print("Texto cifrado:", cifrado)

