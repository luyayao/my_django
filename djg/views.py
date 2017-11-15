from django.shortcuts import render
from django.shortcuts import HttpResponse
from djg import models

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        user = models.UserInfo.objects.get(user=username , pwd=password)
        print(user)
        if user:
            return HttpResponse("登录成功！！")
    return render(request, "index.html")

def index2(request):
    return render(request, "index2.html")

def login(request):

    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username, pwd=password)
    userlist = models.UserInfo.objects.all()
    return render(request, "login2.html", locals())