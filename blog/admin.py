from django.contrib import admin
from .models import Post, Comentario, Categoria 
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title_post', 'author_post', 'date_post',
                    'category_post', 'publisher_post',)
    list_editable = ('publisher_post',)
    list_display_links = ('id', 'title_post',)
    summernote_fields = ('content_post',)


admin.site.register(Post, PostAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_comment', 'email_comment',
                    'post_comment', 'date_comment',
                    'publisher_comment')
    list_editable = ('publisher_comment',)
    list_display_links = ('id', 'name_comment', 'email_comment',)


admin.site.register(Comentario, ComentarioAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat')
    list_display_links = ('id', 'name_cat')


admin.site.register(Categoria, CategoriaAdmin)