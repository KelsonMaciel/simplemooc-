from django.db import models
from django.conf import settings
from django.utils import  timezone

from taggit.managers import TaggableManager
# Create your models here.

class Thread(models.Model):
    """Model definition for Thread."""

    title = models.CharField('Título', max_length=100)
    body = models.TextField('Mensagem')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='threads'
    )
    view = models.IntegerField('Visualizações', blank=True, default=0)
    answers = models.IntegerField('Respostas', blank=True, default=0)
    
    tags = TaggableManager()

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modifield = models.DateTimeField('Modificado em', auto_now=True)

    # TODO: Define fields here
    def __str__(self):
        return self.title
         

    class Meta:
        """Meta definition for Tópico."""
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-modifield']
         

class Reply(models.Model):
    """Model definition for Respostas."""
    thread = models.ForeignKey(Thread, verbose_name='Tópico', related_name='replies')
    reply  = models.TextField('Resposta')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Autor', related_name='replies')
    correct = models.BooleanField('Correta ?', blank=True, default=False)
    
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modifield = models.DateTimeField('Modificado em', auto_now=True)

    
    # TODO: Define fields here
    def __str__(self):
        return self.reply[:100]

    class Meta:
        """Meta definition for Respostas."""

        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering =['-correct','created'] 
