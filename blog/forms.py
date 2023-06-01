from django import forms
from .models import Comentario


class FormComentario(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['name', 'comment']

        
class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
