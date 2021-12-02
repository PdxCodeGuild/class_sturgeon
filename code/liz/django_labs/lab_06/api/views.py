from rest_framework import generics, permissions, viewsets

from students.models import Student
from .serializers import StudentSerializer
from .permissions import IsAuthorOrReadOnly


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthorOrReadOnly]

