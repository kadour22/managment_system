from django.urls import path
from . import views

urlpatterns = [
    path("list-create/", views.list_create_project.as_view(), name='project'),
]