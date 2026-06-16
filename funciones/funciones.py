from TPI import *
def main ():
    paises = cargar_csv('archivo.csv')
    while True:
        print('''
-------MENÚ-------
1. Mostrar países
2. Agregar país
3. Actualizar país
4. Buscar país
5. Filtrar por continente
6. Filtrar por población
7. Filtrar por superficie
8. Ordenar países
9. Mostrar estadísticas
10. Salir
''')
        option = input("Ingrese lo que decida hacer (1-10): ")
        if option.isdigit():
            option = int(option)
            match option:
                case 1:
                    mostrar_paises(paises)
                case 2:
                    agregar_pais(paises)
                case 3:
                    actualizar_pais(paises)
                case 4:
                    buscar_pais(paises)
                case 5:
                    filtrar_continente(paises)
                case 6:
                    filtrar_poblacion(paises)
                case 7:
                    filtrar_superficie(paises)
                case 8:
                    ordenar_paises(paises)
                case 9:
                    mostrar_estadis(paises)
                case 10:
                    print("Salio del sistema correctamente!")
                    break
                case _:
                    print("Opción inválida. Debe ingresar un número del 1 al 10.")
        else:
            print("Lo que ingreso no es un digito. ")
main()




    