from django.urls import path
from . import views
app_name='todo'
urlpatterns = [
    path('',views.add_task,name='main'),
    path('add/',views.add_task,name='add'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
]
