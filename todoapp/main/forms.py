from .models import Todo
from django.forms import ModelForm, TextInput


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write down your task here',
            }),
        }

