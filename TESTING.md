# TESTING

## Manual Testing

Testing has been done manually throughout the development. Testing has been done according to the criterias below and until the desired result was achieved.

Testing has been done on different devices to ensure there are no issues. Testing has also been done by employees at Nercia.

### Visitor / Logged in user

| Page    | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Header      |                        |                  |      |             |
| 1 | Click logo | Redirects to home page | Y | - |
| 2 | Click navbar links | Redirects to correct address | Y | Made sure they work correctly depending on authenticated user or not |
| 3 | Bag link updates | Bag link updates with bag total amount | Y | - |
| Footer | | | | | |
| 1 | Click links | Redirects to correct address | Y | - |
| 2 | Footer is responsive | Divides into column correctly depending on screen size | Y | - |
| Home page | | | | |
| 1 | Page is responsive | Adapt to different sizes | Y | - |
| 2 | Click link | Redirects to correct address | Y | Made sure they work correctly depending on authenticated user or not |
| Contact page | | | | |
| 1 | Click map | Opens up google maps to show directions | Y/N | Works fine on computer, not on mobile - future development |
| 2 | Page responsive | Adapts to different screen sizes | Y | - |
| Products | | | | |
| 1 | Page is responsive | Adapats to different screen sizes | Y | - |
| 2| Search for product | Should display matching results | Y | No error message if no matches - fututre development |
| 3 | Filter category | Should display matching results | Y | - |
| Product detail | | | | |
| 1 | Page is responsive | Adapt to different screen sizes | Y | - |
| 2 | Click links | Redirect to correct address | Y | - |
| 3 | Add product to bag | Should update bag and navbar | Y | - |
| 4 | Quantity picker | Should update bag with correct quantity | Y | - |
| Bag page | | | | | |
| 1 | Edit quantity | Should update bag with correct quantity and amount | Y | - |
| 2 | Remove quantity | Should delete product from bag and update amount | Y | - |
| 3 | Click link | Redirects to correct address | Y | If user not authenticated and clicks Checkout - redirects to sign in page |
| 4 | Page is responsive | Adapts to different screen sizes | Y | - |
| Checkout page | | | | |
| 1 | Confirm button disabled | Button should be disabled until form is valid | Y | - |
| 2 | Choose payment method | Displays relevant form | Y | - |
| 3 | Invalid form invoice | Throws error | Y | Not for Invoice referens, future development |
| 4 | Invalid form card | Throws error | Y | - |
| 5 | Valid payment | Redirects to checkout success page | Y | - |
| 6 | Valid payment | Send confirmation email | Y | - |
| 7 | Page is responsive | Adapts to different screen sizes | Y | - |
| Checkout success page | | | | |
| 1 | Displays reciept | with correct amount | Y | - |
| 2 | Displays payment method | Correct method displays | Y | If invoice the address if fetched from user profile |
| 3 | Displays products | Correct products and quantities | Y | - |
| 4 | Page is responsive | Adapts to different screen sizes | Y | - |
| Sign Up | | | | |
| 1 | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 2 | Click on the Login link in the form | Redirection to Login page | Y |          |
| 3 | Enter valid email | Field will only accept email address format | Y | - |
| 4 | Enter valid password 2 times | Field will only accept password format | Y | - |
| 5 | Redirects user if form is valid | Redirected to confirm Email adress | Y | - |
| Log In | | | | |
| 1 | Click on Log In button | Redirection to Log In page | Y | - |
| 2 | Click on the Sign Up link in the form | Redirection to Sign Up page | Y | - |
| 3 | Enter valid email | Field will only accept email address format | Y | - |
| 4 | Enter valid password | Field will only accept password format | Y | - |
| 5 | Click on Log In button | Redirects user to profile page | Y | - |
| Log Out | | | | |
| 1 | Click log out link | Redirect to log out confirmation page | Y | - |
| 2 | Confirming log out | Redirects to home page | Y | - |
| Profiles page | | | | |
| 1 | Clicks links | Redirects to correct address | Y | - |
| 2 | Fill out form | Throws error if invalid | Y | - |
| 3 | Save valid form | Success message and profile updated | Y | - |
| 4 | Clicks order number in order history | Redirects to success page | Y | - |
| 5 | Click delete account button | Redirects to delete account confirmation page | Y | - |
| 6 | Page is responsive | Adapts to different screen sizes | Y | - |
| Delete account confirmation page | | | | |
| 1 | Enter password form | Deletes account | Y | - |

### Logged in administrator

Home page, products page, Profile page, Bag page, Checkout page and Checkout success page has the same functionality for an administrator as for a regular visitor/logged in user, those pages needs no further testing.

| Page    | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Product Details page | | | | |
| 1 | Clicks edit content | Redirected to edit content page | Y | Fields: Day, title, purpose, topics |
| 2 | Clicks edit description | Redirects to edit description page | Y | Fields: description, description_short, image, duration, perks, online_onsite, and price |
| 3 | Clicks delete | Triggers modal for confirmation | Y | - |
| 4 | Page is responsive | Adapts to different screen sizes | Y | - |
| Products Management page | | | | |
| 1 | Clicks links | Redirects to relevant address | Y | - |
| 2 | Page is responsive | Adapts to different screen sizes | Y | - |
| Product description page | | | | |
| 1 | Submit invalid form | Throws an error | Y | - |
| 2 | Submit valid form | Redirects to product content page | Y | - |
| Products content page | | | | |
| 2 | Submits valid form | Redirects to correct address | Y | - |
| 3 | Clicks add day button | Adds another form to fill out | Y | - |
| Order Management | | | | |
| 1 | Displays orders | With relevant information | Y | - |
| 2 | Clicks delete button | Triggers modal for order deletion | Y | Can only delete orders with invoice payment|
| 3 | Deletes order paid with card | Should throw an error | N | Bug - Future development |
| 4 | Page responsive | Adapts to different screen sizes | N | Not as I would like it, but administrators (finance) wont access this page with their phone (future development) |
| Newsletters | | | | |
| 1 | Filter by category | Displays relevant previous newsletters | Y | - |
| 2 | Clicks link | Redirects to relevant addresses | Y | - |
| 3 | Sends newsletters | Sends to users emails | Y | Only those who subscribes for the newsletter |
| 4 | Page is responsive | Adapts to different screen sizes | Y | - |
| Contact page | | | | |
| 1 | Clicks Add contact | Redirects to add contact page | Y | - |
| 2 | Submit invalid form | Throws error | Y | - |
| 3 | Submits valid form | Redirects to contact page | Y | - |
| Toasts messages | | | | |
| 1 | Displays top right corner | With user actions | Y | Bug - Message for redirecting user to sign when try to enter checkout as a not logged in user is not displaying (future development) |
| 2 | Message disappears automatically | After 3 seconds | Y | - |

## Testing User Stories

| ID | User Story  | Requirement met Y/N    | Image    |
|----|-------------|------------------------|----------|
| 1 | As a site user I can view a list of products so that I can select and add those I need for myself or my employees in the shippoing bag | Y | IMAGE HERE |
| 2 | As a site user I can see the program of the training I'm interested in so that I can understand what to expect of the training | Y | IMAGE HERE |
| 3 | As a site user I can search and filter trainings in different subjects, or by name or by description so that easily find what I'm looking for | Y | IMAGE HERE |
| 4 | As a site user I can view my shopping bag so that I can double check if i forgot something | Y | IMAGE HERE |
| 5 | As a site user I can check the order history so that I can go back and see when myself or an employee attended the training | Y | IMAGE HERE |
| 6 | As a site user I can register an account so that I can have a personal page to store my information and purchases | Y | IMAGE HERE |
| 7 | As a site user I can login and logout so that I can access my personal information | Y | IMAGE HERE |
| 8 | As a site user I can recover my password so that I can recover my account | IMAGE HERE |
| 9 | As a site user I can receive an email confirmation after registration so that I can verify that my account was successfully created | Y | IMAGE HERE |
| 10 | As a site user I can update or edit my account so that I can edit my information | Y | IMAGE HERE |
| 11 | As a site user I can delete my account so that I can remove it if I'm not longer using it | Y | IMAGE HERE |
| 12 | As a site user I can edit /update quantity of the product I've added so that I don't select the wrong number of products | Y | IMAGE HERE |
| 13 | As a site user I can delete a product from the shopping bag if I accidentally added the wrong product | Y | IMAGE HERE |
| 14 | As a site user I can add name and email of the participant on each training so that I can make sure they get an invite to the training | N | Future development |
| 15 | As a site user I can save my billing information so that I can reuse it without entering it again the next time | Y | IMAGE HERE |
| 16 | As a site user I can see the total cost of my shopping bag so that I make sure i don't go over budget | Y | IMAGE HERE |
| 17 | As a site user I can choose if I want to pay with card or bill so that I can make sure my payment is going to be handled the way I want it to | Y | IMAGE HERE |
| 18 | As a site user I can receive a order confirmation efter checkout so that I can see what i bought | Y | IMAGE HERE |
| 19 | As a site user I can receive a email confirmation after checkout so that I can get proof of my purchase | Y | IMAGE HERE |
| 20 | As a admin I can add, edit and delete categories so that I can keep them up to date | Y | IMAGE HERE |
| 21 | As a admin I can add, edit and delete products so that I can make sure the products are up to date | Y | IMAGE HERE |
| 22 | As a admin I can review customers orders so that I can add them to the CRM | Y | IMAGE HERE |
| 23 | As a administrator I can send newsletters to those users that subscribes so that they can receive information about new products and other relevant information | Y | IMAGE HERE |
| 24 | As a user I can subscribe to newsletters so that I can hear about new products and other relevant information regarding company training. | Y | IMAGE HERE |

---

## Validation

### HTML Validation

### CSS Validation

##### base.css

- Testing done in [W3C Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_uri).

- Pass with 4 warnings I don't want to change.

- [Full CSS Calidation Report]()

##### checkout.css

- Testing done in [W3C Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_uri).

- PASS with 1 warning I don't want to change.

- [Full CSS Validation report]()

### Python Validation

- Testing done in [CI Python Linter](https://pep8ci.herokuapp.com/).

- PASS with no errors.

- [Full Python Validation report]()

### JavaScript Validation

- Testing done in [JSHint](https://jshint.com/)

- PASS with no errors.

- [Full JavaScript Validation]()

---

## Stripe

I did not have time to implement webhooks for my project, though I have created the code I have nbot prioritized testing it. Implementing webhooks is for future development.

Since I choose to give the user two options on payment method and wanted it to be a obvious for the user what to do when chosing either option i implemented some javascript that listens to the users behaviour and render the relevant form accordingly to payment method i ran into some problems with the connection to Stripe. After lots of manual testing, debugging and help from tutor support at Code Instititue we figured out that the javascript that handles the payment methods didn't call the javascript that handles the submission of a card payment. When modifiying the javascript the card payment is successfull. 

IMAGE HERE

The card payment is successfull and works correctly, allthough I have a bug with payments created in Stripe as soon as the user enters the checkout page. Since the user is able to choose to pay with invoice I qould like the payment to be connected to Stripe by an event listener when the user choose card payment - future development.

IMAGE HERE

---

## Bugs
 
Below is a list of bugs and the relevant code.

1. Setting up real Emails
When deploying the project to Heroku and testing the real Emails it would throw a "OSError: [Errno 101] Network is unreachable" error. This was due to a compatibility issue with the version of python I'm running (version 3.12). To fix the issue i added a 'runtime.txt' and the line: ```python-3.9.18```. With that the deployed version on Heroku will recognize that as my version of python and the real Email worked.

2. Deploying to Heroku
When I deployed my project to Heroku I received an error in the Heroku build log saying "ERROR: Cannot install -r requirements.txt (line 3) and urllib3==2.0.7 because these package versions have conflicting dependencies.". To fix this I edited my requirements.txt file from this: ```urllib==2.0.7``` to: ```urllib```.

3. Form not rendering
On my contact form in my add contact function for administrators I could not get the form rendered in a Bootstrap 4 modal. Could not fix that, so I had to change approach and separate the form from in another template to make the form render correctly.

4. Images on products page
On the products page I wanted the images to be equaly sized so that the cards would appear the same over all cards. I fixed that by adding this the my css:
```
.card-img-container {
    height: 200px;
    overflow: hidden;
}

.card-img-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

5. Search function on products page
The search function is working fine when I enter a value that has a match in the products, but when there is no match the page doesent throw an error, which would be a good UX (future devlopment).

6. Initially, the company form was not displaying after submitting the profile update form. Adjusted the view to pass both forms to the template and reordered the HTML to display both forms consistently.

7. Some crispy forms are not working, throwing a AttributeError. Those forms are not fixed but I don't think it will affect the UX in short term but problem should be fixed in long term.

8. Faced a FieldError in the profiles/views.py related to the user_profile field when trying to display a user's profile. The issue was identified as a typo in the view. The correct field name is 'user' instead of 'user_profile'. Adjusted the view accordingly.

9. At first I had two separate apps for 'profiles' and 'companies' which gave me problems handling both forms in the checkout and in the profile. To fix it I deleted the 'companies' app and made the company infformation part of the 'profiles' app.

10. The topics in the product details page
The topics in the products detail page where displayed as JSON format. to fix it I needed to add this to the view: 
```
product_content.topics = [
    topic.strip(" '[]") for topic in topics.split(' ')
]
```

---
