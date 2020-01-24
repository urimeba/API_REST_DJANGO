from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Apps.REST.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework.decorators import action

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'Error':'Favor de completar los campos'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"Error":"Credenciales no validas"}, status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    print(_)
    return Response({"token":token.key}, status=HTTP_200_OK)


#
# class UserViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, context={'request':request})
#         return Response(serializer.data)
#
#     def create(self, request):
#         post_data = request.data
#         # 'email','last_name'
#         email = request.data['email']
#         last_name = request.data['last_name']
#         user = User.objects.create_user(username="prueba1", email=email, last_name=last_name)
#         return Response("Usuario creado")
#
#     def update(self, request, pk=None):
#         user = User.objects.get(pk=pk)
#         user.email = request.data['email']
#         user.last_name = request.data['last_name']
#         user.save()
#         return Response("Usuario modificado")
#
#     def destroy(self, request, pk=None):
#         user = User.objects.get(pk=pk)
#         response = user.delete()
#         return Response(response)
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset,pk=pk)
#         serializer = UserSerializer(user, context={'request':request})
#         return Response(serializer.data)
#

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-date_joined')
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
