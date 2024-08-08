# Shopturn E-commerce Data Management

## Description

The `shopturn-ecommerce-data-management` project provides a comprehensive solution for managing and preprocessing eCommerce data. This application includes functionalities for handling customer data, processing orders and payments, managing product reviews, and preprocessing data for consistency and analysis.

## Key Features

- **Customer Management**: Fetch, add, update, and process customer information.
- **Order and Payment Processing**: Retrieve and process order details and payment transactions.
- **Product Reviews**: Analyze and calculate average ratings for products.
- **Data Preprocessing**: Standardize and clean data using preprocessing scripts.
- **Modular Architecture**: Organized into blueprints and utility scripts for maintainability.

## Project Structure
**Root Directory**
app.py: The main entry point for the application. This script initializes and runs the Flask app.
folder_structure.txt: A file documenting the structure of the project.
startPreprocessing.py: Script to initiate preprocessing tasks for customer and product data.
requirements.txt: Lists the dependencies required for the project.

**blueprints/**
Contains Flask Blueprints that define different parts of the application’s routes and views:

address.py: Routes related to address management.
customers.py: Routes for handling customer-related operations.
home.py: Main or home routes.
orderdetails.py: Routes for managing order details.
orders.py: Routes for order management.
payments.py: Routes for payment processing.
processedCustomer.py: Handles routes related to processed customer data.
processedProductReviews.py: Routes for processed product reviews.
products.py: Routes for product management.
reviews.py: Routes for managing reviews.

**databases/**
Contains database models that define the schema for various entities:

Addresses.py: Database model for addresses.
Customers.py: Database model for customers.
OrderDetails.py: Database model for order details.
Orders.py: Database model for orders.
Payments.py: Database model for payments.
Products.py: Database model for products.
Reviews.py: Database model for reviews.

**intermittentStorage/**
Holds intermediate processed data that is used for further operations:

processCustomer.py: Contains data related to processed customers.
processProductsData.py: Contains data related to processed products.

**utility/**
Contains utility scripts for various helper functions:

helper.py: General helper functions used across the project.
preprocessing.py: Functions for data preprocessing tasks.

The folder structure is as follows :
```bash
Shopturn E-Commerce Data Management/
│
├── app.py
├── folder_structure.txt
├── startPreprocessing.py
├── requirements.txt
│
├── blueprints/
│   ├── address.py
│   ├── customers.py
│   ├── home.py
│   ├── orderdetails.py
│   ├── orders.py
│   ├── payments.py
│   ├── processedCustomer.py
│   ├── processedProductReviews.py
│   ├── products.py
│   └── reviews.py
│
├── databases/
│   ├── Addresses.py
│   ├── Customers.py
│   ├── OrderDetails.py
│   ├── Orders.py
│   ├── Payments.py
│   ├── Products.py
│   └── Reviews.py
│
├── intermittentStorage/
│   ├── processCustomer.py
│   └── processProductsData.py
│
└── utility/
    ├── helper.py
    └── preprocessing.py

```
## Getting Started

Follow these steps to set up and run the Flask application locally:

### 1. Clone the Repository

```bash
git clone https://github.com/palas-shome/shopturn-ecommerce-data-management.git
cd shopturn-ecommerce-data-management
```

### 2. Set Up a Virtual Environment
Create a virtual environment to isolate your project’s dependencies:
```bash 
python -m venv .venv
```

### 3. Activate the Virtual Environment
Activate the virtual environment:

## On Windows:
```bash 
.\.venv\Scripts\activate
```
## On macOS and Linux:
```bash 
source .venv/bin/activate
```

### 4. Install Dependencies
Install the required Python packages listed in requirements.txt:
```bash 
pip install -r requirements.txt
```

### 5. Run the Flask Application:
```bash 
python app.py
```

### 6. API Documentation available at 
```bash 
http://127.1.1.1:5000/apidocs/
```