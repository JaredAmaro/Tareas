# Importamos librería
from ftplib import FTP

# Variables de Conexión
#servidor = "ftpupload.net"    
#user = "epiz_25466257"     
#password = "PzN8oatetZyxe"    

# Ésta función devolverá un True si la conexión fue exitosa o un False si hubo un error
def TestConexionFTP(server,user,password):
    # Instanciamos FTP
    try:
        test = FTP(server);  
        
        test.login(user,password);      # UserName #Password
        test.quit();                    # Cierra conexión
        return True;                    # Retorna un True == Conexión 
    except:
        return False;         

def UpLoadfileFTP(server,user,password,pathFileLocal,pathFileFTP,fileName):
    # CREA UN ARCHIVO EN EL SERVIDOR
    # Argument[0] = Nombre del Archivo, ejemplo "file.txt"
    # Argument[1] = -rw-r--r-- drwxr-xr-x
    #               w = write
    #               r = read    
    #               rb = ¿? 
    
    # Si la conexión falla, no continuar con ésta función
    if TestConexionFTP(server,user,password) == False:
        return False;
    else:
        # Conectando con el servidor   
        conexion = FTP(server);  
        #Logearse
        conexion.login(user,password);

        # La ruta de la carpeta donde queremos subir el archivo
        if (pathFileFTP != ""):
            conexion.cwd(pathFileFTP);

        # Intenta subir archivo
        try:
            file = open(fileName, "rb"); #pathFileFTP+

            conexion.storbinary("STOR "+str(fileName), file);
            file.close();

            conexion.quit();

            return True;
        except:
            return False;


def DownloadfileFTP(server,user,password,pathFileLocal,pathFileFTP,fileName):
    # Descargar un ARCHIVO EN EL SERVIDOR FTP
    # Argument[0] = Nombre del Archivo, ejemplo "file.txt"
    # Argument[1] = -rw-r--r-- drwxr-xr-x
    #               w = write
    #               r = read    
    #               rb = ¿? 
    
    # Si la conexión falla, no continuar con ésta función
    if TestConexionFTP(server,user,password) == False:
        return False;
    else:
       
        conexion = FTP(server);  
        
        conexion.login(user,password);

        
        conexion.cwd(pathFileFTP);

        
        try:
            file = open(pathFile+fileName, "wb");

            conexion.retrbinary("RETR FTP.txt",file.write);
            file.close();
            conexion.quit();

            return True;
        except:
            return False;