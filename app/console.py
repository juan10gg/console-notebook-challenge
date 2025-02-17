# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
from datetime import datetime
class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code, tittle, text, importance):
        self.code = code
        self.tittle = tittle
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags = []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return "Date: " + str(self.creation_date) + "\n" + self.tittle + ": " + self.text



