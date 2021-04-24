import base64 as b64

archivo_lectura=open("texto.txt","r")
archivo_escritura=open("resultado.txt","w")
texto_sin_codificar=archivo_lectura.read()

texto_codificado= b64.b64encode(bytes(texto_sin_codificar,"UTF-8"))
print("El texto codificado es {}", format(texto_codificado))

texto_decodificado=b64.b64decode(texto_codificado)
print("El texxto decodificado es: {} ", format(texto_decodificado))

archivo_escritura.write(str(texto_codificado))
archivo_escritura.write(str(texto_decodificado))
archivo_escritura.close()
archivo_lectura.close()