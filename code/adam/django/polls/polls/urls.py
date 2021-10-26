from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path('Now_Is_The_Time/<int:question_id>/', views.detail, name='detail'),
    path('Your_Vote_Counted/<int:question_id>/results/', views.results, name='results'),
    path('Complicated_For_No_Reason/<int:question_id>/vote/', views.vote, name='vote'),
]
