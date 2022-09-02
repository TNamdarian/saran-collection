# Saran Collection Website - Testing details

[Main README.md file](/README.md)

[View live version of website via Heroku](https://saran-collection.herokuapp.com/)

___
<br>

<a></a>
## Table of Contents 
* [Test User Stories](#test-user-stories)
* [Testing and Validation](#testing-and-validation) 
* [Further testing](#further-testing)
___
<br>

## **Test User Stories Test Images**

### Unregistered user story images
<details>
<summary>Home</summary>

![Home](/documentation/images/landing_home_page.png)
</details>

<details>
<summary>Footer</summary>

![Footer](/documentation/images/footer.png)
</details>

<details>
<summary>Shop: Product filter, sort and search</summary>

![Shop: Products](/documentation/images/product_filter_sort_search.png)
</details>

<details>
<summary>Product detail</summary>

![Product detail](/documentation/images/product_detail.png)
</details>

<details>
<summary>Bag: Empty</summary>

![Bag: Empty](/documentation/images/bag_app_empty.png)
</details>

<details>
<summary>Bag: With Products</summary>

![Bag: With Products](/documentation/images/bag_app_products.png)
</details>

<details>
<summary>Checkout</summary>

![Checkout](/documentation/images/checkout_app.png)
</details>

<details>
<summary>Checkout Success</summary>

![Checkout Success](/documentation/images/checkout_success.png)
</details>


<details>
<summary>Shipping</summary>

![Shipping](/documentation/images/shipping.png)
</details>

<details>
<summary>Size Charts</summary>

![Size Charts](/documentation/images/size_charts.png)
</details>

<details>
<summary>Returns</summary>

![Returns](/documentation/images/returns.png)
</details>

<details>
<summary>Contact Us</summary>

![Contact Us](/documentation/images/contact_us.png)
</details>

<details>
<summary>Login</summary>

![Login](/documentation/images/login.png)
</details>

<details>
<summary>Register</summary>

![Register](/documentation/images/register.png)
</details>

### Registered user story images (in addition to the guest user stories)

<details>
<summary>Profile</summary>

![Profile](/documentation/images/profile_app.png)
</details>

<details>
<summary>Logout</summary>

![Logout](/documentation/images/logout.png)
</details>

### Admin user story images (in addition to the guest user stories)
<details>
<summary>Add Products</summary>

![Add Product](/documentation/images/add_product.png)
</details>

<details>
<summary>Edit Product</summary>

![Edit Product](/documentation/images/edit_product.png)
</details>

<details>
<summary>Delete Product</summary>

![Delete Product](/documentation/images/delete_product.png)
</details>

<details>
<summary>Blog</summary>

![Blog](/documentation/images/blog.png)
</details>

<details>
<summary>Blogpost Details</summary>

![Blogpost Details](/documentation/images/blog_details.png)
</details>

<details>
<summary>Add Blogpost</summary>

![Add Blogpost](/documentation/images/add_blogpost.png)
</details>

<details>
<summary>Edit blogpost</summary>

![Edit Blogpost](/documentation/images/edit_blogpost.png)
</details>

<details>
<summary>Delete blogpost</summary>

![Delete Blogpost](/documentation/images/delete_blog.png)
</details>

<br>
<hr>

## **Testing and Validation**
### [Link Checker](https://validator.w3.org/checklink)
- To check that all links are working and not broken. 
- The report did not have any issues in final testing.

<br>

### [Responsinator](http://www.responsinator.com/)
- To test the responsiveness of the live website and functionalities on different size mobile devices.
- The allauth templates were styled to ensure they are responsive after testing.
- All pages are now responsive.

<br>

### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
<details>
<summary>Am I Responsive</summary>

![Am I Responsive](/documentation/images/mockup.png)
</details>
<br>

### [JavaScript: JSHint](https://jshint.com/)
- JSHint was used to test javascript code in this project. 
- All issues were resolved. 

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CSS code of the project pasting code in by direct input method.
- All issues were resolved.

<details>
<summary>CSS validation</summary>

![CSS Validation](/documentation/images/css_validated.png)
</details>

<br>

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- All issues were resolved except for 2 errors relating to Django crispy forms (see image below for more detail).

<details>
<summary>HTML validation</summary>

![HTML Validation](/documentation/images/html_validated.png)
</details>

<br>
    
### [Python: PEP8 Online](http://pep8online.com/)

- To validate the Python code of the project to check if it is PEP8 compliant. It was done by pasting code on the site by the direct input method.

<br>

### Lighthouse (Google dev tool)
- To test the accessibility and performance of the website. 
- After testing the site on Lighthouse, there were minor changes that needed to be made, for example, some buttons did not have aria labels, which was added. Another aspect that was fixed was link text styling, the colour needed to be changed to make it more accessible. Lastly, some heading tags were not in order, which was changed as well. 
- After the above changes were made, the overall performance and accessibility have increased. 
- Additional future changes can be made in optimising images in next-generation formats.

<br>

### Browser Compatibility
To ensure a broad range of users can successfully use this site, I tested it across the 4 major browsers in both desktop and mobile configuration. The following browsers were tested:
- Chrome
- Firefox 
- Safari
- Edge

<br>
<hr>

## **Further testing**
- Usability tests were done with two users to analyse the User Experience. The feedback from the users was very helpful to determine what works, what can be improved and determine future features.  
- Asked fellow students, friends and family to look at the site on their devices and report any issues they find.
- Review all functionality and responsiveness on different desktop browsers and the website displayed correctly in all browsers including Safari, Chrome, Edge, Firefox and Opera browsers. (see Browser Compatibility section for detail)

<br>
<hr>

## **Deployment**
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable is set to False.
- Confirmed that there is no difference between the deployed version and the development version.

<br>
<hr>