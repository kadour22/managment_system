from rest_framework import serializers
from .models import Bug

class bug_serializer(serializers.ModelSerializer) :
    class Meta :
        model  = Bug
        fields = "__all__"
        read_only_fields = ['id','reported_by']