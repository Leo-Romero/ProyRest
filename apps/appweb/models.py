from django.db import models

class Proveedor(models.Model):
    """
    Modelo de proveedores
    """
    nombre = models.CharField('Nombre', max_length=250, blank=False, null=False)
    direccion = models.CharField('Dirección', max_length=250, blank=False, null=False)
    cod_postal = models.CharField('C. Postal', max_length=10, blank=True, null=True)
    ciudad = models.CharField('Ciudad', max_length=50, blank=True, null=True)
    provincia = models.CharField('Provincia', max_length=50, blank=True, null=True)
    pais = models.CharField('País', max_length=50, blank=True, null=True)
    correo = models.EmailField('Email', max_length=254, blank=True, null=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

    def __str__(self):
        """
        Cadena que representa a la instancia particular
        """
        return f"{self.nombre} {self.ciudad}"

