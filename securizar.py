#Hacer un script de nombre securizar.py en el que se cree un nuevo JSON a
# partir de users.json de nombre secure-users.json en el que las contraseñas
# estén hasheadas (3 puntos)
import hashlib
import json
from openpyxl import load_workbook
import pandas as pd

def hashPswd(pswd):
    hasedPswd = hashlib.sha256(pswd.encode('utf-8')).hexdigest()
    return hasedPswd

with open("usrPswOriginal.txt", "r+") as archivo:
    contenido = archivo.read()
    data = json.loads(contenido)
    print(data)

    for u in data:
        print(u.get("password"))
        contraseñaHasseada = hashPswd(u.get("password"))
        print("Contraseña hasseada es: " + contraseñaHasseada)



    archivo.seek(0) # volvemos al inicio del archivo y lo truncamos para construirlo de nuevo
    archivo.truncate()

    with open("usrsJson.txt", "w") as archivo:
     json.dump(data, archivo)









