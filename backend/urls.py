
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User/', include("User.urls")),
    path('Project/', include("Project.urls")),
    # path('Bug/', include("Bug.urls")),
]
