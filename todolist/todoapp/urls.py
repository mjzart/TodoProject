from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name = '_index_'),
    path('additem/', views.additem, name = 'additem'),
    path('deleteitem/<id>', views.delete_item, name='delete_item'),
    path('completeitem/<id>', views.complete_item, name='complete_item'),
]