from claseEmail import Email


if __name__ == "__main__":
    print("Ingrese datos")
    id = input(" ingrese id cuenta: ")
    dominio = input(" ingrese dominio: ")
    tipodom = input(" ingrese el tipo de dominio: ")
    contraseña = input(" ingrese la contraseña: ")
    unemail = Email(id, dominio, tipodom, contraseña)
    unemail.retornaEmail()
    unemail.getdominio()

    direccion = input(" ingrese direccion correo: ")
    mail = Email(0, 0, 0, 0)
    mail.crearcuenta(direccion)
    mail.retornaEmail()

    nombre = input("ingrese nombre:")
    email = input("ingrese email")
    print(f"Estimado {nombre} te enviaremos tus mensajes a la direccion {email}")
    contra = input(" ingrese la contraseña actual: ")
# mail.modificarcontrasenia(contra)
