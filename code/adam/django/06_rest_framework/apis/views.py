
from rest_framework import generics
from rest_framework import filters

from students import models
from .serializers import StudentSerializer
from .permissions import isStafforReadOnly

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
    permission_classes = [isStafforReadOnly]


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [isStafforReadOnly]