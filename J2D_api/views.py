# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from J2D_api.models import Todo
from django.contrib.auth.models import User
from J2D_api.serializer import TodoSerializer
from J2D_api.serializer import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# @api_view(['GET', 'POST'])
# def todo_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = UserSerializer(todos, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def add_todo(request):
#     if request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         print('IS IT VALID OR NOT??? WHO KNOWS>>>>,........',serializer.is_valid())
#         user = User.objects.filter(username = request.data['user'])[0]
#         print('here is users',request.data['user'])
#         if serializer.is_valid():
#             serializer.save(user = user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_todo(request, pk):
#     if request.method == 'GET':
#         todos = Todo.objects.filter(pk = pk)
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)

class UserTodos(APIView):
    def get(self, request,format=None):
        todos = Todo.objects.filter(user = request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class AddTodo(APIView):
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditTodo(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class Authenctication(APIView):
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         user = User.objects.filter(username = request.data['user'])[0]
#         print(user)
#         return Response(serializer.data)