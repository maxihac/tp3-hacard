from django.shortcuts import render, redirect
from naval_app.forms import *
from .models import Buque

# Create your views here.
def index(request):
    return render(request,"naval_app/index.html")

def crear_buque(request):
    if request.method == "POST":
        form =BuqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form =BuqueForm()

    return render(request, "naval_app/buque_form.html", {"form": form})



def listar_buques(request):
    buques = Buque.objects.all()
    return render(request, 'naval_app/buque_list.html', {'buques': buques})
