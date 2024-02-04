from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("displayCategory", views.displayCategory, name="displayCategory"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removeWatchlist/<int:id>", views.removeWatchlist, name="removeWatchlist"),
    path("addWatchlist/<int:id>", views.addWatchlist, name="addWatchlist"),
    path("watchlist", views.displayWatchlist, name="watchlist"),
    path("removeBuy/<int:id>", views.removeBuy, name="removeBuy"),
    path("addBuy/<int:id>", views.addBuy, name="addBuy"),
    path("buy", views.displayBuy, name="buy"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("edit/<int:id>", views.edit, name="edit"),
   
]