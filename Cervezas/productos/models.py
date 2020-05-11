from django.db import models


class Chela(models.Model):
    marca = models.CharField(max_length=60)
    alcohol = models.DecimalField(max_digits=4, decimal_places=2)
    mililitros = models.IntegerField()
    pais = models.CharField(max_length=100, blank=True, null=True)  # blank->django ; null->db
    artesanal = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)

    # mostrar registros por marca de cerveza en el panel de admin django
    def __str__(self):
        return self.marca
