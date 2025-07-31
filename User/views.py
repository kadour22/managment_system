# rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
# local imports
from .serializers import user_serializer, accounts_serializer, ChangePasswordSerializer
from .models import User, Account
from .permissions import AdminPermission, DeveloperPermission, TesterPermission

class admin_view(APIView) :
    permission_classes = [AdminPermission]
    def get(self,request) :
        return Response("welcome to admin Dashboard.")

class add_user_view(APIView) :
    permission_classes = [AdminPermission]
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

class tester_api_view(APIView) :
    permission_classes = [TesterPermission]
    def get(self, request, *args, **kwargs) :
        account = Account.objects.get(user=request.user)
        serializer = accounts_serializer(account, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class developer_api_view(APIView) :
    permission_classes = [DeveloperPermission]
    def get(self, request, *args, **kwargs) :
        account = Account.objects.get(user=request.user)
        serializer = accounts_serializer(account, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
