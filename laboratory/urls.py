from django.urls import path
from laboratory.views.list_lab import List_Lab

app_name = 'laboratorio'

urlpatterns = [
    path('<int:pk>/', List_Lab.as_view(), name='list_lab')
]
