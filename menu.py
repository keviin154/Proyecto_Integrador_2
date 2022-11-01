import controlador

while True:
    print("\n+-------------------------------------------+")
    print("|         DISQUERÍA MUSICAL         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - ALTA / BAJA / MODIFICACION DE UN ÁLBUM")
    print("2 - LISTADO DE ÁLBUMES POR ARTISTAS")
    print("3 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL")
    print("4 - BÚSQUEDA POR NOMBRE")
    print("5 - INSERTAR INTERPRETE")
    print("0 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print("1 - ALTA DE UN ÁLBUM")
        print("2 - BAJA DE UN ÁLBUM")
        print("3 - MODIFICACION DE UN ÁLBUM")
        print("0 - SALIR")
        opcion_2 = int(input("Ingrese su opción: "))
        if opcion_2 == 1:
            controlador.InsertarAlbum()
        elif opcion_2 == 2:
            controlador.EliminarAlbumes()
        elif opcion_2 == 3:
            None
        elif opcion_2 == 0:
            Break
        else:
            print("¡Opción incorrecta!")
    if opcion == 2:
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 3:
        controlador.ListarAlbumesPorGenero()
    elif opcion == 4:
        print("1 - BUSQUEDA DE UN ÁLBUM")
        print("2 - BUSQUEDA DE UN TEMA")
        print("3 - BUSQUEDA DE UN INTERPRETE")
        print("0 - SALIR")
        opcion_3 = int(input("Ingrese su opción: "))
        if opcion_3 == 1:
            controlador.BuscarAlbum()
        elif opcion_3 == 2:
            controlador.BuscarTema()
        elif opcion_3 == 3:
            controlador.BuscarInterprete()
        elif opcion_3 == 0:
            Break
        else:
            print("¡Opción incorrecta!")
    if opcion == 5:
        controlador.InsertarInterprete()
    elif opcion == 0:
        break
    else:
        print("¡Opción incorrecta!")
