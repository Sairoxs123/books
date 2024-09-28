from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Users)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    ordering = ('id', )
    search_fields = ('email', )

@admin.register(Books)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    ordering = ('id', )
    search_fields = ('title',)

@admin.register(Reservations)

class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    ordering = ('id', )
    search_fields = ('name', 'email')

@admin.register(Wishlist)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    ordering = ('id', )
    search_fields = ('name', 'email')

@admin.register(Forums)

class ForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'forum')
    ordering = ('id', )
    search_fields = ('forum',)

@admin.register(Messages)

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver')
    ordering = ('id',)
    search_fields = ('sender', 'receiver')
