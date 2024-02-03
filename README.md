# Final-Project

# Web Programming with Python and JavaScript

# Video-Demonstration link: https://youtu.be/Fy-ZRxop4QQ

This website is a food sharing platform powered by [Django](https://www.djangoproject.com/). In this platform, readers can search, create, rate, and buy food items or browse for recipes to cook!

# Distinctiveness and Complexity:

This project differs from the others in the course in that it does not try to replicate the features of a social network or an e-commerce website. Instead of focusing on creating a link between users and other users like the social network project does, this project instead focuses on creating a connection between the user and the website itself. The way the like functionality functions makes it different from the conventional like button found on social media platforms. The website's CSS design also sets it apart from all other initiatives. Unlike project 2, which focuses on the buying and selling of items, this project is not an online store. It lacks a category feature or bid features because the features seen in project 2 are fundamentally different from the buy function. By combining its own cutting-edge elements, this project adopts a distinctive approach to the purchasing and selling experience. In conclusion, this project combines several elements discovered via all of the earlier initiatives. The developer used the expertise and experience gathered from these projects to produce a distinct product that stands out from the competition.

## Files

### capstone folder 

In the capstone folder there is 1 file I modified that django created. In the settings.py file, I installed an app called recipes, which is important, because this app makes the program work.

### recipes folder

In the recipes folder I created, there are 2 folders and 4 files I modified.

#### The four files:

In the models.py file I created 4 models for the website to function with the features. The models are labeled as User, Category, Listing, and Comment.

In the admin.py file, I have registered the models I created mentioned above.

In the urls.py, file I created there are 15 paths in total which the user can login, logout, register into an account. Create, edit, and buy a recipe, and comment on recipes.

In the views.py file, I firstly imported all the models I created. Afterwords, I wrote code for each of the paths I created in the urls.py file. This file is very important because it displays all the features and functions I created. 

#### static folder

There are 2 files called styles.css and index.js. The styles.css folder has the written css for the website and the index.js file contains the like feature.

#### templates folder

The templates folder in this project is the core of its functionality, containing all of the HTML files that the developer created and modified to bring the website to life. One of the most important files in this folder is the index.html file, which provides the HTML and JavaScript for the homepage of the website. This file acts as the starting point for the user's journey, welcoming them and providing them with a glimpse of what the website has to offer.

The layout.html file is also crucial, as it creates the navigation bar and provides the necessary paths for the user to navigate the website with ease. The navigation bar is labeled with different sections such as "Available Recipes", "Add Recipe", "Bought Ingredients", "Log In", "Log Out", and "Register". This file also links the styles.css and index.js files, providing the necessary styling and scripting for the website to function properly.

One of the key features of this website is the ability for users to create and log in to their own accounts. The login.html and register.html files provide the necessary code for this functionality, allowing the user to enter their username, email, and password to create or log in to their account. This feature provides a secure and personalized experience for the user, as they can store their favorite recipes and keep track of the ones they have bought or watched.

The create.html file allows the user to make their own recipe with the given requirements. This feature provides a unique and interactive experience, as users can share their favorite recipes with the community and receive feedback through the like, comment, and buy features. The listing.html file contains the details of each recipe, providing the user with all the necessary information about the ingredients, cooking time, and instructions.

The watchlist.html file is also an important feature, as it contains the watched and bought recipes the user has encountered. This feature provides a convenient way for the user to keep track of their favorite recipes and purchase them if they desire. They also have the option to refund their purchase if they change their mind. The search.html file provides the code for the search feature, allowing the user to quickly and easily find a specific recipe they are looking for.

In conclusion, the templates folder contains all of the necessary files to bring the website to life, providing the user with a secure, personalized, and interactive experience. Whether they want to create their own recipe, browse through different recipes, or buy ingredients, this website has everything they need in one convenient place.

# Features explained in depth

## Main Page

In the main page, you can search text in any part of the recipes by inputing any words in the input box, and click the blue "Search" button.

if you just want to read a new recipe, just click "Available Recipes" button on the top, and you will get some recipes randomly. Additionally, you don't need to log in for those actions.

![mainpage](https://user-images.githubusercontent.com/97413501/209048132-1aae4c93-bd34-458a-89f9-bcb8f1bf530b.png)

## URLs

At the top of the main page are 4 links which are labeled as, Available Recipes, Add Recipe, Bought Ingredients, and Logout.
I will get into detail on what these links do.

## Result Page

In the result page, you can get recipes with title, and it's information of what the dish is. If you don't satisfied with those results, you can continue to search in the top search bar.

## Add Recipe

In this link users will able to share a recipe they made. They must incldue a description, the recipe name, the imageof the dish, the ingredients, the price, and what kind of dish it is.

![addpage](https://user-images.githubusercontent.com/97413501/209049269-8f29c653-1d18-4e63-a705-ec9302a09a94.png)

## Recipe/Dish Page

When the user clicks on a recipe, they are greeted with buying the ingredients, learning the name of the dish, it's information, ingredients, and recipe. Below, they also know who the chef/creator is, the price of the ingredients, and they are allowed to rate and crique the dish. It is followed with a bright blue Like buton as well.

![dishpage](https://user-images.githubusercontent.com/97413501/209048830-e63e8484-f724-4fe9-aa79-5493a327b4b1.png)

## Like Feature

Using JavaScript, I have created a Like button which allows the user to like any dish they find interesting.

![likebutton](https://user-images.githubusercontent.com/97413501/209050153-fddc69dd-7d73-4a6f-bdf5-2ee9d095929e.png)

## Comment Feature

In the recipe page, users are also allowed to rate and comment on dishes they find fascinating. I really enjoyed creating this feature because of how simple, yet powerful it is.

![commentfeature](https://user-images.githubusercontent.com/97413501/209050372-10e8a9c8-ce45-4b73-a645-3f0a3d12c125.png)

## Bought Ingredients

This link will lead to what dishes the user has bought from the available recipes.

![boughtpage](https://user-images.githubusercontent.com/97413501/209050520-8f498193-2f5d-45d7-a903-bb8566b5f13b.png)

## Edit feature

This feature allows you to interact with the recipes you have made. You are able to edit the dishes title. This was done using Javascript and the AJAX request to django view.

![editpage](https://user-images.githubusercontent.com/97413501/209049850-ac237df2-801a-470f-9242-bd0842610980.png)

## Pagination

This website also has a pagination feature that i learned from this course. You are able to click "Next" and "Previous" to move from a page to page. This is very helpful as it organizes the website much better. 

## Django Admin and Superuser: Backend

Creating a superuser in this project is especially helpful when the webiste includes models. I used /admin to help me delete certain recipes when I wanted to.

# Requirements
There are no requirements for this program to work properly.

# Additional comments

Thanks for all people make [CS50's Web Programming with Python and JavaScript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) possible. I really enjoyed working with Javascript, Python, HTML, and CSS.

December 28, 2022



 











