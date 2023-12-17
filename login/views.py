from django.shortcuts import render, redirect
from core.models import *

# Create your views here.

def index(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        results = Users.objects.all().filter(email=email)

        if results:
            if results[0].password == password:
                request.session["logged-in"] = True
                request.session["email"] = email
                request.session["name"] = results[0].name
                return redirect("/")

            else:
                return render(request, "login/index.html", {"error":"wrongpass"})

        else:
            return render(request, "login/index.html", {"error":"noexist"})

    return render(request, "login/index.html")
