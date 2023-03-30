# Django Marketplace

Django Marketplace is a simple e-commerce platform built with Django that allows users to buy and sell products in a manner similar to eBay. However, unlike eBay, buyers cannot directly purchase items from sellers on the platform. Instead, buyers must send a message to the seller expressing their interest in the item and negotiate a sale through private messages.

The platform is designed to be user-friendly, with an intuitive interface that makes it easy to search for and browse items. Sellers can create listings for their products, set their own prices, and manage their inventory. Buyers can search for items by category, keyword, or seller, and can communicate with sellers directly through the platform's messaging system.

## Installation

1. Clone the repository: `git clone https://github.com/Ikromjon1998/django-marketplace.git`
2. Navigate to the project directory: `cd django-marketplace/djangoMarketplace`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment:
   - On macOS or Linux: `source env/bin/activate`
   - On Windows: `.\env\Scripts\activate`
5. Install pip:
   - If you don't have pip installed already, you can install it using the following command: `python get-pip.py`
6. Install Django: `pip install django`
7. Install Python Imaging Library - Pillow: `pip install Pillow`
8. Make migrations: `python manage.py makemigrations`
   - Create the database tables by making migrations.
9. Apply migrations: `python manage.py migrate`
   - Apply the migrations to the database.
10. Run the server: `python manage.py runserver`
    - The project should now be running at `http://localhost:8000/`.
    - To view the project, open a web browser and go to `http://localhost:8000/`.
