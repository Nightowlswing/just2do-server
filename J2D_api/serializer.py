from rest_framework import serializers
from django.contrib.auth.models import User
from J2D_api.models import Todo, ItemList, Item
    
class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # index = serializers.ReadOnlyField(source='todo.index')
    class Meta:
        model = Todo
        fields = ['id','description', 'day', 'user', 'status']

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'todos']
    

class ItemListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all(), default=[])
    # index = serializers.ReadOnlyField(source='todo.index')
    class Meta:
        model = ItemList
        fields = ['id','title', 'user', 'items']

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    list_id = serializers.ReadOnlyField(source='list_rel.id')
    class Meta:
        model = Item
        fields = ['id','description', 'user', 'status','list_id']