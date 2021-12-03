from django.db.models import query
from rest_framework import generics

from students_app import models
from .serializers import StudentSerializer

# Create your views here.
class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer


