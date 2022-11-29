from django.db import models
from django.contrib.auth.models import User

class Palavra(models.Model):
    palavra = models.CharField(max_length=5)

    def __str__(self):
        palavra = str(self.palavra)
        id = str(self.id)
        return id+"."+palavra

class PalavraUsuario(models.Model):
    palavra = models.ForeignKey(Palavra, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        palavra = str(self.palavra)
        usuario = str(self.usuario)
        data = str(self.data)
        return palavra+"-"+usuario+"-"+data