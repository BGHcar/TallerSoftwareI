class Estudiante:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = []  # Lista para almacenar las materias inscritas

    def inscribir_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)
            print(f"{self.nombre} se ha inscrito en la materia {materia.nombre}.")
        else:
            print(f"{self.nombre} ya está inscrito en la materia {materia.nombre}.")


class Materia:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Inscripcion:
    def __init__(self, estudiante, materia):
        self.estudiante = estudiante
        self.materia = materia

    def __str__(self):
        return f"{self.estudiante} está inscrito en {self.materia}"
