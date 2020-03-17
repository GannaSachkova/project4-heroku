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
- [Wireframes](#wireframes)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

<a name="demo"/>

## Live Demo
A live version of the app is hosted [here: ](https://project4-heroku.herokuapp.com/)
Project code is is available [here: ](https://github.com/GannaSachkova/project4-heroku)

<a name="ux"/>

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


<a name="wireframes"/>

## Wireframes

The following [wireframe](https://github.com/GannaSachkova/project4-heroku/tree/master/wireframes) sketches were created using [Moqups](https://moqups.com/) to design the project layout options for desktop displays.

<a name="features"/>

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
•	**Reviews** - Try to allow user leave a review on purchased product


<a name="technologies-used"/>

## Technologies Used 
The website is designed using following technologies:

### Programming languages
-	**HTML** - the project used HTML to define structure and layout of the web page;
-	**CSS** - the project used CSS stylesheets to specify style of the web document elements;
-	**JavaScript** - the project used JavaScript to implement Maps JavaScript API and customize it.
-	**Python** - the project back-end functions are written using Python. Flask and Python is used to build route functions;

### Libraries
-	[Font Awesome](https://fontawesome.com/v4.7.0/) - Font Awesome bars icon for menu on mobile devices was used in the project, as well as icons for social media links;
-	[jQuery](https://code.jquery.com/jquery-3.4.1.min.js) - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. ### Frameworks & Extensions
-	[Django]( https://www.djangoproject.com/) – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
-	[Bootstrap](https://getbootstrap.com/ – Bootstrap is a web framework that focuses on simplifying the development of informative web pages



### Database
-	[PostgresSQL]( https://www.postgresql.org/) – is a powerful, open source object-relational database system with active development that has earned it a strong reputation for reliability, feature robustness, and performance.

### Others
-	[GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git;

-	[Gitpod](www.gitpod.io) - One-click ready-to-code development environments for GitHub;

-	[Heroku](www.heroku.com) - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps — we're the fastest way to go from idea to URL, bypassing all those infrastructure headaches;

-	[Am I Responsive](http://ami.responsivedesign.is/) - Online tool was used to display the project on various devices;

-	[Moqups](https://moqups.com/) - Online tool that was used to create wireframes.AWS S3 – is a service offered by Amazon Web Services that provides object storage through a web service interface.

-	[Travis-CI](https://travis-ci.org/) – Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub.  

<a name="testing"/>

### Testing
#### Running the tests
Automated tests can be viewed in the tests.py file within the separate Apps. To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:
$ python manage.py test <app name>

#### Resources & Tools Used for Testing
**HTML**  - [W3 HTML Validator](https://validator.w3.org/)

**CSS**   - [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)

**JSHint** - [JSHint](https://jshint.com/) - JSHint is a community-driven tool that detects errors and potential problems in JavaScript code.

**online Beautifier** - [freeformatter.com](https://www.freeformatter.com) and [CSS Formatter](https://www.cleancss.com)

**Responsinator** - [Responsinator](https://www.responsinator.com/) - to check the responsiveness of my site on various devices.

In addition, this project was tested for responsiveness using the Chrome Developer Tools.


<a name="deployment "/>

## Deployment

The project has been deployed to both Github and Heroku with media and static files on AWS S3. 

Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows: [https://github.com/GannaSachkova/project4-heroku](https://github.com/GannaSachkova/project4-heroku)
Heroku App Location is as follows: [https://project4-heroku.herokuapp.com/](https://project4-heroku.herokuapp.com/)


### GitHub Deployment
Created a new repositories on Github where the project will be deployed unto at each commit. At first, use a git remote command to link project with new repo. Then use the git push -u origin master command to push codes and every change into new repo
Using the CLI in terminal to call git init to start git initialization on the project. This allows a file/files to be added to the Github repo by calling a git add command. Then any added file/files is being commited with a git commit -m "commit message" command. Afterwards, the file is been pushed with git push where Github username + password is required. Once successful, code will be deployed into your repo and git status command should indicate branch tree clean.

### AWS3 Deployment Process
Created a new Amazon account and connect to amazon service [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) account are cloud based serve where the project media and staicfiles will be stored unto. At first, we locate S3 on amazon service then we create a bucket. While creating the bucket on S3, the note that public access must be all switched off to allow access for users.
Once we've created the bucket, we now can now click on it's properties and enable the Static Website Hosting option, so it can serve the purpose of hosting our static files, you will need to imput an index.html and error.html before saving. Then we go into the created bucket Permissions and click into CORS configuration, this part already have a prefilled default config, All that is needed is just to write the default code and save the config.
Then we go into the bucket policy to allows access to the contents across all web and inside this we will put in here some code including arn address displayed at the top of the heading. Then we go into amazon [IAM]( https://aws.amazon.com/iam/) to allow identity and access management of our stored files and folder. In the IAM service, we add a new group for our application and then we set the policies to ALL Then it generates a downlaodable zip file containing ID and KEY for us to use for the newly added group. This ID and KEY as to be stored in an environment variable.
This allows us to into our terminal window and install some settings Boto3 Django Storages
The Django Storages is passed into the installed apps in settings and also a custom_storage file is created to store credentials in environment variable. And once everything looks fine we can run python3 manage.py collectstatic. This will collect all the static files in our app including any changes that is made. N.B this command has to be run in the development(local) environment each time a change is been made in the static files/folder And your folder and files should display in your *AWS3 BUCKETS

### Heroku Deployment
Created a new app on Heroku where the app is hosted live. At first, to allow Heroku locate application we login into the CLI using ** heroku login -i** command. You will be requested to imput username and password for Heroku account. After which you can request Heroku Apps via CLI.
Knowing the apps you need to pass deployment into then we can use heroku git:remote -a to allow Git automatically update deployment in Heroku. Once this has been remotely passed . To host the app unto heroku pass the IP and PORT config to match the route main config.
To allow PostgresSQL, we have to go into our newly created app and click into resources inside here you can type PostgresSQL and add as an add on, it should prompt up on your screen choose the hobby dev free and click on provision. Once you allow PostgresSQL it will generate a DATABASE_URL in the heroku settings.
Now we need to install in production terminal dj-database-url and psycopg2 Then we run a migrate to to update our new PostgresSQL database and since this is new in Heroku, all data imputed will be erased. Which means we need to createsuperuser from terminal and add our contents again, Our new production database is ready. So we can rebuild all our projects again.
To allow git to push to heroku the command git push heroku master must be called for a final push. For a succefull and healthy push it is best adviced to have the requirement.txt and Procfile files installed or updated. Most especially for requirement.txt file which gave me a lot of challenges, it requires to be updated along with any installed packages so it can depoly successfully, i.e Flask packages.

#### Databases / Static Files
When running locally, SQLite database was used & static and media files were stored locally. When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.

#### GitPod 
I added alias to "gitpod.yml": alias run="python3 /workspace/project4-heroku/manage.py runserver 0.0.0.0:8080"' >> ~/.bashrc&&source ~/.bashrc . It  allows to run  the project  easely from command line.

<a name="credits "/>

## Credits

### Content
•	The apps products, checkout, cart, and accounts were taken from the [E-commerce Mini Project](https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce) and customized where possible to suit my project.
•	Services and pictures for website categories have been sources from [Google](https://www.google.ie/).
•	Wallpaper background obtained from [Google](https://www.google.ie/).

### Acknowledgements 
•	All materials and content in this project are solely for educational purposes.

### Contact 
•	Created by [Ganna Sachkova]( (mailto:dorogaya1810@gmail.com).
