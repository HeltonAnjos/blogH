from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os


class Categoria(models.Model):
    name_cat = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.name_cat


class Post(models.Model):
    title_post = models.CharField(max_length=255, verbose_name='Título')
    author_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    date_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    content_post = models.TextField(verbose_name='Conteúdo')
    summary_post = models.TextField(verbose_name='Resumo')
    category_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, verbose_name='Categoria')
    image_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publisher_post = models.BooleanField(default=False, verbose_name='Publicado')        

    def __str__(self):
        return self.title_post
    
    def save(self, *args, **kwargs):
        super().save(*args, kwargs)
        
        self.resize_image(self.image_post.name, 800)
    
    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img.path)
        width, height = img.size
        new_height = round((new_width * height) / width)
    
        if width <= new_width:
            img.close()
            return
    
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60
        )
        new_img.close
        

class Comentario(models.Model):
    name_comment = models.CharField(max_length=150, verbose_name='Nome')
    email_comment = models.EmailField(verbose_name='E-mail')
    comment = models.TextField(verbose_name='Comentário')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    date_comment = models.DateTimeField(default=timezone.now)
    publisher_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.name_comment