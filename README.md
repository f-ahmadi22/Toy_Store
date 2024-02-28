# Toy_Store

Welcome to the Toy Store project! This Django project is designed to manage a toy store with features for blogging, product management, shopping cart functionality, and payment processing.

# Install dependencies 
pip install -r requirements.txt

# Features
# Blog App
    Manage blog categories, posts, comments, and media content.
    Use Django admin interface for easy content management.

    Endpoints :
        Get all or detailed categories :  'blog/categories/'
        Get all or detailed posts :  'blog/posts/'
        Get all comments and submit comment :  'blog/comments/'
        ** submit comment needs token authentication, so user needs to login
    


# Store App
    Manage products, categories, pricing and comments. 

    Endpoints :
        Get all or detailed categories :  'store/categories/'
        Get all or detailed products :  'store/products/'
        Get all comments and submit comment :  'store/comments/'
        ** submit comment needs token authentication, so user needs to login


# Cart App
    Enable users to add items to their shopping cart.

    Endpoints :
        Add a product to user's cart : 'cart/'  pass product id in body
        ** It needs token authentication, so user needs to login


# Financial App
    Enable users to  pay their shopping carts and see all their payments.

    Endpoints :
        Get all or detailed payments :  'financial/payments/'
        pay a user's cart : 'financial/pay/'  pass cart id in body
        ** It needs token authentication, so user needs to login



# Authentication
    For token authentication user needs to sign up and login to get token.
    It gets username and password fields.

    Endpoints :
        signup :  'auth/signup/'
        login : 'auth/login/'
