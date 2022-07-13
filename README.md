# Saran Collection

This project is part of my Code Institute Full Stack Software Development studies, specifically the Full Stack Frameworks with Django module. The objective for this milestone project is to plan, design and develop a project with all the functionalities to work as an actual e-commerce website. This project is an e-commerce store for fictional fashion apparel company that specialises in women and men clothing. 

[View live version of website via Heroku](https://saran-collection.herokuapp.com/)

![Mockup image](/documentation/images/mockup.png)

<br>
<hr>

<a></a>
## Table of Contents 
* [UX](#ux)
    * [User Persona](#user-persona)
    * [User Goals](#user-goals) 
    * [Site Owners Goals](#site-owners-goals) 
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [User Stories](#user-stories)
    * [Log In Sign Up Flow](#log-in-sign-up-flow)
* [UI Design](#ui-design) 
    * [Font](#font)
    * [Colour Scheme](#colour-scheme)
    * [Icons](#icons)
    * [Structure](#structure)
* [Wireframes](#wireframes)
* [Data Structure](#data-structure)
* [Existing Features](#existing-features)
* [Future Features](#future-features)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries](#libraries)
    * [Tools](#tools)
    * [Design](#design)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

<br>
<hr>

<a name="ux"></a>
## **UX**
<a></a>
### **User Persona**
This website project will target users who are interested in purchasing fashion products. The primary focus is on providing an easy to navigate and responsive e-commerce website that allows users to easily purchase products. 

<a></a>
### **User Goals**
- View featured products on the website.
- View, search and be able to easily purchase products easily and securely.
- The e-commerce store has to work well on all kinds of devices like mobile phones, tablets and desktops.

<a></a>
### **Site Owners Goals**
- View, add, edit, search, delete products.
- Have an easy and effective user flow so that the user can, without obstacles, successfully purchase so that the conversion rate is high, shopping bag abandonment rate is low and the number of returning customers increases.

<a></a>
### **User Requirements and Expectations**
#### **Requirements**
- Easy to navigate by using the navigation menu.
- Relevant content for each product category.
- Appealing visual elements.
- Easy way to search and sort products that are relevant to the user.

#### **Expectations**
- When clicking on links (resource and social media links), expect the page to open in a separate browser.
- Expect that the navigation links work properly to take the user where they intended to go.
- Expect to be able to successfully & securely purchase a product with appropriate feedback of where they are in the process and if the status of the purchase.
- Feedback whether or not registered, logged in, logged out.

<a></a>
### **User Stories**

#### **Guest User**
*As a Guest User, I want:*
1. the main purpose of the site is to be clear so that I immediately know what the site is intended for upon entering;
2. to be met with a visually appealing and easy to read layout of created items;
3. to view the product group categories to get a sense of what type of products they can buy and easily navigate to it;
4. be able to easily go to the store section to purchase items;
5. to easily find a way to search for products to view what I might be looking for;
6. to be able to register as a returning user to save my detail & access exclusive information;
7. to be able to get in contact via social media so that I can follow Saran Collection;
8. to easily find a way to get in contact with Saran Collection if I have questions;
9. to feel secure in the payment process;
10. to view products by category so I view a particular group of products;
11. to be able to add a product to the shopping bag and view the total of the order at any time to control my budget;
12. to control the number of products they view on a page for ease of use;
13. to view product details and images so I can see the product closer up and see it in more detail ;
14. to be able to update and delete products in the basket to be in full control of the purchase;
15. to view order details to be able to confirm everything before purchase;
16. a clear indication of how to pay for the product as well as an easy and secure method to pay for products with personal & card details so that they feel comfortable providing the information;
17. to view another summary to ensure the products and cost as a final check;
18. to view how long the checkout process is to see how far they are in the process of completing the order;
19. to receive appropriate feedback of order success or failure to ensure purchase has gone through;
20. to easily scroll up on pages with longer information.

#### **Registered User**
*As a Registered User, I want to have the same as the a Guest user as well as:*
1. to be able to log back into the site with my initial latest credentials;
2. to be able to reset password in the event they forget it;
3. to view the place with my order history but also view, edit, add, delete personal info;
4. to be able to log out of my account;

#### **Admin User**
*As a Admin User, I want to have the same as the a Guest & Registered users as well as:*
1. to have the ability to log in to an admin account so that I can add, edit and delete products to the database;
2. to have an environment to view all users, products and manage other information of the e-commerce store;



<br>
<hr>

<a></a>
## **UI Design**
### **Font** 
- [Google Fonts](https://fonts.google.com/) was used to explore the various options.
- The project has the main font of [Lato](https://fonts.google.com/specimen/Lato?query=lato) as it is easy to read and modern
- “Sans-Serif” is used as the default backup font in cases where these fonts have difficulty loading

<a></a>
### **Colour Scheme**
- The colour scheme is based on creating a fun and both feminine and masculine environment to symbolize warmth & enjoyment ;
-  I always loved the combination of bright pink and forest green. MS4 was my last chance to use this colour scheme and have fun with it. 
- All colours were checked with [WebAIM](https://webaim.org/resources/contrastchecker/) to check the accessibility of the colours and present a pass.

#### **Colour Palette**
ColorHunt was used to map out my colour scheme.
<details>
<summary>Colour Palette Detail</summary>

![Colour Palette](/documentation/images/colour_palette.png)
</details>

<a></a>
### **Icons**
- Majority of icons from the [Font Awesome](https://fontawesome.com/) Icon library were used.

<a></a>
### **Framework**
The overall structure that was used is the [Bootstrap4](https://getbootstrap.com/) framework. Bootstrap provides various elements of CSS and Javascript which is very helpful to keep a good structure on your page.

<br>
<hr>

### **Wireframe Images**
#### **Low Fidelity**
[Balsamiq](https://balsamiq.com/) was used to create low-fidelity wireframes. Low-fidelity designs were utilised to make the design process simple and test low-tech concepts. When designing a low-fidelity prototype, the font types and colours are ignored to focus on the design of the project itself.

<details>
<summary>Home (index.html)</summary>

![Wireframe: Home](/documentation/wireframes/wireframe_home.png)
</details>

<details>
<summary>Profile Page (profile.html) - registered users </summary>

![Wireframe: Profile](/documentation/wireframes/wireframe_profile.png)
</details>

<details>
<summary>Products (products.html, products/<category_name>.html) </summary>

![Wireframe: Products](/documentation/wireframes/wireframe_products.png)
</details>

<details>
<summary>Product Details (product/<product_id>.html) </summary>

![Wireframe: Product Details](/documentation/wireframes/wireframe_product_details.png)
</details>

<details>
<summary>Shopping Bag (bag.html)</summary>

![Wireframe: Shopping Bag](/documentation/wireframes/wireframe_bag.png)
</details>

<details>
<summary>Full Shopping Bag (bag.html)</summary>

![Wireframe: Shopping Bag](/documentation/wireframes/wireframe_full_shopping_bag.png)
</details>

<details>
<summary>Checkout (checkout.html) </summary>

![Wireframe: Checkout](/documentation/wireframes/wireframe_checkout.png)
</details>

<details>
<summary>Checkout Success (checkout_success.html)</summary>

![Wireframe: Checkout Success](/documentation/wireframes/wireframe_checkout_success.png)
</details>

<details>
<summary>Login Page (accounts/login.html) </summary>

![Wireframe: Login](/documentation/wireframes/wireframe_login.png)
</details>

<details>
<summary>Registration Page (accounts/signup.html) </summary>

![Wireframe: Registration](/documentation/wireframes/wireframe_register.png)
</details>

<details>
<summary>Contact Us (contact_us.html)</summary>

![Wireframe: Contact](/documentation/wireframes/wireframe_contact_us.png)
</details>

<details>
<summary>Returns (returns.html)</summary>

![Wireframe: Returns](/documentation/wireframes/wireframe_returns.png)
</details>

<details>
<summary>Size Charts (sizing.html)</summary>

![Wireframe: Size Charts](/documentation/wireframes/wireframe_sizing.png)
</details>

<details>
<summary>Shipping (shipping.html)</summary>

![Wireframe: Shipping](/documentation/wireframes/wireframe_shipping.png)
</details>

<details>
<summary>Add Products Page (add_products.html) - for admin users</summary>

![Wireframe: Add Products](/documentation/wireframes/wireframe_add_product.png)
</details>

<details>
<summary>Edit Products Page  (edit_products.html) - for admin users</summary>

![Wireframe: Edit Products](/documentation/wireframes/wireframe_edit_product.png)
</details>

<details>
<summary>Delete Products Page  (delete_products.html) - for admin users</summary>

![Wireframe: Delete Products](/documentation/wireframes/wireframe_delete_product.png)
</details>

<br>
<hr>

<a></a>
## **Data Structure**
A database structure was designed to be specifically suited for Saran Collection. It was important to make sure the data structure was logical. Each product is linked to a category and these are identified by id (pk number). 

Each order has a unique order number which is generated when the order is processed and orders have the users and product details.

Users have the option to purchase products as guest users or as registered users. Guest users can complete the order process but their details will not be saved, they won’t be able to see a Profile with their details, order history and shipping address etc. A Registered user will not only have access to their Profile but will also have their details pre-populated the next time they shop. 

SQLite, which is Django built-in database is used for development mode and Heroku Postgres is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode.

<details>
<summary>Data Structure</summary>

![Data Structure](/documentation/images/data_structure.png)
</details>

<br>
<hr>

<a></a>
## **Existing Features**
### Elements on every page
#### Header
 1. Top bar
- A carousel which highlights the delivery threshold and encourages users to sign up. 
2. Logo
- Allows the user to easily recognise the brand of “Saran Collection”. If the user clicks on the logo, it will return the users to the “Home” section as they would expect.
3. Navbar
- Navigation Bar - Allows the user to easily navigate the website's sections and find what they are looking for with ease and speed.
- The Navbar sticks at the top while useres scroll down hte page so they can click on it while browsing. 
- Above the navigation bar features the Saran Collection logo in the centre.
- For visitors to the site who are not logged in (Guest Users), these menu links are available for them to use:
    - Home
    - Shop with dropdown:
        - All Products
        - By price
        - By rating
        - By category
        - All products
    - Women:
        - Jumpsuits
        - Dresses
        - Bags
        - Shoes
    - Men:
        - Suits
        - Shirts
        - Belts
        - Shoes
    - Profile Icon with dropdown:
        - Log in
        - Register
- For visitors to the site who are not logged in (Guest Users), these menu links are available for them to use:
    - Home
    - Shop with dropdown:
        - All Products
        - By price
        - By rating
        - By category
        - All products
    - Women:
        - Jumpsuits
        - Dresses
        - Bags
        - Shoes
   - Men:
        - Suits
        - Shirts
        - Belts
        - Shoes
    - Profile Icon with dropdown:
        - My Profile
        - Log out
        - Product Management - Only admin users will be able to to view this
- The navbar is collapsed into a burger icon on small screens.

#### Footer
-  Quick links to Contact, Returns, Shipping, and Size Charts 
- Copyright information.
- Links to social media for Admin -Social Icons - Allows the user to access the social platforms of the Saran Collection.

### Home page (index.html) 
- This is the main page of the website. 
- The landing page gives the user an immediate welcome and indication of what the site is about.
- There are two CTA buttons to view the Store for both men and women which is important as the primary goal of the user is to purchase products.
- The bottom of the page features the best sellers based on the ratings of the products. 

### Profile Page (profile.html) - registered users 
- This page can only be viewed by registered users
- Then if the user logs in or registers successfully they are taken back to the login page to login.
- This page will feature their username at the top to personalise the user experience.
- The user will be able to see their user info, delivery info and order history
- The user will see a CTS link. 

### Products (products.html, products/<category_name>.html) 
- The pages where users can see all products and sort by a group of categories & category
- If a user clicks on the view details button, it will take them to the product details page.

### Product Details (product/<product_id>.html) 
- These pages are where the users can see product details and to select the quantity;
- The user will see product detail like Name, Price, Category, and Sizes 
- Users can add a product to the shopping bag.
- The user will also be able to click on a link to go back to the products page
- If a user adds a product to their shopping bag, they are notified and a toast will popup with a summary of what is in their shopping bag then as well as the cost, product info and a link to the shopping bag.

### Add Products Page (add_products.html) - for admin users
- This page can only be viewed by the admin user.
- The add products page features a simple form, where the admin user can input the basic information including adding an image for the product
- The admin user will receive validation or error feedback when they enter information in the input field.
- If the user clicks the add product button, it will add the new product to the database.
- If the user clicks on the cancel button it will take them back to the products page.

### Edit Products Page  (edit_products.html) - for admin users
- This page can only be viewed by the admin user.
- The edit products page features a simple form, where the admin user can edit a product in the database
- If the admin user clicked on the Edit product button on the products page then they will be taken to this page. 
- The current product information will be shown and the admin user can change the information and save it. This will update the database with the new information.
- The admin user will receive validation or error feedback when they enter information in the input field.
- If the user clicks on the cancel button it will take them back to the products page.

### Delete Product (delete_products.html) - for admin users
- If the user is an administrator, they will see the option to delete a product.
- If they click it, they will be presented with a confirmation screen and then if they click delete, they can delete the product and the database will be updated.

### Shopping Bag (bag.html) 
- On this page users can view all the selected products and details. Users can update the quantity and there is an option to remove products. There is a button link to a checkout page for the final step of shopping.
- The order total, delivery cost and Total cost is clearly indicated to the user.
- At the top of the page, there is an indication of where the user is in the buying/checkout process for a better user experience

### Checkout (checkout.html) 
- The checkout page is where users can enter their information to process their order. 
- The user can see a summary of their order at the top of the page.
- At the top of the page, there is an indication of where the user is in the buying/checkout process for a better user experience.
- The user will be able to click on a link to back to their bag if they want to adjust it
- The user will see a clear button/link to go to the next step in the order process which will be the payment page.

### Payment (checkout.html) 
- Stripe is used to process the order payment. This is a secured platform for credit card payment.
- The user will see a simple form to fill in their payment information and securely pay. This is reinforced with the Stripe logo and the lock icon.
- At the top of the page, there is an indication of where the user is in the buying/checkout process for a better user experience.

### Checkout Success (checkout_success.html) 
- The users will see the checkout success page if the payment is a success and the order is processed. Users can see the order number, shipping address and product details. 
- The user will be able to return to the products page.
- At the top of the page, there is an indication of where the user is in the buying/checkout - process for a better user experience.

### Login Page
- The login page features a simple form where the user can enter either their username or their email address and their password.
- There is helper text under each input field to guide the user as to the parameters they can input.
- The user will receive validation or error feedback when they enter information in the input field which is also accompanied by colours to show validation (green for correct and red for incorrect).
- If the user lands on the log in page but realises they don't have an account yet and would like to register, there is a link on the page that will take them to the registration page or they can click on the navbar menu Sign up link.
- The page where users can log in to the website and access the Profile page to see their user info, delivery info and order history
- The form with built-in functionality is created with the Django Allauth package.

### Registration Page
- The sign-up page features a simple form, where the user can input a username, email address and password. The form was kept deliberately simple so that signup has minimum barriers.
- If the user lands on the registration page but realises they already have an account and would like to log in, there is a link on the page that will take them to the login page or they can click on the navbar menu Log in link.
- There is a message to the user about not sharing their information to put the user's mind at ease.

### Log Out
- If a registered or admin user clicks on the log out button, they will be logged out of their current session and will no longer be able to see the pages they would if they were logged in.
- A registered user will have to log in again if they want to see their Profile.
- An Admin user will have to log in again if they want to see their Profile or the Manage Products Page.

### Contact us (contact.html)
- It features a simple form where the user can fill out to send a message to admin. 

### Returns (returns.html)
- Provides information about some FAQs about returning items procedure. 

### Shipping (shipping.html)  
- This page can contains information about shipping details and how much and how long it takes to send items to the customers. 

### Size Charts (sizing.html)  
- Provides a guide to users whether male or female to help them to pick the right size item. 

### 403, 404 & 500 Pages
- The custom 403, 404 & 500 Pages contains an image and text that makes the user understand they have encountered an error. There is a button to return the user to the Saran Collection Home page.

<br>
<hr>

<a></a>
## **Future Features**
These are possible future features to be added to the project which was suggested by users during the usability tests. As these features were not part of a minimum viable product launch phase, they will be implemented in future releases.
- Add a filter products option. 
- Add a blog and tips on how to style. 
- The user can change their password and email from their profile if they click on a Change password button. A modal will pop up and ask for the new password. If they confirm to change their password, their password will be updated in the database under the Users collection.
- I would like to have custom helper text for all forms on the site. Currently, the forms have crispy and Django feedback to users which could frustrate them as they only receive feedback if the fields were filled in incorrectly. After user research, it is clear that users want to know what is expected of them before they enter information in the input fields. As a temporary measure to solve user frustration, I added helper text at the bottom of the register form to guide the user at least what is expected of them.

<br>
<hr>

<a></a>
## **Technologies Used**

### **Languages**
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language

### **Libraries & Frameworks**
- [Bootstrap4](https://getbootstrap.com/) for simplify the structure of the website
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Hover.css](https://cdnjs.com/libraries/hover.css/2.1.0) to apply hover effects to the projects navbar.
- [Django](https://www.djangoproject.com/) (an open-source web framework) as the main framework of Python
- [SQLite](https://www.sqlite.org/index.html) (Django built-in database) as a database in development mode
- [PostgreSQL](https://landing.aiven.io/en/aiven-for-postgresql/) (Heroku built-in) as a database in production mode
- [Stripe](https://stripe.com/en-ie) for credit card payment
- [AWS](https://aws.amazon.com/) (Amazon Web Services) for hosting static files and images for the website

### **Tools**
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment (IDE)
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website
- [Responsinator](http://www.responsinator.com/) - to determine if the site was responsive to various devices.
- [Am I Responsive](http://ami.responsivedesign.is/#) to view images of the website on different devices if the site was responsive to various devices.
- Chrome DevTools to help edit pages and diagnose problems quickly.
- [W3C Markup Validator](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [JSHint Validator](https://jshint.com/) for detecting errors and potential problems in your JavaScript code
- [Link Checker](https://validator.w3.org/checklink) for checking all links on the website and see if all links work
- Lighthouse in Google dev tool for testing the performance of the website
- [PEP8 Online](http://pep8online.com/) for checking Python code syntax
- [Grammerly](https://www.grammarly.com/) to check spelling & grammer
- [Notion](https://www.notion.so) for project planning and tracking

### **Design**
- [Balsamiq](https://balsamiq.com/) to design low fidelity mockups

<br>
<hr>

<a></a>
## **Testing**
Testing information can be found in the separate [TESTING.md file](documentation/TESTING.md)

<br>
<hr>

<a></a>
## **Deployment**
This project uses GitHub for version control, GitPod as the cloud-based IDE and Heroku to deploy the site into production. Heroku Postgres is used for the database. [AWS services](https://aws.amazon.com/), which is also a cloud-based platform, is used to store static files and images as Heroku has [no files system to store new files]().

The below steps are specific to Gitpod therefore depending on your IDE, you might need to adjust the below steps. 

### To clone the project:
From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal: 
```
git clone https://github.com/Franciskadtt/happybean.git
```

#### To install required software:
While you are still in the terminal, type pip3 install -r requirements.txt, this will install all the required softwares to run the project:
```
pip3 install -r requirements.txt
```

#### Setup an enviroment for variables
You now need to set up the database with environment variables. Create a file titled env.py and make sure it is placed in the of this file structure, on the same level as the app.py file. You can also add these in your workspace variable section. 

Option 1: Env.py file:
```
 os.environ.setdefault('SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('DEVELOPMENT', 'True')
 os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your_variable_here>')
 ```
- In ` settings.py`  add:
```
if os.path.exists("env.py"):
    import env
```
-  Add your env.py file to `.gitignore`, before pushing your changes.


<br>Option 2: Workspace Variables:
```
KEY = 'SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'DEVELOPMENT', VALUE = 'True'
KEY = 'STRIPE_PUBLIC_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_CH', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_SUB', VALUE = '<your_variable_here>'
KEY = 'AWS_ACCESS_KEY_ID', VALUE: '<your_variable_here>'
KEY = 'AWS_SECRET_ACCESS_KEY', VALUE: '<your_variable_here>'
KEY = 'USE_AWS', VALUE: 'True'
 ```

- In ` settings.py`  add:
 ```
 SECRET_KEY = os.environ.get('SECRET_KEY', '')
 ```

#### DEBUG 
```
DEBUG = 'DEVELOPMENT' in os.environ
```

### **Heroku Deployment**
- Go to the [Heroku](https://www.heroku.com/) website. Register for an account and click on "Create a new app".
- Setup a Heroku app within the Heroku dashboard - Type in the app name and select region the click on create app.
- In Heroku, in your app, click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
- Search for your repo (or sign in and connect GitHub account) and select this.
- Then click "Hide Config Vars" in Heroku.
- Go to the resources tab and search for Heroku Postgres. Choose the “hobby dev - free” option and submit the order form.
- On the `settings.py file`, you will need to comment out the 'SQLite and Postgres databases' section and uncomment the 'PostgreSQL Database' section. (this is temporary, nothing should be pushed/committed just yet).
- Add the database URL from Heroku & migrate your models to the PostgreSQL database with: 
    ```
    python3 manage.py migrate
    ```
- Create a superuser with the following command, and fill in the required information.:
    ```
    python3 manage.py createsuperuser
    ```
- In the `settings.py` file, you can now delete the 'PostgreSQL Database' section and uncomment the 'SQLite and PostgreSQL Databases' section. This means that either database can now be used interchangeably.
- Install gunicorn and freeze that to the requirements file with the following commands:
    ```
    pip3 install gunicorn
    pip3 freeze --local > requirements.txt
    ```
- Create a Procfile and inside, add the following:
    ```
    web: gunicorn happybean.wsgi:application
- In `settings.py`, use an if statement so that when the app runs on Heroku, you will connect to Postgres, and otherwise, it will connect to sqlite3, like so:
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
- Copy the variables from the variable enviroment one by one into the heroku config vars. They would be:
   ```
    KEY: 'SECRET_KEY', VALUE: “your_variable_here”
    KEY: 'DEVELOPMENT', VALUE: "True"
    KEY: 'STRIPE_PUBLIC_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_SECRET_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_CH', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_SUB', VALUE: "your_variable_here"
    KEY: AWS_ACCESS_KEY_ID, VALUE: "AWS access key ID"
    KEY: AWS_SECRET_ACCESS_KEY, VALUE: "AWS secret access key"
    KEY: USE_AWS, VALUE: "True"
    ```
- Login to Heroku in the CLI and temporarity disable collectstatic, with the following command:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app happybean
    ```
- Add your Heroku app and local host to allowed hosts in `settings.py.`
- Push to Github, and then to Heroku master. 
- In Heroku, go to the 'Deploy' tab. In the section 'Deployment Method' click on 'Github - Connect to Github'. Make sure your Github profile is displayed. Add the repository name and click on 'Search'. After Heroku has found the repository, click on 'Connect'. This will connect your Heroku app to your GitHub repository. Click 'Enable automatic deploys'. Your code will automatically be deployed to Heroku as well. 

### **AWS (Amazon Web Services)**
Create an account with [AWS](www.aws.amazon.com), follow the steps and sign in. 
- Go to the AWS management console and go to the S3 service. There, create a new bucket. Uncheck 'block all public access' and acknowledge that the bucket will be public.
- Go to the buckets properties, and turn on static website hosting. Select 'Use this bucket to host a website', and fill in index.html and error.html, then click 'save'.
- Go to the permissions tab, and go to CORS configuration. Paste in a CORS configuration:
```
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
```
- Go to the Bucket policy tab and click 'policy generator', to create a policy. Choose 's3 bucket policy', allow all principals by typing a star. From the action dropdown menu select 'GetObject'. Copy the ARN and paste it into the ARN box. Then click 'add statment' and then click 'generate policy'. Copy the policy into the bucket policy editor. Add a slash star onto the end of the resource key. Click 'save'. 
- Go to access control list tab, under public access, click on 'Everyone', select 'List Objects'. Then click 'save'. 
- Go to IAM (from services menu), click on 'groups' and create a new user group. Give the group a group name (f.e. 'manage-happybean'). Then click 'create group'. 
- Click 'policies' in the dashboard, and then click 'create policy'. Go to the JSON tab. Click 'import managed policy'. Import 'AmazonS3FullAccess'. Get the bucket ARN from the bucket policy page in S3, and paste that in after 'Resource', as a list (first the ARN, then also the ARN with a slash and star). Click 'next tags' and then 'next review'. Give it a name and description. Click 'create policy'. 
- Go to 'groups'. Click the manage-happybean group. Go to 'permissions'. Click 'attach policy'. Select the policy you just created. Click 'add permissions' and then 'Attach policy'.
- Go to 'users'. Click 'add user'. As username write 'happybean-staticfiles-user. Give programmatic access. Click 'next'. Add the user to the group. Click through to the end. Download the .csv file. 

### **Connecting to DJANGO to S3**
- Go back to GitPod. Install boto3 and Django storages, and freeze them to the requirement file with the following commands:
    ```
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```
- Add 'storages' to the installed apps in the settings.py file.
- Add the following if statement:
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'happybean'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
- On Heroku, add the AWS keys to the Config Variables (they can be found in the csv file you downloaded earlier). Also, add USE_AWS and set it to True. 
- Remove the DISABLE_COLLECTSTATIC from the variables. 
- In GitPod, create a file called custom_storages.py and add:
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S#Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION 
    ```
- To the before mentioned if statement from above, in settings.py, also add:
    ```
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
- Add, commit and push these changes. If you now go to the bucket, you will see all the static files. 
- Go to your bucket and add a new folder called media. Inside it, click 'upload' and then 'add files'. Then select all the images you'd like to use. Click 'next'. Under 'manage public permissions', select 'grant public read access'.
- On Stripe, add a new webhook endpoint, with the URL of your Heroku app, followed by 
```/checkout/wh/```. Select 'receive all events' and click 'add endpoint'.

___
<br>

<a></a>
## **Credits**

### **Content**
- The copy and text for this website was created by Teema Namdarian 
- Product descriptions from the following sources:
  - https://www.moss.co.uk/
  - https://www.aqaq.com/

### **Media**
- Logo Illustration is commissioned. 
- Products photos from the following sources:
    - Men’s section from https://www.moss.co.uk/
    - Women’s section from https://www.aqaq.com/
    - Home page images from [Pexels](https://www.pexels.com//)

### **Code**
- Checkout progress: Original code with modifications from: https://bbbootstrap.com/snippets/bootstrap-4-ecommerce-checkout-form-progress-bar-44177913
- Exclude creator field from form https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#models-and-request-user
- For presenting extra content via context: https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/
- Products app:
    - User permissions: https://bit.ly/3mSsegO
    - Success message in DeleteView: https://bit.ly/3oRYlzG
- Page scroll up javascript feature: Orginal code from with modifications for the project from https://stackoverflow.com/questions/14249998/jquery-back-to-top and https://www.tutorialrepublic.com/faq/how-to-scroll-to-the-top-of-the-page-using-jquery.php 
- Scroll up button and icon Styling: Orginal code from with modifications for the project from https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
- Send email functionality:
    - https://docs.djangoproject.com/en/3.2/topics/email/
    - https://docs.djangoproject.com/en/3.2/topics/forms/
    - https://www.youtube.com/watch?v=w4ilq6Zk-08&list=PLXcnmXd-db_hO1v3SLAzVcNieoS_Tcn-6&index=6

### **Acknowledgements**
- Thanks to my mentor Guido Cecilio for guiding me throughout this project.
- Code Institute Tutors for giving me a guidance on how to solve issues.

##### back to [top](#table-of-contents)
