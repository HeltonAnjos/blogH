from django.urls import path
from . views import HomeView, PostDetailView, PostsView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)