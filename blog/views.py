from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Post
from .forms import FormComentario
from .models import Comentario
from django.contrib import messages
from django.views import View
from django.db.models import Q, Count, Case, When



class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = '-id'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publisher_post=True)
        qs = qs.annotate(
            number_comments=Count(
                Case(
                    When(comentario__publisher_comment=True, then=1)
                )
            )
        )

        return qs
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_articles'] = Post.objects.all()[:1]
        return context
    
    def get_queryset(self):

        pesquisa = self.request.GET.get('search')

        if pesquisa:
            posts = Post.objects.filter(content_post__icontains=pesquisa)
        else:
            posts = Post.objects.all()
        
        return posts


class PostDetailView(View):
    template_name = 'blog/post_detail.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publisher_post=True)
        self.contexto = {
            'post': post,
            'comentarios': Comentario.objects.filter(post_comment=post, publisher_comment=True),
            'form': FormComentario(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']

        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        comentario = form.save(commit=False)

        if request.user.is_authenticated:
            comentario.user_comment = request.user

        comentario.post_comment = self.contexto['post']
        comentario.save()
        messages.success(request, 'Seu comentário foi enviado para revisão.')
        return redirect('post_detalhes', pk=self.kwargs.get('pk'))
    
    
class PostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = '-id'
    paginate_by = 3

    def get_queryset(self):

        pesquisa = self.request.GET.get('search')

        if pesquisa:
            posts = Post.objects.filter(content_post__icontains=pesquisa)
        else:
            posts = Post.objects.all()
        
        return posts