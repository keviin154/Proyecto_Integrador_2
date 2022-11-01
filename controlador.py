import modelo

def ListarAlbumesPorArtistas():
    con = modelo.Conectar()
    listado = con.ListarAlbumes()
    print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
    input("Presione ENTER para continuar")

def ListarAlbumesPorGenero():
    con = modelo.Conectar()
    listado = con.ListarPorGenero()
    print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
    input("Presione ENTER para continuar")
    
def InsertarInterprete():
    
    con = modelo.Conectar()
    
    id_interprete = input("Ingrese el id del interprete: ")

    nombre = input("Ingrese el nombre del interprete: ")

    apellido = input("\nIngrese el apellido del interprete: ")

    nacionalidad = input("\nIngrese la nacionalidad del interprete: ")

    foto = input("Ingrese foto del interprete")

    nuevoInterprete = modelo.Interprete(id_interprete,nombre,apellido,nacionalidad,foto)
    con.InsertarInterprete(nuevoInterprete)
    input("Presione ENTER para continuar")


def InsertarAlbum():
    cod_album = int(input("\nIngrese el código del nuevo Álbum: "))
    nombre = input("Ingrese el nombre del álbum: ")

    con = modelo.Conectar()

    print("\nIntérpretes Disponibles:")

    for i in con.ListarInterprete():
        print(i)
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    
    print("\nGénero")
    for g in con.ListarGenero():
        print(g)
    id_genero = int(input("\nIngrese el ID del Género: "))

    cant_temas = int(input("\nIngrese la cantidad de temas: "))

    print("\nDiscográfica")
    for d in con.ListarDiscografica():
        print(d)
    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\nFormato")
    for f in con.ListarFormato():
        print(f)
        
    id_formato = int(input("\nIngrese el ID del formato: "))
    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
    precio = float(input("\nIngrese el precio: "))
    cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    con.InsertarAlbum(nuevoAlbum)
    input("Presione ENTER para continuar")

   

def EliminarAlbumes():
    con = modelo.Conectar()
    listado = con.ListarPorGenero()
    print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
    cod_album = input("Ingrese el codigo del album a eliminar: ")
    con.EliminarAlbumes(cod_album)
    con.conexion.close()
    input("Presione ENTER para continuar")
    
    
def BuscarAlbum():
    nombre = "%" + (input("ingrese el nombre del album: ")) + "%",

    con = modelo.Conectar()

    nuevoAlbum = con.BuscarAlbum(nombre)
    print("Los resultados son: ")
    for album in nuevoAlbum:
        print("\n| COD. ÁLBUM   |          NOMBRE DEL ALBUM              |")
        print("\t" + str(album[1]),"\t" + str(album[2]))

    input("Presione ENTER para continuar")


def BuscarTema():
    titulo = "%" + (input("ingrese el nombre del tema: ")) + "%",

    con = modelo.Conectar()

    nuevoAlbum = con.BuscarTema(titulo)
    print("Los resultados son: ")
    for Tema in nuevoAlbum:
        print("\n| NOMBRE DEL TEMA   |          NOMBRE DEL COMPOSITOR            |")
        print(str(Tema[1]),"\t""\t" + str(Tema[3]))
    

    input("Presione ENTER para continuar")




def BuscarInterprete():
    nombre = "%" + (input("ingrese el nombre del interprete: ")) + "%",

    con = modelo.Conectar()

    nuevoAlbum = con.BuscarInterprete(nombre)
    print("Los resultados son: ")
    for Interprete in nuevoAlbum:
        print("\n| NOMBRE   |          APELLIDO              |")
        print(str(Interprete[1]),"\t""\t" + str(Interprete[2]))
    

    input("Presione ENTER para continuar")
