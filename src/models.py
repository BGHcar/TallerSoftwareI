class Estudiante:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = []  # Lista para almacenar las materias inscritas

    def inscribir_materia(self, materia, lista_materias):
        # lista_materias es la lista de objetos Materia que devuelve get_lista_inscripciones
        
        # Verifica si la materia ya está en la lista de materias del estudiante
        if any(m.codigo == materia.codigo for m in lista_materias):
            print(f"{self.nombre} ya está inscrito en la materia {materia.nombre}.")
            return
            
        # Si no está inscrito, agrega la materia a la lista del estudiante
        self.materias.append(materia)
        print(f"{self.nombre} se ha inscrito en la materia {materia.nombre}.")

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
        return f"{self.estudiante.nombre} está inscrito en {self.materia.nombre}"