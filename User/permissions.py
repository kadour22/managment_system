from rest_framework.permissions import BasePermission

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "Admin"

class DeveloperPermission(BasePermission) :
    def has_permission(self, request, view):
        return request.user.is_authenticated  and  request.user.role == "Developer" 

class TesterPermission(BasePermission) :
    def has_permission(self, request, view):
        return request.user.is_authenticated  and  request.user.role == "Tester" 