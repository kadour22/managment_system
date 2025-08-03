from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("create-account/", views.add_user_view.as_view(), name="add-user"),
    path("reset-password/", views.ChangePasswordView.as_view(), name="reset-password"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    
    path("token/", TokenObtainPairView.as_view(), name="obtain-token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="obtain-token"),
]
