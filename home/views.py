from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from home import serializers 
from django.db import connection

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE']) 
def todos(request, pk=None): 
    if request.method == 'GET':
        id=pk 
        if id is not None: 
            # todo_data = todo.objects.get(id=id)
            todo_data = todo.objects.raw('SELECT * FROM home_todo WHERE id=%s',[id])[0] 
            # print(todo_data)   
            serializer = TodoSerializer(todo_data)  
            return Response({"message": "Get Data", "data":serializer.data}) 
        # todo_data =todo.objects.all() 
        todo_data=todo.objects.raw('SELECT * FROM home_todo') 
        serializer = TodoSerializer(todo_data,many=True) 
        return Response({"message": "all data", "data":serializer.data}) 
        
    if request.method == "POST":
        # return Response({request.Description})
        # return Response(request.data['id'])
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO home_todo (Description, Completed,Created_by) VALUES (%s, %s,%s)',[request.data['Description'],request.data['Completed'],request.data['Created_by']])
            row = cursor.fetchone()

        # serializer = todo.objects.raw()
        # serializer = TodoSerializer(serializer)
        # if serializer.is_valid():
            # serializer.save()
            return Response({"Data Created"})
        return Response({serializer.errors}) 
   
    
    
    if request.method == "PUT":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE home_todo SET Description = %s,Created_by = %s WHERE id = %s' ,[request.data['Description'],request.data['Created_by'],pk])
            row = cursor.fetchone()
        # todo_data = todo.objects.get(id=id)
        # serializer = TodoSerializer(todo_data,data=request.data)
        # if serializer.is_valid():
            # serializer.save()
            return Response({"Data Update"})
        return Response({serializer.errors})  


    if request.method == "PATCH":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE home_todo SET Description = %s,Created_by = %s WHERE id = %s' ,[request.data['Description'],request.data['Created_by'],pk])
            row = cursor.fetchone()
        # id=pk
        # todo_data = todo.objects.get(id=id)
        # serializer = TodoSerializer(todo_data,data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
            return Response({"Data  patch"}) 
        return Response({serializer.errors})  
    
    if request.method == "DELETE":
        # id=pk
        # todo_data = todo.objects.get(id=id)
        # todo_data.delete() 
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM home_todo WHERE id = %s' ,[pk])
            row = cursor.fetchone() 
        return Response({"Data  Delete"}) 
      
    
def completed(request, id=None):
    
    todo_data = todo.objects.get(pk=id) 
    if todo_data.Completed:
        todo_data.Completed = False 
    else:
        todo_data.Completed = True
    todo_data.save()  
    return HttpResponse(todo_data, 200)     

    
        
def create(request):
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO home_todo (Description, Completed,Created_by) VALUES (%s, %s,%s)',[request.data['Description'],request.data['Completed'],request.data['Created_by']])
        row = cursor.fetchone()
    return Response({"Data Created"})