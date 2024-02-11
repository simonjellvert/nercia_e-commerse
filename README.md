[Authentication using Email](https://tech.serhatteker.com/post/2020-01/email-as-username-django/) 

# NERCIA WEBSHOP

**Deployed website: [Link to website](https://.herokuapp.com/)**

![Main image](docs/img/...)

---

## About

Nercia is a swedish competence development company that has a turnover of approx SEK 250m and has around 150 employees spread out over 17 offices in Sweden. They're working with both government agencies, municipal education coordinators and private own companies. 
The mission is to both develop skill (through Nercia Utbildning AB/Nercia Training Ltd) and to add skill (through Nercia Bemanning AB/Nercia Staffing Ltd).

Within Nercia Training there is a business area in swedish called "Företagsutbildning", in english translated to Business training in which a long lasting strategic orientation has been to develop a webshop where the customers can shop their trainings without having to contact 
a salesperson each and every time they want to book a training for their staff. 

The business area manager, digital training producer and marketing manager has been involved in both lay out of the webshop and what functions they need to be able to launch the website if the board of the company wants the site to go live.

The webshop has a login system so that the user can be able to save billing information and keep track of previuos orders. It has the typical shopping bag function to edit or delete items which has been added. It has a checkout system that provides options for both card payment or by invoice. And of course a card payment system for that option.
Since the products (trainings) are regularly updated with price and new dates it has an easy product managing for the administrators of the site. 


---

## UX

The marketing manager wanted the webshop to look similar to the original website so the visitor would be familiar with the look and to ease the transition from the original page to the webshop. So the first page of the webshop has a obvious welcoming message.

The website follows Nercia's graphical profile which is set up for the all graphical materials to be eye-catching and user friendly.

---

## Target Audience

This webshop is for new and old customers of Nercia and should exist to simplify the booking of the training courses. The purpose is to reduce waitning time for the customer to recieve a confirmation of the booking (which now takes place by a salesperson responding manually), which sometimes can take up till 24 hours. This webshop also allow the customer to ensure that invoicing is set up as preffered and for Nercia's finance department to ensure the invoice is not sent to the wrong adress.

---

## User Stories

#### Viewing and navigation

| Issue ID    | User Story |
|-------------|-------------|
| [#1](https://github.com/simonjellvert/nercia_e-commerse/issues/1) | As a **site user** I can **view a list of products** so that I can **select and add those I need for myself or my employees in the shippoing bag** |
| [#2](https://github.com/simonjellvert/nercia_e-commerse/issues/2) | As a **site user** I can **see the program of the training I'm interested in** so that I can **understand what to expect of the training** |
| [#3](https://github.com/simonjellvert/nercia_e-commerse/issues/3) | As a **site user** I can **search and filter trainings in different subjects, or by name or by description** so that I can **easily find what I'm looking for** |
| [#4](https://github.com/simonjellvert/nercia_e-commerse/issues/4) | As a **site user** I can **view my shopping bag** so that I can **double check if i forgot something** |
| [#5](https://github.com/simonjellvert/nercia_e-commerse/issues/5) | As a **site user** I can **check the order history** so that I can **go back and see when myself or an employee attended the training** |

#### Registration

| [#6](https://github.com/simonjellvert/nercia_e-commerse/issues/6) | As a **site user** I can **register an account** so that I can **have a personal page to store my information and purchases** |
| [#7](https://github.com/simonjellvert/nercia_e-commerse/issues/7) | As a **site user** I can **login and logout** so that I can **access my personal information** |
| [#8](https://github.com/simonjellvert/nercia_e-commerse/issues/8) | As a **site user** I can **recover my password** so that I can **recover my account** |
| [#9](https://github.com/simonjellvert/nercia_e-commerse/issues/9) | As a **site user** I can **receive an email confirmation after registration** so that I can **verify that my account was successfully created** |
| [#10](https://github.com/simonjellvert/nercia_e-commerse/issues/10) | As a **site user** I can **update or edit my account** so that I can **edit my information** |
| [#11](https://github.com/simonjellvert/nercia_e-commerse/issues/11) | As a **site user** I can **delete my account** so that I can **remove it if I'm not longer using it** |
| [#24](https://github.com/simonjellvert/nercia_e-commerse/issues/24) | As a ***site user** I can **subscribe to newsletters** so that I can **hear about new products and other relevant information regarding company training.** |

#### Bag

| [#12](https://github.com/simonjellvert/nercia_e-commerse/issues/12) | As a **site user** I can **edit/update quantity of the product I've added** so that I **don't select the wrong number of products** |
| [#13](https://github.com/simonjellvert/nercia_e-commerse/issues/13) | As a **site user** I can **delete a product from the shopping bag** if I **accidentally added the wrong product** |
| [#14](https://github.com/simonjellvert/nercia_e-commerse/issues/14) | As a **site user** I can **add name and email of the participant on each training** so that I can **make sure they get an invite to the training** |

#### Checkout

| [#15](https://github.com/simonjellvert/nercia_e-commerse/issues/15) | As a **site user** I can **save my billing information** so that I can **reuse it without entering it again the next time** |
| [#16](https://github.com/simonjellvert/nercia_e-commerse/issues/16) | As a **site user** I can **see the total cost of my shopping bag** so that I **make sure i don't go over budget** |
| [#17](https://github.com/simonjellvert/nercia_e-commerse/issues/17) | As a **site** user I can **choose if I want to pay with card or bill** so that I can **make sure my payment is going to be handled the way I want it to** |

#### After checkout

| [#18](https://github.com/simonjellvert/nercia_e-commerse/issues/18) | As a **site user** I can **receive a order confirmation efter checkout** so that I can **see what i bought** |
| [#19](https://github.com/simonjellvert/nercia_e-commerse/issues/19) | As a **site user** I can **receive a email confirmation after checkout** so that I can **get proof of my purchase** |

#### Manager and admin

| [#20](https://github.com/simonjellvert/nercia_e-commerse/issues/20) | As a **admin** I can **add, edit and delete categories** so that I can **keep them up to date** |
| [#21](https://github.com/simonjellvert/nercia_e-commerse/issues/21) | As a **admin** I can **add, edit and delete products** so that I can **make sure the products are up to date** |
| [#22](https://github.com/simonjellvert/nercia_e-commerse/issues/22) | As a **admin** I can **review customers orders** so that I can **add them to the CRM** |
| [#23](https://github.com/simonjellvert/nercia_e-commerse/issues/23) | As a **administrator** I can **send newsletters to those users that subscribes** so that **they can receive information about new products and other relevant information** |

---

## Business Model

The Business Model is B2C, meaning that the company sells products to customers only.
It focuses on individual transactions only.

---

## Web marketing

Text here

1. News letter

Text here

2. Promo codes

Text here

3. Facebook

Text here

4. Instagram

Text here

5. TikTok

Text here

6. LinkedIn

Text here

---

## Future development

#### Link up bookings/order directly to Learning plattform
Nercia has their own learning plattform where the participant get all their info on their training, such as date and time, location, course materials etc. 
When a order has been placed and is valid with participants information (email, name) that info will go straight to the specific training in the learning plattform for the administrators to handle.

#### Link up booking/orders to finance program
When a order has been made and the payment option is invoice the necessary info will automatically be uploaded to the finance program so the finance administrators donät have to do extra work.

#### Link up orders directly to CRM system
The orders should automatically be loaded into the CRM database so a salesman can handle incoming orders.

#### Order cancellation
When a order has been placed the user should be able to cancel it and all information about the order will be deleted.

#### Add attendee
The user should be able to add attendees to each product/training.

#### Google map
Tidy up the map on contacts page, missing functionality in the version.

#### Cancel card payments
Implement easy handling for canceling a customers card payment.

#### Resonsive orde management page
In this version the order management is responsive but it doesent look good even though an administrator of this particular page is not likely going to handle orders from the phone or tablet. But for future development that feature is on to do.

#### Obvious redirecting (checkout)
In this version a user that is not authenticated is not able to enter the checkout page, instead it is redirected to the sign up page - but without any messages. It's a bug that should be fixed in the upcoming versions.

#### Google map warning
The Google Map on contacts page works as I expect it do, but get this warning in the browser console: 
"Google Maps
JavaScript API has been leaded directly without leading=async.
This can result in suboptimal performance. For best-practice leading patterns please see: https://goo.gle/js-api-loading"
Next version should have solved this warning.

#### Webhooks for payment
The code is set up but haven't had the time to test it, but will be tested and implemented for next version.

#### Refined file adder
The button for file adding in products and contacts templates does not look so good and should be refined for better UX.

---

## Technologies used
- ### Languages:
    
    + **Python 3.12.1**: the primary language used to develop the server-side of the website.
    + **JavaScript**: the primary language used to develop interactive components of the website.
    + **HTML**: the markup language used to create the website.
    + **CSS**: the styling language used to style the website.

- ### Frameworks and libraries:

    + **Django**: python framework used to create all the logic.
    + **jQuery**: was used to control click events and sending AJAX requests.
    + **jQuery User Interface**: was used to create interactive elements.

- ### Databases:

    + **SQLite**: was used as a development database.
    + **PostgreSQL**: the database used to store all the data.


- ### Other tools:

    + **Git**:: the version control system used to manage the code.
    + **Pip3**: the package manager used to install the dependencies.
    + **Gunicorn**: the web server used to run the website.
    + **Psycopg2**: the database driver used to connect to the database.
    + **Django-allauth** the authentication library used to create the user accounts.
    + **Django-crispy-forms**: was used to control the rendering behavior of Django forms.
    + **GitHub**: used to host the website's source code.
    + **CodeAnywhere**: the IDE used to develop the website.
    + **GitPod**: the alternative IDE used to develop the website.
    + **Amazon AWS**: host of static files.
    + **Chrome DevTools**: was used to debug the website.
    + **Font Awesome**: was used to create the icons used in the website.
    + **Miro**: was used to make a flowchart for the README file.
    + **Coolors**: was used to make a color palette for the website.
    + **W3C Validator**: was used to validate HTML5 code for the website.
    + **W3C CSS validator**: was used to validate CSS code for the website.
    + **JShint**: was used to validate JS code for the website.
    + **PEP8**: was used to validate Python code for the website.
    + **Stripe**: was used to create the payment system.
    + **Lunapic**: was used to crop and center unsplash images.
    + **Sitemap Generator**: was used to create the sitemap.xml file.

---

## Features

Please refer to the [FEATURES.md](FEATURES.md) file for all test-related documentation.

---

## Design

The website follows Nercia's graphical profile which is set up for the all graphical materials to be eye-catching and user friendly.

<!-- #### Color Scheme

Text here

Link here -->

#### Typography

The fonts used for this website are following Nercias graphical profile: ["Ubuntu"](https://fonts.google.com/specimen/Ubuntu?preview.text=Welcome!&query=ubuntu).

<!-- #### Images

Text here

Image here -->

---

<!-- ## Agile Methodology

#### GitHub Project Management

Text here

Image here -->

---

## Information Architecture

### Database

* During the earliest stages of the project, the database was created using SQLite.
* The database was then migrated to PostgreSQL.

### Entity-Relationship Diagram

The structure of building the model is from the ERD below. The flowchart has been updated since the structure has been updated during the development process.

<!-- ![ERD]() -->

<!-- ### Data Modeling

#### Role Model
| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| name          | name          | CharField    | max_length=50, unique=True, blank=True, null=False, verbose_name='Role name' |
| description   | description   | TextField    | max_length=500, blank=True, null=True, verbose_name='Role description' |



#### Profile Model

When user signs up, a new profile is created. 

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| user          | user          | OneToOneField | User, on_delete=models.CASCADE, related_name='profile', verbose_name='User' |
| first_name    | first_name    | CharField    | max_length=50, blank=True, null=True, verbose_name='First name' |
| last_name     | last_name     | CharField    | max_length=50, blank=True, null=True, verbose_name='Last name' |
| avatar        | avatar        | CloudinaryField | blank=True, null=True, verbose_name='Avatar' |
| subscription | subscription | BooleanField | default=False, verbose_name='Subscription' |
| role          | role          | ForeignKey   | Role, default=1, on_delete=models.SET_NULL, null=True, verbose_name='Role' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |

**Note:** The role field is set to 1 by default. This is because the user is a customer by default. The role can be changed only from the admin panel. The decision to make it mandatory was made due to the store security reasons. **Only the site admin can change the role of the user in order to prevent unauthorized access.**

#### Address Model

Users are encouraged to create their own addresses and set the default address for the fastest purchase. 

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| user          | user          | ForeignKey   | User, on_delete=models.CASCADE, related_name='addresses', verbose_name='User' |
| country       | country       | CharField    | max_length=50, blank=False, null=False, verbose_name='Country' |
| county_region | county_region | CharField    | max_length=50, blank=False, null=False, verbose_name='County/region' |
| city          | city          | CharField    | max_length=50, blank=False, null=False, verbose_name='City' |
| address_line  | address_line  | CharField    | max_length=150, blank=False, null=False, verbose_name='Address line' |
| zip_code      | zip_code      | CharField    | max_length=10, blank=False, null=False, verbose_name='Zip code' |
| phone_number  | phone_number  | CharField    | max_length=15, blank=False, null=False, verbose_name='Phone' |
| is_primary    | is_primary    | BooleanField | default=False, verbose_name='Is primary' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |

#### Wishlist Model

When the user signs up, a new wishlist is created.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| user          | user          | ForeignKey   | User, on_delete=models.CASCADE, related_name='wishlist', verbose_name='User' |
| products      | products      | ManyToManyField | Product, blank=True, related_name='wishlist', verbose_name='Products' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |

#### Category Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| name          | name          | CharField    | max_length=100, unique=True, blank=False, null=False, verbose_name='Category name' |
| slug          | slug          | SlugField    | max_length=150, unique=True, blank=False, null=False, verbose_name='Category Slug' |
| is_active     | is_active     | BooleanField | default=False, verbose_name='Is active' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |

#### Tag Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| name          | name          | CharField    | max_length=100, unique=True, blank=False, null=False, verbose_name='Tag name' |
| slug          | slug          | SlugField    | max_length=150, unique=True, blank=False, null=False, verbose_name='Tag Slug' |
| is_active     | is_active     | BooleanField | default=False, verbose_name='Is active' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |

#### Brand Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| name          | name          | CharField    | max_length=100, unique=True, blank=False, null=False, verbose_name='Brand name' |
| slug          | slug          | SlugField    | max_length=150, unique=True, blank=False, null=False, verbose_name='Brand Slug' |
| description   | description   | TextField    | max_length=500, blank=False, null=False, verbose_name='Brand description' |
| is_active     | is_active     | BooleanField | default=False, verbose_name='Is active' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |


#### Product Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| name          | name          | CharField    | max_length=100, unique=True, blank=False, null=False, verbose_name='Product name' |
| slug          | slug          | SlugField    | max_length=150, unique=True, blank=False, null=False, verbose_name='Product Slug' |
| description   | description   | TextField    | max_length=500, blank=False, null=False, verbose_name='Product description' |
| category      | category      | ForeignKey   | Category, on_delete=models.CASCADE, related_name='products', verbose_name='Category' |
| tags          | tags          | ManyToManyField | Tag, related_name='products', verbose_name='Tags' |
| brand         | brand         | ForeignKey   | Brand, on_delete=models.CASCADE, related_name='products', verbose_name='Brand' |
| is_active     | is_active     | BooleanField | default=False, verbose_name='Is active' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |

#### ProductImage Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| product       | product       | ForeignKey   | Product, on_delete=models.CASCADE, related_name='images', verbose_name='Product' |
| image         | image         | CloudinaryField | null=True, blank=True, verbose_name='Image' |
| alt_text      | alt_text      | CharField    | max_length=300, null=True, blank=True, verbose_name='Alt text' |
| default_image | default_image | BooleanField | default=False, verbose_name='Default image' |
| is_active     | is_active     | BooleanField | default=False, verbose_name='Is active' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |

#### ProductAttribute Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| name          | name          | CharField    | max_length=255, unique=True, blank=False, null=False, verbose_name='Attribute name' |
| description   | description   | TextField    | max_length=500, blank=True, null=True, verbose_name='Attribute description' |

#### ProductType Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| name          | name          | CharField    | max_length=100, unique=True, blank=False, null=False, verbose_name='Product type name' |
| slug          | slug          | SlugField    | max_length=150, unique=True, blank=False, null=False, verbose_name='Product type Slug' |
| product_type_attributes | product_type_attributes | ManyToManyField | ProductAttribute, related_name="product_type_attributes", through="ProductTypeAttribute", verbose_name='Product type attributes' |
| description   | description   | TextField    | max_length=500, blank=False, null=False, verbose_name='Product type description' |

#### ProductAttributeValue Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| product_attribute | product_attribute | ForeignKey   | ProductAttribute, on_delete=models.CASCADE, related_name='product_attribute_values', verbose_name='Product attribute' |
| attribute_value | attribute_value | CharField    | max_length=255, blank=False, null=False, verbose_name='Attribute value' |

#### ProductInventory Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| sku           | sku           | CharField    | max_length=50, null=False, unique=True, blank=False, verbose_name='Stock Keeping Unit' |
| upc           | upc           | CharField    | max_length=12, null=False, unique=True, blank=False, verbose_name='Universal Product Code' |
| product       | product       | ForeignKey   | Product, on_delete=models.CASCADE, related_name='inventory', verbose_name='Product' |
| product_type  | product_type  | ForeignKey   | ProductType, on_delete=models.CASCADE, related_name='inventory', verbose_name='Product type' |
| attribute_values | attribute_values | ManyToManyField | ProductAttributeValue, related_name="product_attribute_values", through="ProductAttributeValues", verbose_name='Attribute values' |
| retail_price  | retail_price  | DecimalField | max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Retail price' |
| store_price   | store_price   | DecimalField | max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Store price' |
| sale_price    | sale_price    | DecimalField | max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Sale price' |
| weight        | weight        | FloatField   | null=False, blank=False, verbose_name='Product weight' |
| is_active     | is_active     | BooleanField | default=False, verbose_name='Is active' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| updated_at    | updated_at    | DateTimeField | auto_now=True, verbose_name='Updated at' |

#### Stock Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| product_inventory | product_inventory | ForeignKey   | ProductInventory, on_delete=models.CASCADE, related_name='stock', verbose_name='Product inventory' |
| last_checked     | last_checked     | DateTimeField | null=True, blank=True, verbose_name='Last checked' |
| units_variable   | units_variable   | IntegerField | default=0, null=False, blank=False, verbose_name='Units variable' |
| units            | units            | IntegerField | default=0, null=False, blank=False, verbose_name='Units current' |
| units_sold       | units_sold       | IntegerField | default=0, null=False, blank=False, verbose_name='Units sold' |

#### ProductAttributeValues Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| attributevalues | attributevalues | ForeignKey   | ProductAttributeValue, on_delete=models.CASCADE, related_name='productattributevalues', verbose_name='Attribute values' |
| productinventory | productinventory | ForeignKey   | ProductInventory, on_delete=models.CASCADE, related_name='productattributevalues', verbose_name='Product inventory' |


#### ProductTypeAttribute Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| product_attribute | product_attribute | ForeignKey   | ProductAttribute, on_delete=models.CASCADE, related_name='producttypeattribute', verbose_name='Product attribute' |
| product_type | product_type | ForeignKey   | ProductType, on_delete=models.CASCADE, related_name='producttypeattribute', verbose_name='Product type' |

*The decision to implement unique_together model method was made due to the wider coverage of it rather than UniqueConstraint which has been added in Django 4.0.0.
[Link to Django Documentation](https://docs.djangoproject.com/en/4.0/ref/models/options/#django.db.models.Options.unique_together)*

#### EmailNewsNotification Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| email_name    | email_name    | CharField    | max_length=100, null=False, unique=True, blank=False, verbose_name='Email name' |
| content       | content       | TextField    | null=False, blank=False, verbose_name='Content' |
| code          | code          | CharField    | max_length=100, null=True, blank=True, verbose_name='Code' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |

#### StockEmailNotification Model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| user           | user           | ForeignKey   | User, on_delete=models.CASCADE, verbose_name='Requested user' |
| requested_product | requested_product | ForeignKey   | Product, on_delete=models.CASCADE, verbose_name='Requested product' |
| requested_attributes_values | requested_attributes_values | ManyToManyField | ProductAttributeValue, related_name="requested_attributes_values", through="RequestedAttributesValues", verbose_name='Requested attributes values' |
| requested_quantity | requested_quantity | PositiveIntegerField | verbose_name='Requested quantity' |
| created_at    | created_at    | DateTimeField | auto_now_add=True, verbose_name='Created at' |
| answer_sent    | answer_sent    | BooleanField | default=False, verbose_name='Answer send' | -->

---

## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.

---

## Deployment and Payment setup

- The app was deployed to [Heroku](https://www.heroku.com/).
- The database was deployed to [ElephantSQL](https://www.elephantsql.com/).

<!-- - The app can be reached by the [link](). -->


Please refer to the [DEPLOYMENT.md](DEPLOYMENT.md) file for all deployment and payment-related documentation.

---
<!--
## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Render](https://render.com/): for providing a free hosting.
- [jQuery](https://jquery.com/): for providing varieties of tools to make standard HTML code look appealing.
- [jQuery UI](https://jqueryui.com/): for providing varieties of tools to make standard HTML code look appealing.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [geonames](https://www.geonames.org/): for providing a free database on countries, regions, cities.
- [Multiple Video & Image Upload Plugin - jQuery Miv.js](https://www.jqueryscript.net/form/multi-video-image-upload.html): for providing a free plugin to upload multiple videos and images.
- [Stripe](https://stripe.com/): for providing a free payment gateway.
- [htmlcolorcodes.com](https://htmlcolorcodes.com/): for providing a free database on colors.
- [Very Academy Youtube Channel](https://www.youtube.com/c/veryacademy): for brilliant tutorials, which shed the light on the implementation of database with multi-values products, precise explanations of the stripe API, and many other things!
- [birme](https://www.birme.net/): for providing free service to center and crop images.
- [fontawesome](https://fontawesome.com/): for providing free icons.
- [googlefonts](https://fonts.google.com/): for providing free fonts.
- [BGJar](https://www.bgjar.com/): for the free access to the background images build tool.
- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en): for providing a free platform to test website responsiveness
- [GoFullPage](https://gofullpage.com/): for allowing to create free full web page screenshots;
- [Favicon Generator. For real.](https://realfavicongenerator.net/): for providing a free platform to generate favicons.
- [Sitemap Generator](https://www.xml-sitemaps.com/): for providing a free platform to generate sitemaps.
- [Coolors](https://coolors.co/): for providing a free platform to generate your own palette.
- [Elon Musk](https://twitter.com/elonmusk?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor): for providing a template for the twitter mock-up page;

### Content and Images

- [unsplash](https://unsplash.com/): for providing a free products' images.
- [Icons8](https://icons8.com/): for providing free access to amazing icons and illustrations to fill out the store.
- [unsplash](https://unsplash.com/): for providing free products' images to fill out the store.
- [chrome developer tools](https://developer.chrome.com/extensions/devtools_inspector): for providing a free platform to test website.
- [adidas](https://www.adidas.com/): for providing free products' data and images to fill out the store on clothes and shoes.
- [fashionunited](https://www.fashionunited.com/): for providing content for the newsletter;
- [dell](https://www.dell.com/): for providing free products' data and images to fill out the store on computers and laptops.
- [nike](https://www.nike.com/): for providing free products' data and images to fill out the store on clothes and shoes.
- [artsaber](https://www.artsabers.com/): for providing free products' images to fill out the store on lightsabers data and images.
- [backwaterreptiles](https://www.backwaterreptiles.com/): for providing free products' images to fill out the store on tarantulas' data and images.
- [Yum Of China](https://www.yumofchina.com/chinese-beer/): for providing free data on Chinese beer.
- [lego](https://www.lego.com/): for providing free products' data and images to fill out the store with toys.
- [maggie](https://www.maggie.com/): for providing free products' data and images to fill out the store with maggie products.
- [barilla](https://www.barilla.com/): for providing free products' data and images to fill out the store with pasta.
- [LG electronics](https://www.lg.com/): for providing free products' data and images to fill out the store with electronics.

---

## Acknowledgments

- [Tim Nelson](https://github.com/TravelTimN) was a great supporter of another bold idea of mine for this project. Tim guided me through the development of the project and helped me to learn a lot of new things by challenging me to do something new.
- [Aleksei Konovalov](https://github.com/lexach91), my husband and coding partner, assisted me greatly in product values js selection control implementation and helped me to stay sane.
- [Very Academy Youtube Channel](https://www.youtube.com/c/veryacademy) provided great insight on the implementation of the database with multi-values products, precise explanations of the stripe API, and many other things! This Youtube channel has plenty of brilliant tutorials that shed light on Django's most curious and useful aspects. -->

