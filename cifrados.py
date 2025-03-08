cifrado = ""
frase = input("Ingresa una frase: ")
desplazamiento = 3

for caracter in frase:
    if caracter.isalpha():
        valor_ascii = ord(caracter)
        if 'a' <= caracter <= 'z':  
            inicio = ord('a')
            limite = ord('z')

        valor_ascii += desplazamiento

        if valor_ascii > limite:  
            valor_ascii -= 26  

        cifrado += chr(valor_ascii)
    else:
        cifrado += caracter  

print("Texto cifrado:", cifrado)

