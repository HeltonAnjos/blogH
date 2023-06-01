from django.urls import path
from . views import HomeView, PostDetailView, PostsView, CategoriaView, EmailView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('categoria/<str:categoria>', CategoriaView.as_view(), name='categorias'),
    path('send-email/', EmailView.as_view(), name='send_email'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)