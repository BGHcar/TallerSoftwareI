import sqlite3
from models import Estudiante, Materia, Inscripcion

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('inscripciones.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Crear tablas de estudiantes, materias e inscripciones
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
            cedula TEXT PRIMARY KEY,
            nombre TEXT
        );''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS materias (
            codigo TEXT PRIMARY KEY,
            nombre TEXT
        );''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inscripciones (
            cedula_estudiante TEXT,
            codigo_materia TEXT,
            FOREIGN KEY(cedula_estudiante) REFERENCES estudiantes(cedula),
            FOREIGN KEY(codigo_materia) REFERENCES materias(codigo)
        );''')
        self.conn.commit()

    def insert_estudiante(self, estudiante):
        # Insertar un estudiante
        self.cursor.execute("INSERT OR IGNORE INTO estudiantes (cedula, nombre) VALUES (?, ?)", 
                            (estudiante.cedula, estudiante.nombre))
        self.conn.commit()

    def insert_materia(self, materia):
        # Insertar una materia
        self.cursor.execute("INSERT OR IGNORE INTO materias (codigo, nombre) VALUES (?, ?)", 
                            (materia.codigo, materia.nombre))
        self.conn.commit()

    def insert_inscripcion(self, inscripcion):
        # Verificar si la inscripción ya existe
        if self.is_inscripcion_existente(inscripcion.estudiante.cedula, inscripcion.materia.codigo):
            print(f"El estudiante con cédula {inscripcion.estudiante.cedula} ya está inscrito en la materia {inscripcion.materia.codigo}.")
            return  # O puedes lanzar una excepción, dependiendo de cómo quieras manejarlo
        
        # Si la inscripción no existe, insertamos
        self.cursor.execute("INSERT INTO inscripciones (cedula_estudiante, codigo_materia) VALUES (?, ?)", 
                            (inscripcion.estudiante.cedula, inscripcion.materia.codigo))
        self.conn.commit()
        print(f"Inscripción exitosa para el estudiante {inscripcion.estudiante.cedula} en la materia {inscripcion.materia.codigo}.")


    def get_estudiantes(self):
        # Obtener todos los estudiantes
        self.cursor.execute("SELECT * FROM estudiantes")
        rows = self.cursor.fetchall()
        estudiantes = []
        for row in rows:
            estudiante = Estudiante(row[0], row[1])
            estudiante.materias = self.get_materias_estudiante(estudiante.cedula)
            estudiantes.append(estudiante)
        return estudiantes

    def get_materias_estudiante(self, cedula):
        # Obtener las materias de un estudiante
        self.cursor.execute('''SELECT m.codigo, m.nombre
                               FROM materias m
                               JOIN inscripciones i ON m.codigo = i.codigo_materia
                               WHERE i.cedula_estudiante = ?''', (cedula,))
        rows = self.cursor.fetchall()
        return [Materia(row[0], row[1]) for row in rows]

    def get_estudiante_by_cedula(self, cedula):
        # Método para obtener un estudiante por su cédula
        self.cursor.execute("SELECT * FROM estudiantes WHERE cedula = ?", (cedula,))
        row = self.cursor.fetchone()
        if row:
            return Estudiante(row[0], row[1])
        return None

    def get_materia_by_codigo(self, codigo):
        # Método para obtener una materia por su código
        self.cursor.execute("SELECT * FROM materias WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            return Materia(row[0], row[1])
        return None
    
    def is_inscripcion_existente(self, cedula_estudiante, codigo_materia):
        try:
            # Consulta SQL para verificar si la inscripción ya existe
            query = """
            SELECT 1
            FROM inscripciones
            WHERE cedula_estudiante = ? AND codigo_materia = ?
            LIMIT 1
            """
            self.cursor.execute(query, (cedula_estudiante, codigo_materia))
            result = self.cursor.fetchone()

            # Devolver True si existe un registro, False si no
            return result is not None
        except sqlite3.Error as e:
            print(f"Error al verificar inscripción: {e}")
            return False


    def get_lista_inscripciones(self, cedula):
        # Obtener todas las inscripciones de un estudiante dado su cédula
        self.cursor.execute('''SELECT m.codigo, m.nombre
                               FROM inscripciones i
                               JOIN materias m ON i.codigo_materia = m.codigo
                               WHERE i.cedula_estudiante = ?''', (cedula,))
        rows = self.cursor.fetchall()
        # Crear una lista de objetos Materia para las materias en las que el estudiante está inscrito
        return [Materia(row[0], row[1]) for row in rows]
