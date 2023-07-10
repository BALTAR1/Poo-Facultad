from ManejaHelados import manejadorHelado
from ManejaSabores import manejadorSabor
from ClaseHelado import helado


if __name__ == "__main__":
    manejaSabor = manejadorSabor()
    manejaSabor.cargarSabores()
    manejaHelados = manejadorHelado()

while True:
    print("==Menu de opciones==")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        peso = int(input("\nIngrese el peso del helado: "))
        precio = float(input("Ingrese el precio del helado: "))
        sabores = []
        while True:
            idSabores = input("Ingrese los id de los sabores separados por comas: ")
            idSabores = idSabores.split(",")
            manejaSabor.obtenerSabor(idSabores)
            helado = helado(peso, precio, sabores)
            manejaHelados.agregarHelado(helado)
    elif opcion == "2":
        helados = manejaHelados.obtenerHelados()
        for helado in helados:
            print("Peso:", helado.getPeso())
            print("Precio:", helado.getPrecio())
            print("Sabores: ")
            for sabor in helado.getSabores():
                print(sabor)
    elif opcion == "3":
        break
    else:
        print("Opción inválida")
