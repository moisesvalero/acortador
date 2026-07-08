from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create", views.create, name="create"),
    path("health", views.health, name="health"),
    path("<str:code>", views.redirect_view, name="redirect"),
]
