Sistema de Gestión de Biblioteca:
Integrantes
- Fernando Yeray Medinaceli Andrade
- David Abraham Apaza Nistaza
- Benjamin Mateo Magueno Cano





1. Descripción del proyecto

El Sistema de Gestión de Biblioteca es un programa desarrollado en Python que permite administrar los préstamos de materiales bibliográficos de una institución educativa.

El sistema busca mejorar el registro de préstamos, evitando datos incompletos, errores de ingreso y registros duplicados.

2. Problema identificado

La institución educativa presenta dificultades en la administración de préstamos de biblioteca, como registros incompletos, datos inconsistentes, fechas incorrectas y préstamos duplicados.

Estas dificultades afectan el control de los materiales y la organización de la información.

3. Objetivo

Desarrollar un prototipo de sistema de gestión de préstamos que permita registrar, consultar, validar y almacenar la información de manera organizada.

4. Funcionalidades

- Registro de préstamos de biblioteca.
- Consulta de préstamos registrados.
- Validación del código del estudiante.
- Validación del nombre del estudiante.
- Validación del título del material.
- Validación de la cantidad de días del préstamo.
- Control de préstamos duplicados.
- Manejo de errores mediante excepciones.
- Almacenamiento de información en archivos CSV.
- Recuperación de registros guardados.
- Menú interactivo en consola.

5. Tecnologías utilizadas

- Python: Desarrollo del programa.
- CSV: Almacenamiento y recuperación de información.
- Git: Control de versiones.
- GitHub: Publicación y administración del repositorio.
- Visual Studio Code: Entorno de desarrollo.

6. Estructura del proyecto

PFU111_Evaluacion/
│
├── main.py
├── prestamos.csv
├── README.md
└── .git/

7. Instalación y ejecución

Requisitos

- Python instalado.
- Visual Studio Code.
- Git instalado.

Pasos para ejecutar

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir la terminal.
4. Ejecutar el siguiente comando:

python main.py

5. Seleccionar una opción del menú principal.

8. Menú principal

El sistema presenta las siguientes opciones:

1. Registrar nuevo préstamo.
2. Consultar préstamos.
3. Salir.

9. Validaciones

El programa realiza las siguientes validaciones:

- Verifica que el código del estudiante tenga un formato válido.
- Evita registrar nombres vacíos.
- Evita registrar títulos de materiales vacíos.
- Comprueba que los días del préstamo sean números enteros.
- Permite registrar préstamos entre 1 y 30 días.
- Evita registrar el mismo material para el mismo estudiante más de una vez.
- Maneja errores de ingreso de datos.

10. Persistencia de datos

Los préstamos se almacenan en el archivo "prestamos.csv".

El sistema permite recuperar los registros guardados cuando se ejecuta nuevamente el programa, evitando la pérdida de información.

11. Control de versiones

El proyecto utiliza Git para registrar los cambios realizados durante el desarrollo.

GitHub permite publicar el repositorio y compartir el código fuente para su revisión.

12. Conclusión

El proyecto permite desarrollar un prototipo de gestión de préstamos de biblioteca utilizando Python.

Mediante funciones, estructuras de datos, validaciones y archivos CSV, se busca mejorar la organización de los registros y facilitar la administración de los préstamos.

Además, el uso de Git y GitHub permite mantener un control de versiones y compartir el proyecto.
