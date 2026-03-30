
def buscar_estudiantes(students,name):
    """Busca un producto por nombre (sin importar mayúsculas) y retorna el dict."""
    for student in students :
        if student["name"] == name:
            print("estudiante encotrado")
            return student
    return None

