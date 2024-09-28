from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('search/', views.search, name = "search"),
    path('book/<int:bookid>', views.bookDetails, name = "bookdetails"),
    path('reserve/', views.reserve, name = "reserve"),
    path('unreserve/', views.unreserve, name = "unreserve"),
    path('forums/', views.forums, name = "forums"),
    path('forum/<int:id>', views.forum, name = "forum"),
    path('fetch/<int:id>', views.fetchForum, name = "fetch"),
    path('forum/sendmessage/', views.sendMessage, name = "send"),
    path('wishlist/', views.wishlist, name = "wishlist"),
    path('dewishlist/', views.dewishlist, name = "dewishlist"),
    path('wishlist/view/', views.wishlistdisplay, name = "wishlistdisplay"),
    path('reservations/view/', views.reservationsdisplay, name = "reservationsdisplay"),
    path('logout/', views.logout, name = "logout")
]
