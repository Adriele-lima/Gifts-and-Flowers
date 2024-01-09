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

## :heavy_check_mark: Testing

### :round_pushpin: RESPONSIVENESS:

- The deployed application was tested on multiple devices to check for responsiveness issues. The bootstrap classes were used to be as responsive as possible.

![Responsive](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/responsive.png)

### :round_pushpin: BROWSER COMPABILITY TESTING:

The deployed project was tested on multiple browsers to check for compatibility issues and works as expected.

- __Photo of Microsoft Edge:__
      
![Edge](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/edge.png)

- __Photo of Firefox:__

![Firefox](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/mozila.png)
  
- __Photo of Mobile:__

![Mobile](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/mobile.png)


### :round_pushpin: LIGHTHOUSE

The deployed project was tested using the Lighthouse Audit tool to check for any major issues.

![Light House](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/lighthouse.png)


### :round_pushpin: Agile and Milestone

![Agile](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/agile.png)

![Milestones](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/milestones.png)

### :round_pushpin: Bugs

:x: One bug found when testing the deployed site. As I created more models after I deployed the website, when I tested my contact us form, it was giving an error as I didn't have the env file and the migrations was only done on my local base.

:white_check_mark: After I add the env file with the postgres Database and run the migrations again, the deployed website was updated with the new models and the form started to work.

### :round_pushpin: CODE VALIDATION:

### :round_pushpin: HTML

[HTML Validator](https://validator.w3.org/nu/) to validate all HTML files. The result for each page is listed below:

- __Home page__

:x: On home page I found some simple errors:
 
![Html_home_error1_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-errors-home.png)

![Html_home_error2_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-errors-home2.png)

:white_check_mark: All resolved by removing some text that wasn't needed and some items not allowed.

![Html_home page_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-home.png)

- __View list of products__

:white_check_mark: No errors found.

![Html_view_list_of_products_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-products.png)

- __Product View__

:white_check_mark: No errors found.

![Html_product_view_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-product-view.png)

- __Product Management__

:white_check_mark: No errors found, only one info that I couldn't find to fix.

[Html_product_management_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-product-management.png)

- __Shopping Bag__

:white_check_mark: No errors found.

!Html_shopping_bag_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-bag.png)

- __Checkout__

:white_check_mark: No errors found.

![Html_checkout_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-checkout.png)

- __Contact Us__

:x: On contact page I found some simple errors:

![Html_contact_error1_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-errors-contact1.png)
![Html_contact_error2_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-errors-contact2.png)

:white_check_mark: All resolved by removing some duplicated IDs and the other ones were fixed on the base template.

![Html_contact_us_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-contact-us.png)

- __Profile__

:white_check_mark: No errors found, only one info that I couldn't find to fix.

![Html_profile_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-my-profile.png)

- __Wishlist__

:white_check_mark: No errors found.

![Html_wishlist_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/html-wishlist.png)

### :round_pushpin: CSS

[The CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS file.
 
:white_check_mark: No errors found.

![CSS_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/css-test.png)

### :round_pushpin: JAVASCRIPT

[The JShint Validator](https://jshint.com/) was used to validate the JavaScript file.

- __Add Product__

:white_check_mark: No errors found.

![Javascript_add_product_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/javascript-add-product.png)

- __Edit Product__

:white_check_mark: No errors found.

![Javascript_edit_productt_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/javascript-edit-product.png)

- __Products__

:white_check_mark: No errors found.

![Javascript_products_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/javascript-products.png)

- __View Prduct__

:white_check_mark: No errors found.

![Javascript_view_product_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/javascript-view-product.png)

- __Shopping Bag__

:white_check_mark: No errors found.

![Javascript_shopping_bag_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/javascript-bag.png)

- __Checkout__

:white_check_mark: No errors found.

![Javascript_checkout_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/javascript-checkout.png)

### :round_pushpin: PYTHON:

[The Code Institute Python Linterwas](https://pep8ci.herokuapp.com/) was used to validate all Python files.

- __E-commerce - Settings__

:white_check_mark: No errors found.

![Python_settings_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-ecommerce-settings.png)

- __Bag - Views__

:white_check_mark: No errors found.

![Python_bag_views_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-bag-views.png)

- __Checkout - Forms__

:white_check_mark: No errors found.

![Python_checkout_forms_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-checkout-forms.png)

- __Checkout - Models__

:white_check_mark: No errors found.

![Python_checkout_models_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-checkout-models.png)

- __Checkout - Views__

:white_check_mark: No errors found.

![Python_checkout_views_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-checkout-views.png)

- __Contact us - Forms__

:white_check_mark: No errors found.

![Python_contact_forms_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-contact-us-forms.png)

- __Contact us - Models__

:white_check_mark: No errors found.

![Python_contact_models_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-contact-us-models.png)

- __Contact us - Views__

:white_check_mark: No errors found.

![Python_contact_views_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-contact-us-views.png)

- __Home - Views__

:white_check_mark: No errors found.

![Python_home_views_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-home-views.png)

- __Products - Forms__

:white_check_mark: No errors found.

![Python_products_forms_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-products-forms.png)

- __Products - Models__

:white_check_mark: No errors found.

![Python_products_models_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-profiles-models.png)

- __Products - Views__

:white_check_mark: No errors found.

![Python_products_views_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-products-views.png)

- __Profiles - Forms__

:white_check_mark: No errors found.

![Python_profiles_forms_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-profiles-forms.png)

- __Profiles - Models__

:white_check_mark: No errors found.

![Python_profiles_models_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-profiles-models.png)

- __Profiles - Views__

:white_check_mark: No errors found.

![Python_profiles_views_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-profiles-views.png)

- __Wishlist - Views__

:white_check_mark: No errors found.

![Python_wishlist_views_test](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/python-wishlist-views.png)

## :heavy_check_mark: Credits

The useful support needed came from:

[Code Institute](https://codeinstitute.net/ie/)
[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
[GitHub - Markdown Guide](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
