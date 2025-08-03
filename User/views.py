# rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
# local imports
from .utils import get_account_data
from .serializers import user_serializer, accounts_serializer, ChangePasswordSerializer
from .models import User, Account
from .permissions import AdminPermission, DeveloperPermission, TesterPermission

class add_user_view(APIView) :
    
    def post(self, request, *args, **kwargs) :
        serializer = user_serializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)        

class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        if request.user.role == "Developer":
            return get_account_data(user=request.user)
        elif request.user.role == "Tester":
            return get_account_data(user=request.user)
        elif request.user.role == "Admin":
            return get_account_data(user=request.user)
        return Response({"error": "Unknown role"}, status=status.HTTP_403_FORBIDDEN)