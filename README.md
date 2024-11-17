# Taller Diseño e Implementación de Software I

## Descripción
Este proyecto es un sistema de gestión de inscripciones universitarias. Permite gestionar las inscripciones de los estudiantes a diversas materias. El sistema cuenta con las siguientes funcionalidades:

- Cargar inscripciones desde un archivo de texto.
- Mostrar el total de materias por estudiante.
- Filtrar estudiantes por materia.
- Exportar los datos a formatos JSON o CSV.
- Guardar la información en una base de datos SQLite.

## Requisitos
Antes de ejecutar el proyecto, debes tener instalados los siguientes requisitos:

- [Python 3.x](https://www.python.org/downloads/) - Un lenguaje de programación utilizado para el desarrollo del sistema.
- [SQLite](https://www.sqlite.org/) - Base de datos utilizada para almacenar los registros de estudiantes y materias.

## Instalación

1. **Clonar el repositorio**

   Primero, clona el repositorio desde GitHub:

   ```bash
   git clone https://github.com/BGHcar/TallerSoftwareI.git
   ```

2. **Instalar dependencias**

   Una vez clonado el proyecto, navega al directorio del proyecto y crea un entorno virtual para instalar las dependencias necesarias. Abre una terminal o línea de comandos y ejecuta:

   ```bash
   cd Taller_Diseno_Implementacion
   python -m venv env  # Crear entorno virtual
   .\env\Scripts\activate  # Activar entorno virtual en Windows
   ```

   Para sistemas basados en Unix (Linux/macOS), usa:

   ```bash
   source env/bin/activate  # Activar entorno virtual
   ```

   Luego, instala las dependencias necesarias utilizando `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Base de datos**

   El sistema utiliza una base de datos SQLite para almacenar los registros. Asegúrate de que el archivo de la base de datos (`database.db`) esté presente en el directorio del proyecto o el sistema lo creará automáticamente al ejecutar el código por primera vez.

## Uso

1. **Iniciar el programa**

   Para iniciar el programa, asegúrate de que el entorno virtual esté activado y ejecuta el siguiente comando:

   ```bash
   python src/main.py
   ```

2. **Menú del programa**

   Al ejecutar el programa, se mostrará el siguiente menú interactivo:

   ```
   Menú Principal------------------
   1. Cargar archivo de inscripciones
   2. Mostrar total de materias por estudiante
   3. Filtrar estudiantes por materia
   4. Exportar datos a JSON/CSV
   5. Salir
   ```

   Para seleccionar una opción, ingresa el número correspondiente y presiona `Enter`.