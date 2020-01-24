from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Apps.Email.serializers import UserSerializer, GroupSerializer

# Create your views here.
def EnviarCorreo(request):
    correo_usuario = "carlosd_eg@yahoo.com.mx"
    remitente, correo_remitente = "Betas", "betascharlie17@gmail.com"
    html_content = get_template("correo.html").render({"nombre_usuario":"Carlos Estrada"})
    msg = EmailMultiAlternatives(remitente, html_content, correo_remitente,[correo_usuario])
    msg.content_subtype = "html"
    msg.send()

    html_content = get_template('Default/correo/solicitudCambioDeContrasenia.html').render({'nombre' : user.first_name, 'apellidos' : str(user.last_name.split("_")[0]) +" "+ str( user.last_name.split("_")[1]), 'clv' : clv})
    msg = EmailMultiAlternatives(remitente, html_content, correo_remitente, [correo_usuario])
    msg.content_subtype = "html"
    msg.send()

    return HttpResponse("Enviado")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
