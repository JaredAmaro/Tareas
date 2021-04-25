#Importables librería
from ConexionFTP import *

# Variables de conexión
server = "ftpupload.net";       # Nombre del Dominio
user = "epiz_25466257";         # Usuario
password = "PzN8oatetZyxe";     # Contraseña
pathFileLocal = "";             # Directorio local, la ruta se utiliza para subir o descargar el archivo
pathFileFTP = "htdocs";         # Directorio Remoto FTP, la ruta se utiliza para subir o descargar el archivo
fileName =  "FTP2.txt";        # Nombre completo del Archivo a subir, ejemplo:  archivoPrueba.jpg


print("El proceso mando un: "+str(TestConexionFTP(server,user,password)));

print("El proceso mando un: "+str(UpLoadfileFTP(server,user,password,pathFileLocal,pathFileFTP,fileName)));