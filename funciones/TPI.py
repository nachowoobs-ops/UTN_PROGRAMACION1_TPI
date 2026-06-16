import csv
import os
if not os.path.exists("archivo.csv"):
    cabecera = ["nombre","poblacion","superficie","continente"]
    with open("archivo.csv","w",newline="",encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo,fieldnames=cabecera)
        writer.writeheader()     
        writer.writerow({"nombre":"Argentina","poblacion":45376763,"superficie":2780400,"continente":"América"})
        writer.writerow({"nombre":"Australia","poblacion":27000000,"superficie":7741220,"continente":"Oceanía"})  
        writer.writerow({"nombre":"Brasil","poblacion":213993437,"superficie":8515767,"continente":"América"})  
        writer.writerow({"nombre":"Alemania","poblacion":83149300,"superficie":2780400,"continente":"Europa"}) 
        writer.writerow({"nombre":"Suiza","poblacion":9000000,"superficie":41291,"continente":"Europa"})                
print("El archivo.csv se ha creado correctamente. ")
#La primera linea se importa el csv para poder trabajar con las mismas, luego se importa os para trabajar con el sistema operativo,en este caso para verificar la existencia de un archivo.
#Luego la linea 3 verifica si el archivo existe, su salida es true si existe o false si no existe. Si el archivo no existe entra al if, si existe no entra para no sobrescribirlo.
#En la linea 5 tenemos la creacion del archivo csv que abarca hasta la linea 12.
#=====VALIDACIONES=====
def pedir_entero(mensaje):
    continuar_=True
    while continuar_:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("error, no puede ingresar numeros negativos. ")
            else:
                return numero
        except ValueError:
            print("error, debe ingresar un numero valido. ")
#=====CARGAR CSV=====
def cargar_csv(nombre_archivo):
    paises=[]
    try:
        with open(nombre_archivo,"r",encoding="utf-8")as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais={
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                    }
                paises.append(pais)
    except FileNotFoundError:
        print("Error, el archivo no se encontro. ")
    except ValueError:
        print("Hay un error de formato en el archivo CSV.  ")
    return paises
#Este bloque lee los datos del archivo.csv y los guarda en la lista vacia de paises[].
#=====GUARDAR CSV=====
def guardar_csv(nombre_archivo, paises):

    cabecera = ["nombre","poblacion","superficie","continente"]

    with open(nombre_archivo,"w",newline="",encoding="utf-8") as archivo:

        writer = csv.DictWriter(
            archivo,
            fieldnames=cabecera
        )

        writer.writeheader()

        for pais in paises:
            writer.writerow(pais)
#Aqui se guarda en el archivo.csv todos los paises que estan almacenados en la lista de paises[]
#=====MOSTRAR PAISES=====
def mostrar_paises(paises):
    if len(paises) == 0:
        print("No se encuentra ningun pais cargado.")
        return
    for pais in paises:
            print(f'''
nombre: {pais['nombre']}
poblacion: {pais['poblacion']}
superficie: {pais['superficie']} Km**2
continente: {pais['continente']}
''')
#======AGREGAR PAIS=====
def agregar_pais(paises):
    try:
        while True:
            nombre = input("ingrese el nombre del pais que desee agregar: ").capitalize().strip()
            encontrado = False
            if nombre.replace(" ","").isalpha():
                poblacion = pedir_entero("poblacion: ")
                superficie = pedir_entero("superficie: ")
                continente = input("ingrese el contiente: ").capitalize().strip()
                if continente.replace(" ","").isalpha():
                    break
                else:
                    print("Error, debe ingresar un continente correctamente. ")

            else:
                print("Error, ingrese el nombre del pais correctamente. ")
        pais ={
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        for country in paises:
            if country["nombre"] == nombre:
                print("Ese pais ya existe.")
                return  
        paises.append(pais)
        guardar_csv("archivo.csv", paises)
        print("Pais cargado correctamente. ")
    except Exception as e:
        print("Error, ha ingresado algo incorrecto.")
#=====ACTUALIZAR PAIS=====
def actualizar_pais(paises):
    try:
        nombre = input("Ingrese el nombre del pais que desea actualizar: ").capitalize()
        encontrado = False
        if nombre.replace(" ","").isalpha():
            for pais in paises:
                if pais ['nombre'] == nombre:
                    encontrado = True
                    print(f"Ingrese los nuevos datos de {nombre}:  ")
                    pais['poblacion']= pedir_entero("Nueva poblacion: ")
                    pais['superficie']= pedir_entero("Nueva superficie: ")
                    guardar_csv("archivo.csv", paises)
                    print("Datos actualizados correctamente! ")
                    print(paises)
                    return          
            if not encontrado:
                print("El pais que ingreso no fue encontrado. ")   
        else:
            print("Solo puede ingresar letras. ")
            return
    except Exception as e:
        print(f"Error, {e}")
#=====BUSCAR PAIS=====
def buscar_pais(paises):
    busqueda = input("Buscar país: ").capitalize().strip()
    if busqueda.replace(" ","").isalpha():
        encontrados = []
        for pais in paises:
            if pais["nombre"].capitalize().startswith(busqueda):
                encontrados.append(pais)
        print("Pais encontrado! ")
        mostrar_paises(encontrados)
        if len(encontrados) == 0:
            print("No se encontraron resultados")
#Para poder hacer la busqueda parcial o completa del pais usamos .startswith que sirve para hacer una busqueda de los elementos sin colocar el nombre completo del pais.
#Ej:Si Argentina se encuentra en la lista,el ingreso podria ser arg y la salida mostrara Argentina.
#=====FILTRAR CONTINENTE=====
def filtrar_continente(paises):
    continente = input("continente (Ingrese su nombre con el tilde correspondiente): ").capitalize().strip()
    if continente.replace(" ","").isalpha():
        filtrados = []
        for pais in paises:
            if pais['continente'] == continente:
                filtrados.append(pais)
        if len(filtrados) == 0:
            print(f"No se encuentran paises en {continente} o no ingreso el nombre del continente con tilde. ")
        else:
            mostrar_paises(filtrados)
#=====FILTRAR POBLACION=====
def filtrar_poblacion(paises):
    try:
        minima = input("Ingrese una poblacion mínima: ")
        if minima.isdigit():
            minima = int(minima)
            maxima = input("Ingrese una poblacion máxima: ")
            if maxima.isdigit():
                maxima = int(maxima)
                if minima > maxima:
                    print("Rango inválido.")
                    return
                filtrados = []
                for pais in paises:
                    if minima <= pais['poblacion'] <= maxima:
                        filtrados.append(pais)
                if len(filtrados) == 0:
                    print("No se encuentran paises. ")
                else:
                    mostrar_paises(filtrados)
            else:
                print("Solo puede ingrsar digitos. ")
        else:
                print("Solo puede ingrsar digitos. ")
    except Exception as e:
        print(f"error,{e} ")
#=====FILTRAR SUPERFICIE=====
def filtrar_superficie(paises):
    minimo = input("Superficie mínima: ")
    if minimo.isdigit():
        minimo = int(minimo)
        maximo = input("Superficie máxima: ")
        if maximo.isdigit():
            maximo = int(maximo)
            if minimo > maximo:
                print("Rango inválido. ")
                return
            filtrados=[]
            for pais in paises:
                if minimo <= pais["superficie"] <= maximo:
                    filtrados.append(pais)
            if len(filtrados) == 0:
                print("No se encuentran paises! ")
            else:
                mostrar_paises(filtrados)
        else:
            print("Solo puede ingresar números.")
    else:
        print("Solo puede ingresar números.")
#=====ORDENAR PAISES=====
def ordenar_paises(paises):
    try:
        print('''
    1)_Ordenar por nombre:
    2)_Ordenar por poblacion:
    3)_Ordenar por superficie ascendente:
    4)_Ordenar por superficie descendente:
    ''')
        opcion = input("Ingrese lo que desea hacer: ").strip()
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                ordenados=sorted(paises, key=lambda x: x['nombre'])
            elif opcion == 2:
                ordenados = sorted(paises, key=lambda x: x['poblacion'])
            elif opcion == 3:
                ordenados = sorted(paises, key=lambda x: x['superficie'])
            elif opcion == 4:
                ordenados = sorted(paises, key=lambda x: x['superficie'],reverse=True)
            else:
                print("Lo que ingreso es incorrecto. ")
                return
            print("Paises ordenados correctamente!")
            mostrar_paises(ordenados)
    except ValueError:
        print("Error, solo puede ingresar digitos")
    except Exception as e:
        print(f"Error, {e}. ")
#La funcion sorted() devuelve una nueva lista ordenada, (key=lambda x: x['nombre']) esto indica que la forma de ordenamiento sera de la a-z.
#En el caso que fuese 'poblacion' y no 'nombre', esta misma se ordenara de menor a mayor poblacion. Si queremos que sea al reves le agregamos el reverse = true al final de la linea.  
#=====ESTADISTICAS=====
def mostrar_estadis(paises):
    if len(paises)== 0:
        print("No se encuentran paises cargados!")
        return
    mayor = max(paises, key=lambda x: x['poblacion'])
    menor = min(paises, key=lambda x: x['poblacion'])
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}
    for pais in paises:
        suma_poblacion += pais['poblacion']
        suma_superficie += pais['superficie']
        continente = pais['continente']
        if continente in continentes:
            continentes[continente] += 1
        else: continentes[continente] = 1
    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)
    print("-----ESTADÍSTICAS-----")
    print()
    print(f'''
Pais con mayor poblacion:
{mayor['nombre']} - {mayor['poblacion']}
Pais con menor poblacion:
{menor['nombre']} - {menor['poblacion']}
Promedio de la poblacion: 
{promedio_poblacion}
Promedio de la superficie:
{promedio_superficie}
''')
    print("======Cantidad de paises por continente=====: ")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")    
#Primero verifica que la lista paises[] no se encuentre vacia, luego busca el pais con mayor y menor poblacion, luego se encuentran dos acumuladores para la poblacion total y
#la superficie total, luego el diccionario de continentes que comienza vacio, si un continente se encuentra en el diccionario se suma al contador sino lo crea con valor 1.
def salir():
    pass

        


    


            

            

            




        
