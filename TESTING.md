# TESTING

## Manual Testing

Testing has been done manually throughout the development. Testing has been done according to the criterias below and until the desired result was achieved.

Testing has been done on different devices to ensure there are no issues.


| Page    | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up     |                        |                  |      |             |
| 1           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 2           | Click on the Login link in the form | Redirection to Login page | Y |          |
| 3           | Enter valid email 2 times | Field will only accept email address format | Y |          |
| 4           | Enter valid password 2 times | Field will only accept password format | Y |          |
| Log In      |                        |                  |      |             |
| 1           | Click on Log In button | Redirection to Log In page | Y |          |
| 2           | Click on the Sign Up link in the form | Redirection to Sign Up page | Y |          |
| 3           | Enter valid email | Field will only accept email address format | Y |          |
| 4           | Enter valid password | Field will only accept password format | Y |          |
| 5           | Click on Log In button | Redirects user to blank In page | Y |          |
| Navigation  |                        |                  |      |             |
| 1           | Click on the logo | Redirection to home page | Y |          |
| 2           | Click Store | Redirection to Store page | Y |          |
| 3           | Click wishlist button | Redirection to wishlist page | Y |          |
| 4           | Click bag button | Redirection to bag page | Y |          |
| Admin Navigation |                        |                  |      |             |
| 1           | Click Personnel dashboard | Dropdown menu opens | Y |          |
| 2           | Click on Promo | Redirection to Promo page | Y |          |
| 3           | Click on Emails | Redirection to create email page | Y |          |
| 4           | Click Categories | Redirection to Categories page | Y |          |
| 5           | Click Brands | Redirection to Brands page | Y |          |
| Store |                        |                  |      |             |
| 1 | Type in search bar | Search results are displayed | Y |          |
| 2  | Select a category | Products are displayed | Y |          |
| Product Details |                        |                  |      |             |
| 1 | Click on left or right carousel | Carousel will change | Y | If there is only 1 image, there will be no arrow to click |
| 2 | Click on heart button | Product is added to wishlist and message will appear to notify user | Y | If user is logged out, the user will see a message to login and the click will be ignored |
| Profile |                        |                  |      |             |
| 1 | Click on the edit button | User will be redirected to the edit profile page | Y | |
| 2 | Click on the add address button | User will be redirected to the add address page | Y | |
| Edit Profile |                        |                  |      |             |
| 1 | Click on the edit button | User will see a pop up window to upload an avatar | Y | |
| 2 | Click on the upload button | User will see a pop up window to upload an avatar | Y | |
| Delete Account |                        |                  |      |             |
| 1 | Click on the Delete button | User will see a dropdown menu with the confirmation message | Y | |
| 2 | Click Yes button in the dropdown menu | User will be redirected to the home page and the message will appear to notify user | Y | |
| My Orders |                        |                  |      |             |
| 1 | Click on the order card | User will be redirected to the order page | Y | |
| Bag |                        |                  |      |             |
| 1 | Click on ready to purchase button | the page will smoothly scroll to the bottom of the page | Y | |
| 2 | Click on the product's name | User will be redirected to the product page | Y | |
| Checkout |                        |                  |      |             |
| 1 | Type in the Full name | Full name is changed | Y | If user has filled out the profile fully, the filled will be filled automatically |
| 2 | Type in the email | Email is changed | Y | |
| Checkout Success |                        |                  |      |             |
| 1 | Click on the View my orders button | User will be redirected to the My Orders page | Y | |
| Personnel Categories |                        |                  |      |             |
| 1 | Click on the add category button | User will be redirected to the add category page | Y | |
| 2 | Click on the edit button | User will be redirected to the edit category page | Y | |
| Personnel Add Category |                        |                  |      | Access only to administrators           |
| 1 | Type in the category name | Category name is changed | Y | |
| 2 | Check the category status | Category status is changed | Y | |
| Personnel Edit Category |                        |                  |      | Access only to administrators           |
| 1 | Render the category name | Category name is changed | Y | |
| 2 | Check the category status | Category status is changed | Y | |
| Personnel Delete Category |                        |                  |      | Access only to administrators           |
| 1 | Click on the cancel button | Changes will not be confirmed and the admin will be redirected to the categories page | Y | |
| Personnel Products |                        |                  |      | |
| 1 | Type in the product type name | Product type name is changed | Y | |
| Personnel Add Producuts |                        |                  |      | |
| 1 | Type in the product type name | Product type name is changed | Y | |
| Personnel Edit Products |                        |                  |      | |
| 1 | Type in the product type name | Product type name is changed | Y | |
| Personnel Delete Products |                        |                  |      | |
| 1 | Type in the product type name | Product type name is changed | Y | |
| Personnel Order Management |                        |                  |      | |
| 1 | Type in the product type name | Product type name is changed | Y | |
| Personnel Newsletters |                        |                  |      | |
| 1 | Type in the product type name | Product type name is changed | Y | |