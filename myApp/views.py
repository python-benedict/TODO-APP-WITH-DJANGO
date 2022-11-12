from django.shortcuts import render
from .models import MyToDo
# Create your views here.
def alltodo(request):
    
    tasks = MyToDo.objects.all()
    context = {
        'tasks':tasks,
    }
    return render(request, 'myApp/alltodo', context)