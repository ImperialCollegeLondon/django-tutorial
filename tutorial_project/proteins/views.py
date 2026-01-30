from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from .models import Protein


# Create your views here.
def index(request):
    #return HttpResponse("Welcome to the proteins app", )
    return render(request, "proteins/index.html", context={})

def prot_autocomplete(request):
    q = request.GET.get("q").upper()
    print(q)
    proteins = Protein.objects.filter(uniprot_id__startswith=q).all()
    uniprot_ids = [p.uniprot_id for p in proteins]
    print(uniprot_ids)
    return JsonResponse({"uniprot_ids": uniprot_ids})

def prot_show(request):
    q = request.GET.get("q").upper()
    print(q)
    protein = Protein.objects.filter(uniprot_id=q).first()
    print(protein)
    return render(request, "proteins/show_table.html", context = {"protein": protein})
