from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        name_comment = data.get('nome_comentario')
        email_comment = data.get('email_comentario')
        comment = data.get('comentario')

        if len(name_comment) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

    class Meta:
        model = Comentario
        fields = ('name_comment', 'email_comment', 'comment')
