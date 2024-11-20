from models import Estudiante, Materia, Inscripcion

class FileReader:
    def __init__(self, archivo, db):
        self.archivo = archivo
        self.db = db
        self.error_count = 0  # Contador de líneas con errores
        self.correct_count = 0  # Contador de líneas procesadas correctamente

    def read_file(self):
        # Verifica que el archivo existe
        archivo_ruta = f"data/{self.archivo}.txt"
        print(f"Leyendo archivo: {archivo_ruta}")
        
        try:
            with open(archivo_ruta, 'r', encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    # Intentar leer cada línea y manejar errores si el formato no es correcto
                    try:
                        # Se asume que el archivo tiene el formato: cedula, nombre, codigo_materia, nombre_materia
                        parts = line.strip().split(",")
                        
                        if len(parts) != 4:
                            raise ValueError(f"La línea {line_number} tiene un formato incorrecto: '{line.strip()}'")
                        
                        cedula, nombre, codigo_materia, nombre_materia = parts

                        # Validar que la cédula no esté vacía
                        if not cedula:
                            print(f"Error en la línea {line_number}: La cédula está vacía.")
                            self.error_count += 1
                            continue  # Saltar esta línea si la cédula está vacía

                        # Validar que tanto el código como el nombre de la materia estén presentes
                        if not codigo_materia or not nombre_materia:
                            raise ValueError(f"En la línea {line_number}, falta el código o el nombre de la materia.")

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
                        if not self.db.is_inscripcion_existente(cedula, codigo_materia):
                            # Si no existe, inscribir al estudiante en la materia
                            inscripcion = Inscripcion(estudiante, materia)
                            self.db.insert_inscripcion(inscripcion)
                            estudiante.inscribir_materia(materia, self.db.get_lista_inscripciones(cedula))  # Añadir la materia al estudiantes
                            print(f"{estudiante.nombre} inscrito en {materia.nombre} correctamente.")
                        else:
                            print(f"El estudiante {nombre} ya está inscrito en la materia {materia.nombre}.")
                    
                    except ValueError as e:
                        # Informar sobre cualquier error encontrado en la línea específica
                        print(f"Error en el archivo en la línea {line_number}: {e}")
                        self.error_count += 1
                    
                    except Exception as e:
                        # Capturar cualquier otro tipo de error y continuar procesando
                        print(f"Error inesperado en la línea {line_number}: {e}")
                        self.error_count += 1
                        continue  # Ignorar esta línea y pasar a la siguiente

        except FileNotFoundError:
            print(f"El archivo {archivo_ruta} no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error al intentar abrir el archivo: {e}")
            
        print("".center(50, "-"))
