# Rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Local imports
from .serializers import bug_serializer
from .models import Bug
from .permissions import BugPermission

class create_bug_report(APIView):
    permission_classes = [BugPermission]

    def post(self, request, *args, **kwargs) :
        serializer = bug_serializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(reported_by=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get(self, request) :
        bugs = Bug.objects.filter(reported_by=request.user)
        serializer = bug_serializer(bugs, many=True)
        return Response(
            serializer.data , status=status.HTTP_200_OK
        )