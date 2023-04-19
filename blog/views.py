from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Post
from .forms import FormComentario
from .models import Comentario
from django.contrib import messages
from django.views import View


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostDetailView(View):
    template_name = 'blog/post_detail.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publisher_post=True)
        self.contexto = {
            'post': post,
            'comentarios': Comentario.objects.filter(post_comment=post,
                                                     published_comment=True),
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
            comentario.usuario_comentario = request.user

        comentario.post_comment = self.contexto['post']
        comentario.save()
        messages.success(request, 'Seu comentário foi enviado para revisão.')
        return redirect('post_detalhes', pk=self.kwargs.get('pk'))