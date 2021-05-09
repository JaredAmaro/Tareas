#VerIP
import subprocess

print("Configuracion de los DNS:")

ip=('netsh interface ipv4 show dns Wi-fi')

subprocess.run(ip,shell=True)
