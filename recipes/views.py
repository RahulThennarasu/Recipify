from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from markdown2 import Markdown
from django.http import JsonResponse
import json


from .models import User, Category, Listing, Comment




def edit(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_listing = Listing.objects.get(pk=id)
        edit_listing.title = data["content"]
        edit_listing.save()
        return JsonResponse({"message": "Change successful"})


def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    return render(request, "recipes/listing.html", {
        "listing": listingData,
        "isListingInWatchlist": isListingInWatchlist,
        "allComments": allComments
    })

def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['newComment']

    newComment = Comment(
        author=currentUser,
        listing=listingData,
        message=message
    )

    newComment.save()

    return HttpResponseRedirect(reverse("listing",args=(id, )))


def displayWatchlist(request):
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    return render(request, "recipes/watchlist.html", {
        "listings": listings,
    })

def removeWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def addWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def displayBuy(request):
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    return render(request, "recipes/watchlist.html", {
        "listings": listings,
    })

def removeBuy(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def addBuy(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def index(request):
    query = request.GET.get("q")
    listings = Listing.objects.filter(isActive=True)
    if query:
        listings = listings.filter(title__icontains=query)
    paginator = Paginator(listings, 4)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    posts_of_the_page = paginator.get_page(page_number)

    allCategories = Category.objects.all()
    return render(request, "recipes/index.html", {
        "posts_of_the_page": posts_of_the_page,
        "listings": listings,
        "categories": allCategories,
        "query": query,
        
    })



def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        activeListings = Listing.objects.filter(isActive=True, category=category)
        allCategories = Category.objects.all()
        return render(request, "recipes/index.html", {
            "listings": activeListings,
            "categories": allCategories
        })



def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "recipes/create.html", {
            "categories": allCategories
        })
    else:
        #
        title = request.POST["title"]
        description = request.POST["description"]
        recipeMade = request.POST['recipeMade']
        imageUrl = request.POST["imageUrl"]
        price = request.POST["price"]
        category = request.POST["category"]
        # 
        currentUser = request.user

        #
        categoryData = Category.objects.get(categoryName=category)
        #
        newListing = Listing(
            title=title,
            description=description,
            recipeMade=recipeMade,
            imageUrl=imageUrl,
            price=float(price),
            category=categoryData,
            owner=currentUser
        )
        #
        newListing.save()
        #
        return HttpResponseRedirect(reverse(index))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "recipes/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "recipes/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "recipes/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "recipes/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "recipes/register.html")
