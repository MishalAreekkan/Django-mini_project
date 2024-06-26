from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Userprofile,user_login,unversity
# Create your views here.

def signin(request):
    if request.method == "POST":
        s_user = request.POST.get("s_username")
        s_email = request.POST.get("s_email")
        s_pass = request.POST.get("s_pass")
        s_conpass = request.POST.get("s_conpass")
        if s_pass != s_conpass:
            return HttpResponse("passwords does not match")
        if not s_user.isalpha():
            return HttpResponse("password should be in alphabets")
        if len(s_user) < 4:
            return HttpResponse("user name should have 4 letter")
        if len(s_pass) < 2:
            return HttpResponse("should have 2 characters")
        print(s_user,s_email,s_pass,s_conpass)
        return redirect('login')
    return render (request, 'signin.html')

def login(request):
    if request.method == "POST":
        l_user = request.POST.get("l_username")
        l_pass = request.POST.get("l_pass")
        # print(l_user,l_pass)
        login_obj = user_login(names = l_user,passwords = l_pass)
        login_obj.save()
        return redirect('home')
    return render(request,"login.html")

def listed(request):
    data = user_login.objects.all()
    return render(request,"listed.html",{"user":data})

@login_required(login_url='login')
def home(request):
    if request.method == "POST":
        n = request.POST.get("name")
        p = request.POST.get("place")
        d = request.POST.get("dept")
        t = request.POST.get("teac")
        home_obj = unversity(name=n,place=p,department=d,teachers=t)
        home_obj.save()
    # print(unversity.objects.get(place="tn"))
    return render(request,"home.html")

def univ(request):
    datas = unversity.objects.all()
    return render(request,"univ.html",{"univ":datas})

def delete(request,id):
    deleted_one = unversity.objects.get(id=id)
    deleted_one.delete()
    return redirect("univ.html")


# def display(request):
#     data = Userprofile.objects.get(username ="harry")
#     print("username",data.username)
