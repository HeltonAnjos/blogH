from django.urls import path, include
from . views import HomeView, PostDetailView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)