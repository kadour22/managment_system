# rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
# local imports
from .serializers import project_serializer
from .models import Project
from .permissions import ProjectPermission

class list_create_project(APIView) :
    permission_classes = [ProjectPermission]
    def post(self, request, *args, **kwargs) :
        serializer = project_serializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get(self, request, *args, **kwargs) :
        projects = Project.objects.select_related('created_by').all()
        serializer = project_serializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
