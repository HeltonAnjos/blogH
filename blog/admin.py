from django.contrib import admin
from .models import Post, Comentario, Categoria 
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo_post', 'autor_post', 'data_post',
                    'categoria_post', 'publicado_post',)
    list_editable = ('publicado_post',)
    list_display_links = ('id', 'titulo_post',)
    summernote_fields = ('conteudo_post',)


admin.site.register(Post, PostAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario',
                    'post_comentario', 'data_comentario',
                    'publicado_comentario')
    list_editable = ('publicado_comentario',)
    list_display_links = ('id', 'nome_comentario', 'email_comentario',)


admin.site.register(Comentario, ComentarioAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')
    list_display_links = ('id', 'nome_cat')


admin.site.register(Categoria, CategoriaAdmin)