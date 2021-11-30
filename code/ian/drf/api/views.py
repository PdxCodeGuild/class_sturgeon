from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from students import models
from .serializers import StudentSerializer



# Create your views here.
class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'first_name',
        'last_name',
        'cohort',
        'favorite_topic',
        'favorite_teacher',
        'capstone',
        ]

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class ListStudentFirst(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        first_name = self.kwargs['first_name']
        return models.Student.objects.filter(first_name=first_name) 