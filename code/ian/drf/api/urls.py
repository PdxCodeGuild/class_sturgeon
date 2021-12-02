from django.urls import path

from .views import ListStudent, DetailStudent, ListStudentFirst

urlpatterns = [
    path('', ListStudent.as_view()),
    path('<int:pk>/', DetailStudent.as_view()),
    path('<first_name>/', ListStudentFirst.as_view()),
]