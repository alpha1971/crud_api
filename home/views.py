from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from home import serializers 
# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE']) 
# @api_view(['GET', 'POST']) 
def todos(request, pk=None): 
    if request.method == 'GET':
        id=pk 
        if id is not None: 
            todo_data = todo.objects.get(id=id)
            serializer = TodoSerializer(todo_data)  
            return Response({"message": "Get Data", "data":serializer.data}) 
        todo_data =todo.objects.all() 
        serializer = TodoSerializer(todo_data,many=True) 
        return Response({"message": "all data", "data":serializer.data}) 
        

    if request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data Created"})
        return Response({serializer.errors}) 
    
    
    if request.method == "PUT":
        id=pk
        todo_data = todo.objects.get(id=id)
        serializer = TodoSerializer(todo_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data Update"})
        return Response({serializer.errors})  


    if request.method == "PATCH":
        id=pk
        todo_data = todo.objects.get(id=id)
        serializer = TodoSerializer(todo_data,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data  patch"}) 
        return Response({serializer.errors})  
    
    if request.method == "DELETE":
        id=pk
        todo_data = todo.objects.get(id=id)
        todo_data.delete()  
        return Response({"Data  Delete"}) 
      
    
    
    
        
            