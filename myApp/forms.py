from django import forms
from .models import MyToDo

class MyToDoForm(forms.ModelForm):
    class Meta:
        models = MyToDo
        fields = ['task',]