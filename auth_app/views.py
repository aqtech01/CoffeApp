from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def login_page(request):
    re = request.POST
    if request.method == "POST":
        username = re.get("username")
        password = re.get("pass")
        user= authenticate(username=username,password=password)
        login(request,user)
        return redirect("home")
    else:
        messages.warning(request,"Invalid Cradential")
    context = {
        "title":"Login",
    }
    return render(request,"login.html",context)
def signup_page(request):
    try:
        re = request.POST
        if request.method == "POST":
            username = re.get("username")
            email = re.get("email")
            password1 = re.get("password1")
            password2 = re.get("password2")
            if password1 != password2:
                messages.warning(request,"Password and Confirm Password Should be same")
            else:
                user = User.objects.create_user(username,email,password1)
                user.save()
                return redirect("login_page")
    except BaseException as e:
        messages.warning(request,"Ivalid Error!")
        return e


    context = {
        "title":"SignUp",
    }
    return render(request,"signup.html",context)

def logout_page(request):
    logout(request)
    return redirect("login_page")