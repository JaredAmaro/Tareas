import smtplib
from decouple import config
#Como no puedo poner mi correo y contraseña no puedo ponerlo aqui por que tengo miedo...
message="Hola, un mensaje mio desde python!"
subject="Prueba de correo"

message="Subject:{}\n\n{}".format(subject, message)

server=smtplib.SMTP("jsimonist_t42j@bylup.com", 587)
server.starttls()
server.login("jsimonist_t42j@bylup.com", "nose21")

server.sendmail("jsimonist_t42j@bylup.com","jsimonist_t42j@bylup.com",message)

server = smtplib.SMTP('smtp.office365.com:587')

server.quit()

print("Correo enviado exitosamente!")