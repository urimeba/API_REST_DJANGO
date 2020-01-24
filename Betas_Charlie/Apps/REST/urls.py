from django.contrib import admin
from django.urls import path
from Apps.REST import views as views_REST


urlpatterns = [
    path('', include(views_REST.UserViewSet.as_view())),
]
