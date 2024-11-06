from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва новини'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс новини'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата новини',
                'type': 'datetime-local'  # Убедитесь, что используется правильный input type
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text новини'
            }),
        }
