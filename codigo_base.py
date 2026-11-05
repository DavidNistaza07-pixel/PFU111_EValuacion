import csv
import os
import re

ARCHIVO = "prestamos.csv"
# --------------------------------
# 1. CARGAR LOS PRESTAMOS
# --------------------------------

def cargar_prestamos():
    prestamos = []

    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)

                for fila in lector:
                    prestamos.append(fila)

        except (OSError, csv.Error) as error:
            print("Error al cargar los prestamos:", error)

    return prestamos


# --------------------------------
# 2. GUARDAR LOS PRESTAMOS
# --------------------------------

def guardar_prestamos(prestamos):
    campos = [
        "codigo",
        "nombre",
        "material",
        "dias"
    ]

    try:
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(prestamos)

        return True

    except OSError as error:
        print("Error al guardar los datos:", error)
        return False
# --------------------------------
# 3. VALIDAR CODIGO
# --------------------------------

def validar_codigo(codigo):
    patron = r"^(SIS|EST)-\d{3,6}$"

    return re.fullmatch(patron, codigo) is not None

# --------------------------------
# 4. REGISTRAR PRESTAMO
# --------------------------------

def registrar_prestamo(prestamos):

    print("\n--- REGISTRAR PRESTAMO ---")

    codigo = input("Codigo del estudiante: ").strip().upper()

    if not validar_codigo(codigo):
        print("Error: codigo invalido.")
        print("Ejemplo: SIS-123456")
        return

    nombre = input("Nombre del estudiante: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacio.")
        return

    material = input("Titulo del material: ").strip()

    if material == "":
        print("Error: el material no puede estar vacio.")
        return

    # Validar dias
    try:
        dias = int(input("Cantidad de dias del prestamo: "))

        if dias < 1 or dias > 30:
            print("Error: los dias deben estar entre 1 y 30.")
            return

    except ValueError:
        print("Error: debes ingresar un numero entero.")
        return

    # Evitar prestamos duplicados
    for prestamo in prestamos:

        mismo_codigo = prestamo["codigo"] == codigo

        mismo_material = (
            prestamo["material"].strip().lower()
            == material.lower()
        )

        if mismo_codigo and mismo_material:
            print("Error: este prestamo ya esta registrado.")
            return

    # Crear registro
    nuevo_prestamo = {
        "codigo": codigo,
        "nombre": nombre,
        "material": material,
        "dias": str(dias)
    }

    prestamos.append(nuevo_prestamo)

    # Guardar en archivo
    if guardar_prestamos(prestamos):
        print("\nPrestamo registrado correctamente.")
    else:
        prestamos.pop()
        print("No se pudo guardar el prestamo.")

