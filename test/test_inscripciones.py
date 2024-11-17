import pytest
from src.database import Database
from src.models import Estudiante, Materia, Inscripcion

def test_insert_estudiante():
    db = Database()
    estudiante = Estudiante("12345", "Juan Perez")
    db.insert_estudiante(estudiante)
    estudiantes = db.get_estudiantes()
    assert len(estudiantes) == 1
    assert estudiantes[0].cedula == "12345"

def test_insert_materia():
    db = Database()
    materia = Materia("CS101", "Introducción a la programación")
    db.insert_materia(materia)
    # Prueba similar a la de estudiantes, verificando si la materia se ha insertado correctamente
