from django.shortcuts import render

# Create your views here.
def alltodo(request):
    return render(request, 'myApp/alltodo', context)