from .models import *
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = todo
        fields = ['id', 'Description', 'Completed', 'Created_by'] 