[![Build Status](https://travis-ci.com/GannaSachkova/project4-heroku.svg?branch=master)](https://travis-ci.com/GannaSachkova/project4-heroku)
# Milestone Project 4 – Full Stack Development

**Ecommerce & Blog Web Application with User Authentication and Stripe Payments**
This Web App was built as a final project for the Code Institute's classroom bootcamp. It is a fictional ecommerce site built with Python's Django framework

This website consists of the following pages:

1. Home - it is the start page of the website
2. All Body Massage - page contains information about services
3. Face Massage - page contains information about services
4. Packages -  page contains information about services
5. Register - page contains register form
6. Log In - page contains a login form
7. Cart - page contains items the user would like to buy
8. Search - page contains search panel

## Table of Contents
- [Demo](#demo)
- [UX](#ux)
- [Design Choices](#design-choices)
- [Wireframes](#wireframes)
- [Features](#features)
- [Database Scheme](#database-scheme)
- [Database Design](#database-design)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


## Live Demo
A live version of the app is hosted [here:](https://project4-heroku.herokuapp.com/).
Project code is is available [here:](https://github.com/GannaSachkova/project4-heroku).


## UX
This project created as my fourth and last Milestone project at Code Institute. The project is a full-stack web application and it is an online shop where we can buy some spa services with secure payment. 


My goal in the design was to make it as easy as possible to access information on the site while striving for a minimalist design. So the website does this in a simple intuitive way with easy navigation, minimal fields. This application is user-friendly and interactive.
Details of the UX design is available in the wireframes folder. This folder contains web page sketch pages of the application.

The four dominant color on the page is grey, brown, green, orange and black letters.

Apps

Accounts
This app allows visitors to register an account, log in, view their profile (which confirms what User they are logged in or logged out). This allows the user to purchase services through the website and cart.

Cart
This allows visitors to view and adjust the services they have selected from the products page just before clicking "Checkout" before making a purchase. 

Purchased
purchased.html is rendered once the User has successfully completed a purchase through checkout.html. A pop-up message is displayed saying "You have successfully paid"

Checkout
This allows visitors to purchase some services that were added to their Cart. Users can adjust the quantity of each service they have selected. Before purchasing they fill out their personal and payment details to buy that via Stripe.

Products
This app displays all services from the Category the User selected in categories. Each service is displayed on its own panel-card which has the Service Image, Name, short description, price and "View Product" button. Pressing this button opens up a modal that has the same information and an "Add to Cart" button attached to a "Quantity" selector. "Add to Cart" will add the chosen amount of services to the User's Cart and then redirect them to the Categories products.html page. It also has a "Go Back" button which will take the User back one page. 

Search
This app allows users to search the website

## Design Choices
###Colour Scheme
I'm a big fan of brown colours, so as you can see it. And I suggested that it is a good reason to use it as the main color because brown color suggests neatness, openness, approachability, and friendliness. Also, it relates well to nature, wholesome food. 
The main colour was taken off the main page of the website.   A colour palette was then found using [coolors](https://coolors.co/).  There were used 5 main colours.

###Styling
Styling was done on the principle of mobile first. As most Users these day access sites from their phone, this site needed to be friendly for them.

I chose to keep the collapsed menu all the way up till the large screen otherwise the screen seemed too busy and this way it keeps the visual overload to a minimum.

## Wireframes

The following [wireframe](https://github.com/GannaSachkova/project4-heroku/tree/master/wireframes) sketches were created using [Moqups](https://moqups.com/) to design the project layout options for desktop displays.



## Features
#### Existing Features 
•	User is able to login or register by clicking "login/register" on the navbar and filling out the form.
•	The profile allows the user to view their details when signed into the app
•	Navbar allows users to quickly move around the app 
•	User is able to view all services by clicking the necessary button on the navbar
•	The user is able to put a product by clicking "add to cart" and checking out.
•	User is able to buy a product by clicking "Checkout"
•	Images - Django ImageField attributes are used to store images in models. Images are hosted on AWS3 Bucket to allow hosting on cloud servers. 


####  Future Features 
Time was gone too fast and unfortunately, there are many more features I would like to include to enhance the appeal and useability of the app.
•	registered users would have the function to access their own orders through profile;
•   a user review section would be a useful feature for new visitors to the site;
•   adding and changing amount Items for order via the items page or on checkout; 
•   add more content for the end-user to see on their Profile page; 
•   email functionality: sending registration emails, sign in with just email;
•   need to create a contact form for visitors to fill in and send an email to the site owner; 
•   need to create the "About Us "page.



## Database Schema
I chose to use Database Design  website beacose  it is a simple online tool to quickly draw database diagrams by typing.

![Database Design](https://anna-django-shop.s3-eu-west-1.amazonaws.com/static/img/DB-Diagram.png)



## Database Design

Relationships between tables are as follows:

User and Order- one to many relationship as one user in the user table can be associated with many orders;

Services and Order_Service - one to many relationship as one service in the Service table can be associated with many serviced orders;

Order_Service and Order - one to many relationships as an Order_Service can be ordered by many orders.

## Technologies Used 
The website is designed using following technologies:

### Programming languages
-	**HTML** - the project used HTML to define structure and layout of the web page;
-	**CSS** - the project used CSS stylesheets to specify style of the web document elements;
-	**JavaScript** - the project used JavaScript to implement Maps JavaScript API and customize it.
-	**Python** - the project back-end functions are written using Python. Flask and Python is used to build route functions.

### Libraries
-	[Font Awesome](https://fontawesome.com/v4.7.0/) - Font Awesome bars icon for menu on mobile devices was used in the project, as well as icons for social media links;
-	[jQuery](https://code.jquery.com/jquery-3.4.1.min.js) - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. ### Frameworks & Extensions
-	[Django]( https://www.djangoproject.com/) – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
-	[Bootstrap](https://getbootstrap.com/) – Bootstrap is a web framework that focuses on simplifying the development of informative web pages


### Database
-	[QuickDBD](https://www.quickdatabasediagrams.com/) – Quick Database Diagrams (QuickDBD) is a simple online tool to quickly draw database diagrams by typing.

### Others
-	[GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git;

-	[Gitpod](www.gitpod.io) - One-click ready-to-code development environments for GitHub;

-	[Heroku](www.heroku.com) - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps — we're the fastest way to go from idea to URL, bypassing all those infrastructure headaches;

-	[Moqups](https://moqups.com/) - Online tool that was used to create wireframes.AWS S3 – is a service offered by Amazon Web Services that provides object storage through a web service interface.

-	[Travis-CI](https://travis-ci.org/) – Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub.  



## Testing
I conducted testing across different platforms and web browsers in order to make sure the website looked great across each one. I also asked friends and family to test across their own devices and to give me honest opinions and feedback.

Platforms:

* Samsung Galaxy 8
    * Google Chrome
    * Firefox
    * Samsung web browser
* Ubuntu 18.0
    * Google Chrome
    * Firefox
* Windows 7
    * Google Chrome
    * Firefox

### Browser Testing
Chrome -The project was developed using Chrome as the serving site. All features were running optimally when tested.

Firefox - All the features were working.

### Device testing
This was tested on multiple devices, including Iphone, Ipad, Android, tablets and phones. Working as expected on all devices. No issues reported.

Travis was used to scan packages and libraries for bugs and anything that might damage travis or the server, to ensure that that server is safe and free of code that might be dangerous. All tests were passed, see the green build passing button in top of the README file and see pictures below: 

![Travis](https://anna-django-shop.s3-eu-west-1.amazonaws.com/static/img/travis.png)

Also checked my Stripe dashboard for succesful payments. See picture below:

![Stripe](https://anna-django-shop.s3-eu-west-1.amazonaws.com/static/img/stripe.png)


#### Running the tests
Automated tests can be viewed in the tests.py file within the separate Apps. To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:
$ [python manage.py test +app name]



#### Resources & Tools Used for Testing
**HTML**  - [W3 HTML Validator](https://validator.w3.org/)

**CSS**   - [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)

**JSHint** - [JSHint](https://jshint.com/) - JSHint is a community-driven tool that detects errors and potential problems in JavaScript code.

**online Beautifier** - [freeformatter.com](https://www.freeformatter.com) and [CSS Formatter](https://www.cleancss.com)

**Responsinator** - [Responsinator](https://www.responsinator.com/) - to check the responsiveness of my site on various devices.

**Responsive Checker** - [Responsive Checker](https://www.websiteplanet.com/webtools/responsive-checker/) - Online tool was used to display the project on various devices;

In addition, this project was tested for responsiveness using the Chrome Developer Tools.



## Deployment

The project has been deployed to both Github and Heroku with media and static files on AWS S3. 

Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows: [https://github.com/GannaSachkova/project4-heroku](https://github.com/GannaSachkova/project4-heroku)
Heroku App Location is as follows: [https://project4-heroku.herokuapp.com/](https://project4-heroku.herokuapp.com/)


The web application was built and tested locally and once near completion it was pushed to Heroku by linking the master git branch from the remote Github repository to the app created in Heroku. All changes pushed to the master Github branch automatically pushed to the production application in Heroku. 

To ensure additional features and testing was conducted before being pushed to the production environment in Heroku. I created a development branch in git. All changes were pushed with commits first to the development branch then once happy merged into the master branch. Then as mentioned this would automatically push to the production environment.

There are two differences between the development environment and the production environment. 

1. Development environment uses SQLite for its database where the production environment uses PostgreSQL.
2. Production environment DEBUG is set to False. Development DEBUG is set to TRUE.

Functions have been written in the setting.py file to recognise which environment the application is running on.

### How to deploy the code locally

If you wish to run this code locally then please follow the instructions below.

1. Download the code from the Github repository at [https://github.com/GannaSachkova/project4-heroku](https://github.com/GannaSachkova/project4-heroku).
2. Click on Clone or *download* then *Download ZIP*. This will download the code into a ZIP folder locally on your computer.
3. Uncompress the ZIP folder.
4. Create a virtual environment. Tutorial of how to create a virtual environment can be found here. [https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
5. Activate the virtual environment.
6. Install the necessary Python packages in the requirements.txt file.
    * `pip3 install -r requirements.txt`
7. Set environment variables. On MacOS and Linux add the following code to your /.bashrc or /.bash_profile files. For Windows, create a new folder within the top level of this project and create a file to add the code in.
```bash
# Environment variables for Django projects
export DB_USER=<DB admin username>
export DB_USER_PASSWORD=<DB user password>
export EMAIL_HOST_USER=<email address>
export EMAIL_HOST_PASSWORD=<email password>
export SECRET_KEY=<secret key>
export STRIPE_PUBLISHABLE=<stripe publishable key>
export STRIPE_SECRET=<stripe secret key>
export AWS_STORAGE_BUCKET_NAME=<AWS bucket name>
export AWS_ACCESS_KEY_ID=<AWS access key ID>
export AWS_SECRET_ACCESS_KEY=<AWD secret access key>
export CELERY_BROKER_URL=<celery broker URL>
export DEBUG=True
```
8. Create an AWS account by following these instructions. [https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
9. Create a AWS s3 bucket using these instructions. Make sure your bucket is set to public under the permissions tab. [https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)#### Databases / Static Files
When running locally, SQLite database was used & static and media files were stored locally. When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.

### Deploy to Heroku

This project was deployed to Heroku and uses Heroku for its production environment. Instructions are below on how to deploy this web application to a production environment in Heroku.

**Git must be installed onto your computer. Instructions for installing Git can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

**Heroku CLI must be installed in order to deploy to Heroku using these instructions. Please follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli) to download and install Heroku CLI. 

1. Open up Heroku and navigate to your dashboard.
2. Select 'New' > 'Create New App' and fill out the details required then hit 'Create App'.
3. Select 'Settings' > 'Reveal Config Vars'
    * Enter in the same environment variables that are in step 7 of deploying code locally.
4. Download the code from the Github repository [here](https://github.com/AnthonyNicklin/newage-auctions)
5. Click on Clone or *download* then *Download ZIP*. This will download the code into a ZIP folder locally on your computer.
6. Uncompress the ZIP folder.
7. Open up a terminal or cmd prompt and login into Heroku CLI.
    * `heroku login`
8. Check the app is present.
    * `heroku apps`
9. A Proflice has already been created for this project but make sure it is present. If for some reason it is not then follow the steps below to create one.
    * Procfile
        * In a terminal make sure you are in the root directory of the project then run `touch Profile`.
        * Add the following code to the Procfile 
        ```
       web: gunicorn project4_heroku.wsgi:application
        ```
10. Add a new git remote for Heroku.
    * `git remote add heroku git@heroku.comYOUR_APP_NAME.git`
11. Push to Heroku.
    * `git push heroku master`
12. Give Heroku a few minutes to get it all set up and then check the activity logs under the Activity tab in your Heroku dashboard.
13. Once the build is complete click on 'Open App' top right to see Newage Auctions in action.

### PostgreSQL on Heroku
 
To install and set up a PostgreSQL database follow the well document instructions provided by Heroku at [https://devcenter.heroku.com/articles/heroku-postgresql](https://devcenter.heroku.com/articles/heroku-postgresql).

#### GitPod 
If you wish to run this code through gitpod in CLI you lust need type command "run" because I added alias to "gitpod.yml": alias run="python3 /workspace/project4-heroku/manage.py runserver 0.0.0.0:8080"' >> ~/.bashrc&&source ~/.bashrc . It  allows to run  the project  easely from command line.


## Credits

### Content
•	The apps products, checkout, cart, and accounts were taken from the [E-commerce Mini Project](https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce) and customized where possible to suit my project.
•	Services and pictures for website categories have been sources from [Google](https://www.google.ie/).
•	Wallpaper background obtained from [Google](https://www.google.ie/).

### Contact 
•	Created by [Ganna Sachkova]( (mailto:dorogaya1810@gmail.com).

### Acknowledgements 
•	Many thanks to my mentor Maranatha Ilesanmi  for all the support and advice he has given during the course of this project
•	Thanks to my school Code Institute for creating a great Full-Stack Developer Education.

*All materials and content in this project are solely for educational purposes.*


