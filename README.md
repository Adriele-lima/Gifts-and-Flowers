# :blossom::gift::tulip: Gifts and Flowers

Welcome to [Gifts and Flowers!](https://gifts-and-flowers-6d75002e0957.herokuapp.com/) This is a e-commerce web application designed for people who loves to gift and surprise their loved ones!'

## Table of Contents

* [UX Design](#heavy_check_mark-ux-design)
    * [The Strategy Plane](#round_pushpin-the-strategy-plane)
    * [The Sites Ideal User](#round_pushpin-the-sites-ideal-user)
    * [Site Goals](#round_pushpin-site-goals)
    * [Facebook Page](#round_pushpin-facebook-page)
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

### :round_pushpin: Facebook Page

* Follow us on our [Facebook Page](https://www.facebook.com/gifts.and.flowers.2024/)

![Facebook](https://github.com/Adriele-lima/Gifts-and-Flowers/blob/main/static/images/facebook.png)

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

## :heavy_check_mark: Deployment

### :round_pushpin: How to Fork

To fork the repository:

1. Log in (or sign up) to Github.

2. Go to the repository for this project.

3. Click the Fork button in the top right corner.
   
### :round_pushpin: How to deploy

How to deploy the repository:

1. On terminal:

   - Install all the necessary applications:
    
       - Install dj_database_url and psycopg2:
   
               pip3 install dj_database_url==0.5.0 psycopg2
   
       - Install Django and gunicorn:
   
               pip3 install 'django<4' gunicorn

      - Install storages package:
    
     		      pip3 install django-storages

       - Create requirements file:
   
               pip3 freeze --local > requirements.txt
   
2. Create the new Database:

   - In your settings.py file, import dj_database_url underneath the import for os:
     
      	   import os
      	   import dj_database_url

   - Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated:
     
            # DATABASES = {
      	   #     'default': {
      	   #         'ENGINE': 'django.db.backends.sqlite3',
      	   #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      	   #     }
      	   # }
           
      	   DATABASES = {
      	   'default': dj_database_url.parse('your-database-url-here')
      	   }
   **DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations. We will remove it in a moment.**

   - In the terminal, run the showmigrations command to confirm you are connected to the external database:

           python3 manage.py showmigrations
   - If you are, you should see a list of all migrations, but none of them are checked off.

   - Migrate your database models to your new database:

           python3 manage.py migrate

   - Load in the fixtures. Please note the order is very important here. We need to load categories first:

           python3 manage.py loaddata categories

   - Then products, as the products require a category to be set:

           python3 manage.py loaddata products

   - Create a superuser for your new database:

           python3 manage.py createsuperuser

   - Follow the steps to create a your superuser username and password. The email address can be left blank.
   - Finally, to prevent exposing our database when we push to GitHub, your DATABASE in the settings.py file should look like this:

            if 'DATABASE_URL' in os.environ:
             DATABASES = {
              'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
             }
            else:
              DATABASES = {
                 'default': {
                     'ENGINE': 'django.db.backends.sqlite3',
                     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                 }
             }


3.	On [Elephantsql](https://customer.elephantsql.com/login):
     - Log in/or create an account to access your ElephantSQL account
     - Click “Create New Instance”
     - Set up your plan:
        - Give your plan a Name (this is commonly the name of the project)
        - Select the Tiny Turtle (Free) plan
        - You can leave the Tags field blank
     - Click “Select Region”
     - Click “Review”
     - Return to the ElephantSQL dashboard and click on the database instance name for this project
     - Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://
  
4. On [AWS - Amazon](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fs3.console.aws.amazon.com%2Fs3%2Fhome%3Fregion%3Deu-north-1%26state%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fs3&forceMobileApp=0&code_challenge=3nuR8Bl59qVf9AK1xcJXvIq-d1MAld6tTuy2SuRGdXI&code_challenge_method=SHA-256):
      - Log in/or create an account to access your AWS account
      - On AWS page go to S3
      - Click on create new bucket
      - Create a name (best to be the same as Heroku) and select region.
      - Select ACLs Enabled and Bucket owner preferred
      - Deselect all "Block all puclic access"
      - Confirm the yellow alert
      - Click on create bucket
      - Click on the new bucket
      - Click on the Properties tab
      - Scroll to the bottom of the page and on static website hosting click on edit
      - Select “enable” static website hosting, then add the text “index.html” and “error.html” to index document
      - Save changes
      - Still on bucket, click on permissions tab
      - Scroll to the bottom of the page, on CORS Cross-origin resource sharing (CORS), click on edit and paste the below then save.

                  [
              {
                  "AllowedHeaders": [
                      "Authorization"
                  ],
                  "AllowedMethods": [
                      "GET"
                  ],
                  "AllowedOrigins": [
                      "*"
                  ],
                  "ExposeHeaders": []
              }
            ]
      
      - On Bucket policy click on edit and click o policy generator
      - It will open a new tap, and then needs to fill the below:
         - Type of policy: S3 Bucket policy
         - Principal: *
         - Action: Get object
         - ARN: Copy from the AWS page on bucket policy
      - Click add statement and then generate policy
      - Copy the policy
      - Paste the policy on the bucket page, add “/*” at the end of resource link and save.
      - On Access control list (ACL), click on edit and select everyone (public access)
      - Select the “I understand box” and save.
      - Now, search for IAM and click on the dashboard click on User groups
      - Give it a name and press create group
      - On the dashboard click on policies and create policy
      - Click on JSON then on import policy
      - Write “S3” on the search menu and select AmazonS3FullAccess then click on Import policy
      - Add the ARN (From bucket page) on the resource twice but on the second link add “/*” and the click on next
      - Give the policy a name and a description and click on create policy
      - Go back to User groups, click on the group you created and then click on permissions, add permissions and attach policies.
      - Find you policy by the name and attach
      - On the dashboard click on users.
      - Create a new user
      - Give the user a name and click next
      - Select the group and click next and create user
      - On the users menu, click on the user you created
      - Click on create access key
      - Select application running on an AWS compute service, click on the box “I understand” and click next
      - Leave the description blank and click on create access key
      - Download the CSV file
      - On the CSV file from AWS you will find the SECRET KEY and ACCESS KEY, that needs to be added on Heroku as well the USE AWS set to TRUE.

5. On [Stripe](https://stripe.com/ie):
     
     - Log in/or create an account to access your Stripe account
     - On your dashboard you will have your test API key that you will need to add on your Heroku.

6.	On [Heroku](https://id.heroku.com/login):
     - Login/or create an account to access your Heroku account
     - Create new Heroku App
     - Open the settings tab
     - Click Reveal Config Vars
         - Add a Config Var called DATABASE_URL: The value should be the ElephantSQL database url you copied from step 3.
         - Add a Config Var called MY_SECRET_KEY: The value should be of your choice, but keep ot secret. (Should be the same as set on your env.py file)
         - Add a config Var called AWS_ACCESS_KEY_ID: The value should be the AWS access key from step 4.
         - Add a config Var called AWS_SECRET_ACCESS_KEY: The value should be the AWS secret access key from step 4.
         - Add a config Var called STRIPE_PUBLIC_KEY: The value should be the Stripe public key from step 5.
         - Add a config Var called STRIPE_SECRET_KEY: The value should be the Stripe secret key from step 5.
         - Add a config Var called USE_AWS: the value should be "True"

7. On your settings.py:

     - Reference env.py by adding on the top:
       
           import os
           import dj_database_url
           if os.path.isfile("env.py"):
           import env

     - Remove the insecure secret key (if any) and replace with:
       
           SECRET_KEY = os.environ.get('SECRET_KEY')
            
     - Add new DATABASES Section:
  
           if 'DATABASE_URL' in os.environ:
             DATABASES = {
              'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
             }
            else:
              DATABASES = {
                 'default': {
                     'ENGINE': 'django.db.backends.sqlite3',
                     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                 }
             }
    
      - Add ‘storages’ to installed apps:
  
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'django.contrib.sites',
                'allauth',
                'allauth.account',
                'allauth.socialaccount',
                'home',
                'products',
                'bag',
                'checkout',
                'profiles',
            
                # Other
                'crispy_forms',
                'storages',

     - Add AWS section for the static files and media:
  
             if 'USE_AWS' in os.environ:
                # Cache control
                AWS_S3_OBJECT_PARAMETERS = {
                    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                    'CacheControl': 'max-age=94608000',
                }
            
                # Bucket Config
                AWS_STORAGE_BUCKET_NAME = 'gifts-and-flowers-6d75002e0957'
                AWS_S3_REGION_NAME = 'eu-west-1'
                AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
                AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
                AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
            
                # Static and media files
                STATICFILES_STORAGE = 'custom_storages.StaticStorage'
                STATICFILES_LOCATION = 'static'
                DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
                MEDIAFILES_LOCATION = 'media'
            
                # Override static and media URLs in production
                STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
                 - Tell Django to use Cloudinary to store media and static files:
     
               STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
               STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
               STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
               
               MEDIA_URL = '/media/'
               DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

     - Link file to the templates directory in Heroku:
  
            TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

     - Change the templates directory to TEMPLATES_DIR:
  
           TEMPLATES = [
                {
                   …,
                    'DIRS': [TEMPLATES_DIR],
                   …,
                        ],
                    },
                },
            ]
     - Add Heroku Hostname to ALLOWED_HOSTS:

           ALLOWED_HOSTS = ["**PROJ_NAME**.herokuapp.com", "**YOUR_HOSTNAME**"]

8. Create a Procfile on the top level directory, and add the code below inside:

        web: gunicorn **PROJ_NAME**.wsgi

9. Create the env.py file on the top level directory, and add the secret keys:

       import os
   
         os.environ['DATABASE_URL'] = 'your postgres key'
         
         os.environ['SECRET_KEY'] = 'your secret key7'
         
         os.environ['AWS_ACCESS_KEY_ID'] = 'AWS key'
         
         os.environ['AWS_SECRET_ACCESS_KEY'] = 'AWS secret key'
             
         os.environ['STRIPE_PUBLIC_KEY'] = 'your stripe public key'
         
         os.environ['STRIPE_SECRET_KEY'] = 'stripe secret key'
         
         os.environ['USE_AWS'] = 'True'
       
    
10. Make sure you have debug set to False on Settings.py:

        DEBUG = False

11. Commit your changes to github:

        git add .
        git commit -m "YOUR MESSAGE"
        git push

12. On Heroku, you can manually deploy it our set up an automatic deployment.
   
13. The live link can be found here [Gifts and Flowers](https://gifts-and-flowers-6d75002e0957.herokuapp.com/)

## :heavy_check_mark: Credits

The useful support needed came from:

[Code Institute](https://codeinstitute.net/ie/)
[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
[GitHub - Markdown Guide](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
