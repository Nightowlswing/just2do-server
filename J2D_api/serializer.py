from rest_framework import serializers
from django.contrib.auth.models import User
from J2D_api.models import Todo
    
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
