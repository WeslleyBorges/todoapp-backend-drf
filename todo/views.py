# from rest_framework_mongoengine import viewsets
from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
     queryset = Todo.objects.all()
     serializer_class = TodoSerializer

