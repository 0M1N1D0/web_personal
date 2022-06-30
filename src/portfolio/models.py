""" Modelos de la app portfolio: """

from django.db import models


# Create your models here.
class Project(models.Model):
    """ modelo Project """
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    # upload_to = 'projects': las imagenes subidas por el usuario se guardarán
    # en el directorio projects dentro de la carpeta media
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    link = models.URLField(verbose_name='Dirección Web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta: # pylint: disable=too-few-public-methods
        """ Metadatos del modelo Project """
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        # -created: el guion es para ordenar del más nuevo
        # al más antiguo
        ordering = ['-created']

    def __str__(self): # pylint: disable=invalid-str-returned
        return self.title
