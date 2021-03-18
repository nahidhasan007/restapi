from django.shortcuts import render
from .models import Todo
from rest_framework import generics
from .serializers import TodoSerializer

# Create your views here.
def index(request):
    data = Todo.objects.all()
    return render(request,'todo/index.html',{'data':data})

class TodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer    
