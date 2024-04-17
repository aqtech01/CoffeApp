from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login_page")
def home(request):

    coffee=  Coffe.objects.all()
    context = {
        "title":"Home",
        "items": coffee,
        
    }
    return render(request,"home.html",context)

