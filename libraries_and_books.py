#Hacer un script que configure un nuevo JSON de nombre libraries-and-books.json que contenga una lista de objetos library en el que cada uno
# contiene la lista de objetos libro que le pertenecen en los que habrá un campo userId con el usuario correspondiente que tiene el libro prestado.
# Pasar esa estructura a un dataframe de pandas que lo mande a un excel cuyo nombre sea la fecha de hoy + libros-prestados (eemploj: 20-mayo-libros-prestados.xlsx)
import json
import pandas as pd
import datetime


with open("usrPswOriginal.txt", "r+") as archivo:
    contenido = archivo.read()
    data = json.loads(contenido)
    print(data)
    for usuario in data:
         libros = usuario.get("books", [])
         print(libros)

         for libro in libros:
             print(libro)

             # definimos los campos del excel
             bookIds = [entry["bookId"] for entry in libro]
             bookTitles = [entry["bookTitle"] for entry in libro]
             bookEditorials = [entry["bookEditorial"] for entry in libro]
             bookPublications = [entry["bookPublication"] for entry in libro]
             libraryIds = [entry["libraryId"] for entry in libro]

             # relacionar la data
             df = pd.DataFrame(
                 {'bookId': bookIds, 'bookTitle': bookTitles, 'bookEditorial': bookEditorials, 'bookPublication': bookPublications, 'libraryId': libraryIds})

             # Obtener el mes y año actual
             now = datetime.date.today()
             mes_anio = now.strftime("%m-%Y")

             # Crear el archivo Excel
             nombre_excel = f"{mes_anio}-libros-prestados.xlsx"
             df.to_excel(nombre_excel, index=False)

             print(f"Archivo Excel '{nombre_excel}' creado exitosamente.")


