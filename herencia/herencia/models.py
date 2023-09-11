from django.db import models
from datetime import date


class Author (models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField()

    def __str__(self):
        resultado = f"{self.name} - {self.email}"
        return resultado


 




