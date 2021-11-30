from django.views.generic import ListView

from .models import student

class StudentListView(ListView):
    model = student
    template_name = 'student_list.html'
