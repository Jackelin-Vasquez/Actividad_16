#Actividad 16
libros= []

class Libro:
    def __init__(self, titulo,autor,year):
        self.titulo= titulo
        self.autor=autor
        self.year=year

    def mostrar_informacion(self):


def agregar_libro():
    libro_agregar= input("Ingrese titulo de libro:")
    autor= input("Ingrese autor de libro:")
    year= int(input("Ingrese año de publicación:"))
    libros.append(Libro)

def menu_principal():
    print(f"---MENÚ PRINCIPAL---\n1.agregar libro.\n2.Mostrar la lista de libros.")
    print(f"3.Eliminar libro por titulo.\n4.Salir del programa")