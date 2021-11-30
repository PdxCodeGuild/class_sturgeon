
from rest_framework import generics
from rest_framework import filters

from students import models
from .serializers import StudentSerializer

class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'firstName',
        'lastName',
        'cohort',
        'favoriteTopic',
        'favoriteTeacher',
        'capstone',
        ]
    ordering_fields = '__all__'

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer