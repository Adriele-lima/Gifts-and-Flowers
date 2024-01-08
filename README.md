# :blossom::gift::tulip: Gifts and Flowers

Welcome to [Gifts and Flowers!](https://gifts-and-flowers-6d75002e0957.herokuapp.com/) This is a e-commerce web application designed for people who loves to gift and surprise their loved ones!'

## Table of Contents

* [UX Design](#heavy_check_mark-ux-design)
    * [The Strategy Plane](#round_pushpin-the-strategy-plane)
    * [The Sites Ideal User](#round_pushpin-the-sites-ideal-user)
    * [Site Goals](#round_pushpin-site-goals)
    * [User Stories](#round_pushpin-user-stories)
    * [The Scope Planned](#round_pushpin-the-scope-plane)
    * [Future Enhancements](#round_pushpin-future-enhancements)
* [Technologies](#heavy_check_mark-technologies)
* [Exiting Features](#heavy_check_mark-existing-features)
* [Testing](#heavy_check_mark-testing)
    * [Responsiveness](#round_pushpin-responsiveness)
    * [Browser Compatibility](#round_pushpin-browser-compability-testing)
    * [Light House](#round_pushpin-lighthouse)
    * [Agile and Milestones](#round_pushpin-agile-and-milestone)
    * [Bugs]()
    * [Code Validation](#round_pushpin-code-validation)
        * [HTML](#round_pushpin-html)
        * [CSS](#round_pushpin-css)
        * [Java Script](#round_pushpin-javascript)
        * [Python](#round_pushpin-python)
* [Deployment](#heavy_check_mark-deployment)
    * [How to Fork](#round_pushpin-how-to-fork)
    * [How to Deploy](#round_pushpin-how-to-deploy)
* [Credits](#heavy_check_mark-credits)


## :heavy_check_mark: UX Design

### :round_pushpin: The Strategy Plane

*  Gifts and Flowers is intended to be an e-commerce site for users to find their perfect gift.
Users will also be able to rate the products and see other peoples rating experience, so they can find the perfect product. The graphical elements and overall
design of the site provide the user with a fun and enjoyable environment.

### :round_pushpin: The Sites Ideal User

* Occasional Shoppers: The ideal user is someone who shops for gifts and flowers on special occasions such as birthdays, anniversaries, weddings, holidays, and other celebrations. They might not be frequent shoppers but are willing to spend on thoughtful and meaningful gifts.
* Busy Professionals: Target individuals with busy lifestyles who may not have the time to physically shop for gifts. An easy-to-navigate website with quick ordering processes and delivery options will appeal to them.
* Romantic Individuals: Appeal to the romantic side of users who are looking for expressive and sentimental gifts, such as flowers, personalized items, or romantic-themed presents. Highlight products that convey love and affection.
* Last-Minute Shoppers: Consider users who tend to leave gift shopping to the last minute. Offer same-day or express delivery options to cater to their needs, and ensure that the website is user-friendly with a straightforward checkout process.

### :round_pushpin: Site Goals

* Find the Perfect Gift: Users want to discover a thoughtful and appropriate gift for the occasion, whether it's a birthday, anniversary, wedding, or another celebration. The website should offer a wide variety of options for different tastes and preferences.
* Budget-Friendly Options: Many users have a budget in mind when shopping for gifts. The website should cater to users seeking budget-friendly options by providing filters, sorting options, and a range of products at various price points.
* Efficient Checkout Process: Users want a straightforward and secure checkout process. Simplifying the steps involved in placing an order contribute to a positive user experience.

### :round_pushpin: User stories

From the Epics, 23 User stories were developed. Each story was assigned a classification of Must-Have and Could-Have.
I will however revisit them at a later time for a redevelopment of the project. 

These are the user stories that were completed within the projects first release.

![Milestones1](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/EPIC%201.png)
![Milestones2](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/EPIC%202.png)
![Milestones3](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/EPIC%203.png)
![Milestones4](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/EPIC%204.png)

### :round_pushpin: The Scope Plane

**Features planned:**

* User Profile:
  * Users can Register, Login and Logout
  * Access their Profile that they can see their order history and their default address which they can update
  * They can have a personalised Wishlist
  * They can Rate Products
* Product Management (Owner) - Can create, read, update and delete products
* Other Users - Can read reviews and Purchase any product without need to login/Register
* Contact page with opening hours, frequently asked questions and a form that they can submit any queries
* Shopping bag list that they can see which products they are buying and that they can also upate the quantity or remove the product
* Checkout page that they can easily add they payment and address information
* Search menu bar that they can find an specific product
* Newsletter Marketing email that they can register to receive updates and latest deals

### :round_pushpin: Future Enhancements

There are several items of functionality that I would like to add in the future. 
The key areas I would like to add to the site in the future are:

* The ability for users to filter products by rating
* The ability for users to pay with apple pay and other types of payment
* The ability for users to login via social networks such as google or facebook
  
## :heavy_check_mark: Technologies

* Python
    * The following python modules were used on this project:
        * asgiref==3.7.2
        * boto3==1.29.3
        * botocore==1.32.3
        * dj-database-url==0.5.0
        * Django==3.2.22
        * django-allauth==0.41.0
        * django-countries==7.2.1
        * django-crispy-forms==1.14.0
        * django-storages==1.14.2
        * gunicorn==21.2.0
        * jmespath==1.0.1
        * oauthlib==3.2.2
        * Pillow==10.1.0
        * psycopg2==2.9.9
        * python3-openid==3.2.0
        * pytz==2023.3.post1
        * requests-oauthlib==1.3.1
        * s3transfer==0.7.0
        * sqlparse==0.4.4
        * stripe==7.4.0
        * urllib3==1.26.18

* Django
    * Django was used as the main python framework in the development of this project.
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Heroku Was used as the cloud based platform to deploy the site on.
* ElephantSQL - Postgres
    * ElephantSQL was used as the database for this project during development and in production.
* EWS
    * EWS was used to storage all the images and static files.   
* JavaScript
    * Custom JavaScript was utilised to set time for messages.
* Bootstrap 5.13
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.
* Stripe
    * Stripe was used to handle the payments and send the confirmation emails when completing a new purchase.  

## :heavy_check_mark: Existing Features

- __Initial Page__

    - Contains a nice background with an image button that sends customer to the list of products.

![Initial-Page](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/home_page.png)

- __List of Products__

    - Allow anyone to see the list of products, that can be filtered by categories on the navbar and sorted by price on the menu on the top right. They can also see the product's rating. Owners only, will have buttons that allow them to delete or update the products.

![List-of-Products](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/products_list.png)

- __View a Product__

    - Allow anyone to see the product details, ratings and also add the product to shopping bag. Logged in Users have extra benefits such as adding product to wishlist and rate the product. Owners only, will have buttons that allow them to delete or update the products.

![View-Product](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/product_view.png)
![Product-Review](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/product_review.png)
![Rating-Product](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/product_rating.png)

- __Shopping Bag__

    - Allow anyone to see their products on the shopping bag, they will be able to adjust the quantity and also to remove an item if they need.

![Shopping-Bag](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/shopping_bag.png)

- __Checkout__

    - Allow anyone to checkout their products from the shopping bag and confirm their address and payment details to submit their order.

![Checkout](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/check_out.png)

- __My Profile__

    - Allow logged in users to access their default address that they can update at any time and also see all their order history.

![My-Profile](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/my_profile.png)

- __Wishlist__

    - Allow logged in users to access their wishlist that they are able to remove the products as well if they want.

![Wishlist](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/wish_list.png)

- __Contact Us__

    - Allow anyone to access this page were they can check our contact information, frequently asked questions and also fill a form with any queries.

![Contact-Us](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/contact_us.png)

- __Product Management__

    - Store Owner only has access to this page, as they can create, edit and delete products.

![Product-Management](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/product_management.png)

- __Login__

    - A user can login on their account.

![Login](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/login_page.png)

- __Sign in__

    - Anyone can create an account.

![Sign-in](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/sign_in_page.png)

- __Logout__

    - A user can confirm if they want to logout before it gets logged out.

![Logout](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/signout_confirmation.png)

The useful support needed came from:

[Code Institute](https://codeinstitute.net/ie/)
[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
[GitHub - Markdown Guide](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
