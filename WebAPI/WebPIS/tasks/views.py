from django.contrib.auth.models import User, AnonymousUser
from tasks.serializers import UserSerializer, TaskSerializer
from tasks.models import Task
from rest_framework import generics, viewsets, permissions, renderers
from tasks.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if type(user) == AnonymousUser:
            return NotAuthenticated
        else:
            return Task.objects.filter(owner=user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, validated_data):
        print "DATA::::"
        print validated_data.data['username']
        user = User.objects.create(
            username=validated_data.data['username'],
            email=validated_data.data['email'],
        )

        user.set_password(validated_data.data['password'])
        user.save()

        serializer.save()

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })
