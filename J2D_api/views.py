from J2D_api.models import Todo, ItemList, Item
from django.contrib.auth.models import User
from J2D_api.serializer import TodoSerializer, UserSerializer, ItemListSerializer, ItemSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class UserTodos(APIView):
    def get(self, request,format=None):
        todos = Todo.objects.filter(user = request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class UserItemLists(APIView):
    def get(self, request,format=None):
        lists = ItemList.objects.filter(user = request.user)
        serializer = ItemListSerializer(lists, many=True)
        return Response(serializer.data)

class UserItems(APIView):
    def get(self, request,format=None):
        items = Item.objects.filter(user = request.user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class AddItem(APIView):
    def post(self, request, format=None):
        l = ItemList.objects.get(pk = request.data['list_rel'])
        serializer = ItemSerializer(data={'description':request.data['description']})
        if serializer.is_valid():
            serializer.save(user = request.user, list_rel = l)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddItemList(APIView):
    def post(self, request, format=None):
        serializer = ItemListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


class EditItem(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EditItemList(APIView):
    def get_object(self, pk):
        try:
            return ItemList.objects.get(pk=pk)
        except ItemList.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        item_list = self.get_object(pk)
        serializer = ItemListSerializer(item_list, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item_list = self.get_object(pk)
        item_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)