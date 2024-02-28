#Hacer un script tabla_users.py que introduzca a los usuarios con sus contraseñas hasheadas en un excel llamado usuarios.xlsx usando pandas
# y openpyxl (integrado en pandas) (2 puntos)
import array
import hashlib
import json
import pandas as pd
import datetime

#lo suyo seria acceder a el nuevo archivo json creado en securizar, no acceder al archivo original directamente
def hashPswd(pswd):
    hasedPswd = hashlib.sha256(pswd.encode('utf-8')).hexdigest()
    return hasedPswd
def crarExcel():
    with open("usrPswOriginal.txt","r+") as archivo:
        contenido = archivo.read()
        data = json.loads(contenido)

        print(data)
        # definimos los campos del excel
        userIds = [entry["userId"] for entry in data]
        userNames = [entry["userName"] for entry in data]
        userSurnames = [entry["userSurname"] for entry in data]
        passwords = [entry["password"] for entry in data]
        print(passwords)

        print("---------------")

        for i in passwords:
            i = hashPswd(i)
            print(i)

        print("---------------")
        print(passwords)
        #no se pq aqui no esta cambiado el array

        #relacionar la data
        df = pd.DataFrame({'userId':userIds, 'userName':userNames,'userSurnames':userSurnames, 'passwords':passwords})

        # Obtener el mes y año actual
        now = datetime.date.today()
        mes_anio = now.strftime("%m-%Y")

        # Crear el archivo Excel
        nombre_excel = f"ExamenPython-{mes_anio}.xlsx"
        df.to_excel(nombre_excel, index=False)

        print(f"Archivo Excel '{nombre_excel}' creado exitosamente.")



print("Creando anrchivo excel...")
crarExcel()

