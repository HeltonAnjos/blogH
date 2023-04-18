from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from stdimage.models import StdImageField

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200, unique=True)
    created_on = models.DateField(auto_now_add=True)
    update_on = models.DateField(auto_now=True)
    summary = RichTextField(verbose_name='Resumo', null=True, blank=True)
    content = RichTextUploadingField(verbose_name='Conteúdo')
    cover_image = StdImageField('Imagem Capa', upload_to='static/images', variations={'thumbnail': {"width": 200, "height": 250, "crop": True}})
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE, related_name='blog_posts')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

def __str__(self):
    return self.title 
