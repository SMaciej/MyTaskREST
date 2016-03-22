from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Task
		fields = ('id', 'url', 'name', 'status', 'priority', 'owner')

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'tasks')
