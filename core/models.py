from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField("Name", max_length=50, blank=False)
    email = models.EmailField("Email", max_length=20)
    password = models.CharField("Password", max_length=20)

    def __str__(self):
        return str(self.email)

class Books(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    title = models.CharField('Title', max_length=100, blank=False)
    description = models.CharField('Description', max_length=1024, blank=True)
    author = models.CharField('Author', max_length=50, null=False)
    location = models.CharField('Location', max_length=1024, blank=False)
    pic = models.ImageField(upload_to='books/')
    price = models.IntegerField(blank=False, null=False)
    rating = models.IntegerField(blank=False)
    url = models.CharField("Link To Buy", max_length=1024)

    def __str__(self):
        return str(self.id)

class Reservations(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    bookid = models.ForeignKey(Books, related_name="bookid", blank=False, on_delete=models.CASCADE)
    email = models.ForeignKey(Users, related_name="emaili", on_delete=models.CASCADE)
    date = models.DateField("Date")

class Wishlist(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    bookid = models.ForeignKey(Books, related_name="book", blank=False, on_delete=models.CASCADE)
    email = models.ForeignKey(Users, related_name="emailid", on_delete=models.CASCADE)

class Forums(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    forum = models.CharField("Forum Name", max_length=100)

    def __str__(self):
        return str(self.forum)

class Messages(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    sender = models.ForeignKey(Users, related_name="senderr", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Forums, related_name="receiverr", on_delete=models.CASCADE)
    message = models.CharField("Message", max_length=1024)

