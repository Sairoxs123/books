from django.shortcuts import render, redirect
from core.models import Users

# Create your views here.

def index(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        repass = request.POST["repass"]
        name = request.POST["name"]

        if not email or not password or not repass or not name:
            return render(request, "signup/index.html", {"error":"empty"})

        try:
            results = Users.objects.get(email=email)
            return render(request, "signup/index.html", {"error":"exists"})

        except:
            if password == repass:
                Users.objects.create(name = name, email=email, password=password)
                request.session["logged-in"] = True
                request.session["email"] = email
                request.session["name"] = name
                return redirect("/")

            else:
                return render(request, "signup/index.html", {"error":"notsame"})

    return render(request, "signup/index.html")
