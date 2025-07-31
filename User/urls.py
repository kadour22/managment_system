from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("create-account/", views.add_user_view.as_view(), name="add-user"),
    path("reset-password/", views.ChangePasswordView.as_view(), name="reset-password"),
    path("developer/", views.developer_api_view.as_view(), name="developer"),
    path("tester/", views.tester_api_view.as_view(), name="tester"),

    path("token/", TokenObtainPairView.as_view(), name="obtain-token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="obtain-token"),
]
