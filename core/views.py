from django.shortcuts import render, redirect, HttpResponse
from .models import *
from datetime import date

# Create your views here.


def index(request):
    if not request.session.get("logged-in"):
        return redirect("/login")

    name = request.session.get("name")
    email = request.session.get("email")

    results = Books.objects.all()

    return render(request, "main/index.html", {"name":name, "email":email, "books":results})

def search(request):

    if request.method == "POST":
        query = request.POST['title'].strip()

        results = Books.objects.all().filter(title__contains=query)

        return render(request, "main/search.html", {"books":results})

    return redirect("/")

def bookDetails(request, bookid):
    if not request.session.get("logged-in"):
        return redirect("/login")

    results = Books.objects.all().filter(id=bookid)

    email = request.session.get("email")

    #id instance
    id_instance = Books.objects.get(id=bookid)

    #email instance
    email_instance = Users.objects.get(email=email)

    wished = False

    wish = None

    reserved = False

    res = []

    res = Reservations.objects.filter(email=email_instance).filter(bookid=id_instance)

    if res:
        reserved = True

    else:
        reserved = False

    try:
        wish = Wishlist.objects.get(bookid=id_instance)
        wished = True
    except:
        wished = False

    url = results[0].url

    return render(request, "main/details.html", {"books":results, "email":email, "wished":wished, "rating":results[0].rating, "url":url, "reserved":reserved})

def reserve(request):
    if request.method == "POST":
        bookid = request.POST["id"]
        email = request.POST["email"]

        if bookid == "" or email == "":
            return redirect("/")


        #book instance
        bookints = Books.objects.get(id=bookid)

        #email instance
        emailinst = Users.objects.get(email=email)

        Reservations.objects.create(email=emailinst, bookid=bookints, date=date.today())

        return redirect(f"/book/{bookid}")

    return redirect("/")

def unreserve(request):
    if request.method == "POST":
        bookid = request.POST["id"]
        email = request.POST["email"]

        if bookid == "" or email == "":
            return redirect(f"/book/{bookid}")

        #book instance
        bookints = Books.objects.get(id=bookid)

        #email instance
        emailinst = Users.objects.get(email=email)

        Reservations.objects.get(email=emailinst, bookid=bookints).delete()

        return redirect(f"/book/{bookid}")

    return redirect("/")

def wishlist(request):

    if request.method == "POST":
        bookid = request.POST["id"]
        email = request.POST["email"]

        if bookid == "" or email == "":
            return redirect("/")

        id_inst = Books.objects.get(id=bookid)
        email_inst = Users.objects.get(email=email)

        results = Wishlist.objects.all().filter(email=email_inst, bookid=id_inst)

        if results:
            pass

        else:
            Wishlist.objects.create(email=email_inst, bookid=id_inst)

        return redirect(f"/book/{bookid}")

    return redirect("/")

def dewishlist(request):

    if request.method == "POST":
        bookid = request.POST["id"]
        email = request.POST["email"]

        if bookid == "" or email == "":
            return redirect("/")

        id_inst = Books.objects.get(id=bookid)
        email_inst = Users.objects.get(email=email)

        Wishlist.objects.get(email=email_inst, bookid=id_inst).delete()

        return redirect(f"/book/{bookid}")

    return redirect("/")

def wishlistdisplay(request):
    if not request.session.get("logged-in"):
        return redirect("/login")

    email = request.session.get("email")

    #email instance
    email_inst = Users.objects.get(email=email)

    results = Wishlist.objects.all().filter(email=email_inst)

    books = []

    if results:
        for i in results:
            book = Books.objects.get(id=int(str(i.bookid)))
            books.append(f'''
            <a href="/book/{ book.id }">
                <div class="store-box">
                    <img src="{ book.pic.url }" width="56" height="56">
                    <h2>{ book.title }</h2>
                    <p>{ book.price }.00 AED</p>
                </div>
            </a>
''')

    else:
        books = False

    return render(request, "main/wishlist.html", {"books":books})


def reservationsdisplay(request):
    if not request.session.get("logged-in"):
        return redirect("/login")

    email = request.session.get("email")

    #email instance
    email_inst = Users.objects.get(email=email)

    results = Reservations.objects.all().filter(email=email_inst)

    books = []

    if results:
        for i in results:
            book = Books.objects.get(id=int(str(i.bookid)))
            books.append(f'''
            <a href="/book/{ book.id }">
                <div class="store-box">
                    <img src="{ book.pic.url }" width="56" height="56">
                    <h2>{ book.title }</h2>
                    <p>{ book.price }.00 AED</p>
                </div>
            </a>
''')

    else:
        books = False

    return render(request, "main/reservations.html", {"books":books})


def forums(request):

    if not request.session.get("logged-in"):
        return redirect("/login")

    forums = Forums.objects.all()

    return render(request, "main/forum.html", {"forums":forums})


def forum(request, id):

    if not request.session.get("logged-in"):
        return redirect("/")

    # receiver instance
    x = Forums.objects.get(id=id)

    email = request.session.get("email")

    return render(request, "main/forum-chat.html", {"id":id, "name":x.forum, "email":email})

def fetchForum(request, id):
    # receiver instance
    x = Forums.objects.get(id=id)

    results = Messages.objects.all().filter(receiver=x)

    email = request.session.get("email")

    messages = []

    for i in results:
        if str(i.sender) == email:
            messages.append(f'''
            <div class="right">
                <span>
                    { i.message }
                </span>
            </div>
''')

        else:
            messages.append(f'''
            <div class="left">
                <span>
                    { i.message }
                    <br><br>
                    -{ Users.objects.get(email=i.sender).name }
                </span>
            </div>
''')

    return HttpResponse(messages)

def sendMessage(request):
    sender_email = request.GET["sender"]
    forum_id = int(request.GET["forum"])
    message = request.GET["message"]

    #sender instance
    sender = Users.objects.get(email=sender_email)

    #forum instance
    forum = Forums.objects.get(id=forum_id)

    Messages.objects.create(sender=sender, receiver=forum, message=message)

    return HttpResponse("success")

def logout(request):
    request.session["logged-in"] = False
    request.session["email"] = None
    request.session["name"] = None

    return redirect("/login")

