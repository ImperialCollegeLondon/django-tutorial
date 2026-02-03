from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.prot_autocomplete, name="search"),
    path("protein/", views.prot_show_param, name="show_protein_param"),
    path("protein/<str:pid>/", views.prot_show, name="show_protein")
]