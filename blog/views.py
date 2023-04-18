from .models import Post
from django.views.generic import ListView, DetailView, TemplateView


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

###class PostList(ListView):
    ###queryset = Post.objects.filter(status=1).order_by('-created_on')
    ###template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 