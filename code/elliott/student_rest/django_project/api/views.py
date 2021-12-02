from rest_framework import generics

from students.models import student
from .serializers import studentSerializer

class studentAPIView(generics.ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer