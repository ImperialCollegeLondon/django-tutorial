from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from .models import Protein, StructureSegment


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


def prot_show_param(request):
    pid = request.GET.get("pid").upper()
    print(pid)
    if len(pid)>0:
        return redirect('show_protein', pid=pid)
    return render(request, "proteins/index.html", context={})

def prot_show(request, pid):
    print(pid)
    protein = Protein.objects.filter(uniprot_id=pid).first()
    print(protein)
    structure_segments = StructureSegment.objects.filter(uniprot_id=pid)
    print(structure_segments)
    context_4template =  {"protein": protein,
                        "structure_segments":structure_segments }
    return render(request, "proteins/protein.html", context = context_4template)
