from django.urls import path
from . import views

urlpatterns = [
    path("report-bug/", views.create_bug_report.as_view()),
]
