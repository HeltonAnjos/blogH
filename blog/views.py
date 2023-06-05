from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.shortcuts import render

from .models import Post
from .forms import FormComentario, ContactForm
from .models import Comentario
from django.contrib import messages
from django.views import View
from django.db.models import Q, Count, Case, When
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import get_connection



class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('category_post')
        qs = qs.order_by('-id').filter(publisher_post=True)
        qs = qs.annotate(
            number_comments=Count(
                Case(
                    When(comentario__status='Lido', then=1)
                )
            )
        )
        return qs
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_articles'] = Post.objects.all().order_by('-id')[:1]
        return context
    

class PostDetailView(View):
    template_name = 'blog/post_detail.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publisher_post=True)
        self.contexto = {
            'post': post,
            'comentarios': Comentario.objects.filter(post=post, status='Lido'),
            'form': FormComentario(request.POST or None),
        }

    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']

        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        comentario = form.save(commit=False)

        comentario.post = self.contexto['post']
        comentario.save()
        messages.success(request, 'Seu comentário foi enviado para revisão.')
        return redirect('post_detail', pk=self.kwargs.get('pk'))
    
    
class PostsView(HomeView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = '-id'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        pesquisa = self.request.GET.get('search')
    
        if not pesquisa:
            return qs

        qs = qs.filter(
            Q(title_post__icontains=pesquisa) |
            Q(author_post__first_name__iexact=pesquisa) |
            Q(content_post__icontains=pesquisa) |
            Q(summary_post__icontains=pesquisa) |
            Q(category_post__name_cat__iexact=pesquisa)
        )

        return qs
    
class CategoriaView(PostsView):
    template_name = 'blog/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(category_post__name_cat__iexact=categoria)

        return qs
    

class EmailView(FormView):
    
    template_name = 'blog/contacts.html'  
    form_class = ContactForm  
    success_url = '/'  

    def form_valid(self, form):
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email_user = form.cleaned_data['email']  

        
        corpo_mensagem = f"""
        Nome: {name}
        Email do remetente: {email_user}
        Assunto: {subject}
        Mensagem: {message}
        """

        connection = get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS,
            use_ssl=settings.EMAIL_USE_SSL    
        )  

        send_mail(
            subject,
            corpo_mensagem,
            settings.DEFAULT_FROM_EMAIL,
            ['seuEmailQueReceberáOsEmailsDosUsuários'],
            fail_silently=False,
            connection=connection
        )
        
        messages.success(self.request, 'O e-mail foi enviado com sucesso!')

        return super().form_valid(form) 
