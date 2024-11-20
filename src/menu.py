import os
import csv
import json
from file_reader import FileReader
from models import Estudiante, Materia, Inscripcion

class Menu:
    def __init__(self, db):
        self.db = db

    def display(self):
        while True:
            print("\nMenú Principal".center(50, "-"))
            print("1. Cargar archivo de inscripciones")
            print("2. Mostrar total de materias por estudiante")
            print("3. Filtrar estudiantes por materia")
            print("4. Exportar datos a JSON/CSV")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                archivo = input("Ingrese el nombre del archivo: ")
                if not os.path.exists(f"data/{archivo}.txt"):  # Verificación si el archivo existe
                    print(f"El archivo {archivo} no se encuentra en la carpeta 'data'.")
                else:
                    reader = FileReader(archivo, self.db)
                    reader.read_file()  # Llamar el método para cargar los datos
                    if reader.error_count > 0:
                        print(f"Se procesaron con errores {reader.error_count} líneas del archivo {archivo}.")
                    else:
                        print(f"Archivo {archivo} cargado correctamente sin errores.")
            elif opcion == "2":
                self.show_total_materias()
            elif opcion == "3":
                self.filter_estudiantes_by_materia()
            elif opcion == "4":
                self.export_data()
            elif opcion == "5":
                print("\nSaliendo del programa.".center(50, "-"))
                break
            else:
                print("\nOpción no válida. Intente de nuevo.\n".center(50, "-"))

    def show_total_materias(self):
        estudiantes = self.db.get_estudiantes()
        if not estudiantes:
            print("\nNo hay estudiantes registrados en la base de datos.\n".center(50, "-"))
            return
        
        print("\nListado de estudiantes y sus materias".center(50, "-"))
        for estudiante in estudiantes:
            print(f"\n{estudiante.nombre} ({estudiante.cedula}) está inscrito en {len(estudiante.materias)} materias.".ljust(50))
            print("-" * 50)
            print("Materias inscritas:")
            for materia in estudiante.materias:
                print(f"  {materia.nombre} ({materia.codigo})")
            print("-" * 50)

    def filter_estudiantes_by_materia(self):
        codigo_materia = input("Ingrese el código de la materia: ")
        estudiantes = self.db.get_estudiantes()
        found = False
        
        print("\nEstudiantes inscritos en la materia:".center(50, "-"))
        for estudiante in estudiantes:
            # Filtramos los estudiantes que están inscritos en esta materia
            if any(materia.codigo == codigo_materia for materia in estudiante.materias):
                if not found:
                    print(f"Materia:{codigo_materia}".center(50, "-"))
                    found = True
                print(f"{estudiante.nombre} ({estudiante.cedula})")
        
        if not found:
            print(f"\nNo hay estudiantes inscritos en la materia {codigo_materia}.\n".center(50, "-"))

    def export_data(self):
        format_option = input("Seleccione el formato para exportar (1: JSON, 2: CSV): ")

        estudiantes = self.db.get_estudiantes()
        if not estudiantes:
            print("\nNo hay estudiantes registrados para exportar.\n".center(50, "-"))
            return

        if format_option == "1":
            self.export_to_json(estudiantes)
        elif format_option == "2":
            self.export_to_csv(estudiantes)
        else:
            print("\nOpción no válida.\n".center(50, "-"))

    def export_to_json(self, estudiantes):
        data = []
        for estudiante in estudiantes:
            materias = [{"codigo": materia.codigo, "nombre": materia.nombre} for materia in estudiante.materias]
            data.append({"cedula": estudiante.cedula, "nombre": estudiante.nombre, "materias": materias})

        with open('estudiantes_exportados.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("\nDatos exportados a estudiantes_exportados.json".center(50, "-"))

    def export_to_csv(self, estudiantes):
        with open('estudiantes_exportados.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Cedula', 'Nombre', 'Materia'])
            for estudiante in estudiantes:
                for materia in estudiante.materias:
                    writer.writerow([estudiante.cedula, estudiante.nombre, materia.nombre])
        print("\nDatos exportados a estudiantes_exportados.csv".center(50, "-"))
