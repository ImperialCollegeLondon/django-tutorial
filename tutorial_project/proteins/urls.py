from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.prot_autocomplete, name="search"),
    path("show/<str:pid>/", views.prot_show, name="show")
]