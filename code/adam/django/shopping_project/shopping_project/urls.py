"""shopping_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopping_list.views import shopping_list_view, add_item_view, delete_item_view, completeItem, uncompleteItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopping_list/', shopping_list_view, name='index'),
    path('add_item/', add_item_view, name='add'),
    path('delete_item/<int:item_id>/', delete_item_view, name='delete'),
    path('complete/<item_id>', completeItem, name="complete"),
    path('uncomplete/<item_id>', uncompleteItem, name="uncomplete"),
    path('shopping_list/<error>', shopping_list_view, name='index_error'),
]
