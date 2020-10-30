from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:todo_id>', views.delete, name='del'),
    path('update/<int:todo_id>', views.update, name='upd')
]
