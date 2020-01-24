from django.urls import path, include
from Apps.Email import views as views_Email



urlpatterns = [
    path('EnviarCorreo/', views_Email.EnviarCorreo, name="EnviarCorreo"),
]
