from django.db import models


class Palavra(models.Model):
    palavra = models.CharField(max_length=5)

    def __str__(self):
        palavra = str(self.palavra)
        id = str(self.id)
        return id+"."+palavra