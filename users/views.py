from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users import serializers as srz
from users.models import User
# Create your views here.

class UserListMainView(GenericViewSet):
    serializer_class = srz.UserListSerializer

 

    def list(self, request):
        queryset = User.objects.all()
        print(queryset)
        serializer =srz.UserListSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = srz.UserListSerializer(user)
        return Response(serializer.data)    