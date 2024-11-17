from models import Estudiante, Materia, Inscripcion

class FileReader:
    def __init__(self, archivo, db):
        self.archivo = archivo
        self.db = db

    def read_file(self):
        # Verifica que el archivo existe
        with open(f"data/{self.archivo}", 'r', encoding="utf-8") as file:
            for line in file:
                # Se asume que el archivo tiene el formato: cedula, nombre, codigo_materia, nombre_materia
                cedula, nombre, codigo_materia, nombre_materia = line.strip().split(",")
                
                # Verificar si el estudiante ya existe
                estudiante = self.db.get_estudiante_by_cedula(cedula)
                if not estudiante:
                    # Si no existe, creamos el estudiante
                    estudiante = Estudiante(cedula, nombre)
                    self.db.insert_estudiante(estudiante)
                    print(f"Estudiante {nombre} ({cedula}) agregado a la base de datos.")
                else:
                    print(f"El estudiante con cédula {cedula} ya está registrado.")
                
                # Verificar si la materia ya existe
                materia = self.db.get_materia_by_codigo(codigo_materia)
                if not materia:
                    # Si la materia no existe, la creamos
                    materia = Materia(codigo_materia, nombre_materia)
                    self.db.insert_materia(materia)
                    print(f"Materia {nombre_materia} ({codigo_materia}) agregada a la base de datos.")
                
                # Verificar si el estudiante ya está inscrito en la materia
                if materia in estudiante.materias:
                    print(f"El estudiante {nombre} ya está inscrito en la materia {materia.nombre}.")
                    continue
                
                # Inscribir al estudiante en la materia
                inscripcion = Inscripcion(estudiante, materia)
                self.db.insert_inscripcion(inscripcion)
                estudiante.inscribir_materia(materia)  # Añadir la materia al estudiante
                print(f"{estudiante.nombre} inscrito en {materia.nombre} correctamente.")
