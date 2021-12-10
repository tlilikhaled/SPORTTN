from django.shortcuts import render
from .models import Proteines,Materiels,Vetements
# Create your views here.
#Protéines
def ProtAction(request):
        prot  = Proteines.objects.all()
        return render(request,"product/ProtProduct.html" , {'prot' :prot})
def ProtDetailAction(request,pk):
        protdetails  = Proteines.objects.get(id=pk)
        prot  = Proteines.objects.order_by('?')[:4]
        context = {
                "protdetails" : protdetails,
                "prot" : prot
        }
        return render(request,"product/ProtProductDetails.html" , context)
#Vetements
def VetHAction(request):
        vet  = Vetements.objects.all()
        return render(request,"product/vetements/vetementH.html" , {'vet' :vet})

def VetFAction(request):
        vet  = Vetements.objects.all()
        return render(request,"product/vetements/vetementF.html" , {'vet' :vet})

def VetDetailAction(request,pk):
        vetdetails  = Vetements.objects.get(id=pk)
        vet  = Vetements.objects.order_by('?')[:4]
        context = {
                "vetdetails" : vetdetails,
                "vet" : vet
        }
        return render(request,"product/vetements/vetementsDetails.html" , context)        

#Materiels

def MatBAction(request):
        mat  = Materiels.objects.all()
        return render(request,"product/materiels/materielB.html" , {'mat' :mat})

def MatFAction(request):
        mat  = Materiels.objects.all()
        return render(request,"product/materiels/materielF.html" , {'mat' :mat})

def MatDetailAction(request,pk):
        matdetails  = Materiels.objects.get(id=pk)
        mat  = Materiels.objects.order_by('?')[:4]
        context = {
                "matdetails" : matdetails,
                "mat" : mat
        }
        return render(request,"product/materiels/materielsDetails.html" , context)  