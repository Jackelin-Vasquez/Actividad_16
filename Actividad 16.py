#Actividad 16
libros= []

class Libro:
    def __init__(self, titulo,autor,year):
        self.titulo= titulo
        self.autor=autor
        self.year=year

    def mostrar_informacion(self):
        print(f"---Información de libro---")
        print(f"Titulo:{self.titulo}\nAutor:{self.autor}\nAño:{self.year}")

def agregar_libro():
    libro_agregar= input("Ingrese titulo de libro:")
    if libro_agregar in libros:
        print("Libro ya registrado...")
    else:
        autor= input("Ingrese autor de libro:")
        year= int(input("Ingrese año de publicación:"))
        libro= Libro(libro_agregar,autor,year)
        libros.append(libro)
def mostrar_libros():
    print("---LIBROS INGRESADOS---")
    for i in libros:
        print(f"---Información libro {i+1}--")
        Libro.mostrar_informacion()
def eliminar_libro():
    libro_eliminar= input("Ingrese nombre de libro a eliminar:")
    if libro_eliminar in libros:
        libros.remove(libro_eliminar)



def menu_principal():
    print(f"---MENÚ PRINCIPAL---\n1.agregar libro.\n2.Mostrar la lista de libros.")
    print(f"3.Eliminar libro por titulo.\n4.Salir del programa")