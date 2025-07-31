from rest_framework import serializers
from .models import Project

class project_serializer(serializers.ModelSerializer) :
    class Meta :
        model  = Project
        fields = '__all__'
        read_only_fields = ['id','created_by']