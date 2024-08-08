from databases.Customers import Customers
from databases.OrderDetails import OrderDetails
from databases.Orders import Orders
from databases.Reviews import Reviews
from databases.Products import Products
from databases.Payments import Payments

def findCustomers(customerId):
    """
    Find a customer by customer ID.

    Args:
        customerId (int): The ID of the customer to find.

    Returns:
        dict: The customer data if found, otherwise None.
    """
    for cust in Customers:
        if cust['customer_id'] == customerId:
            return cust
        
def addNewCustomer(data):
    """
    Add a new customer to the database.

    Args:
        data (dict): The customer data to add.

    Returns:
        None
    """
    Customers.append(data)

def findOrdersforCustomer(customerId):
    """
    Find all orders for a given customer ID.

    Args:
        customerId (int): The ID of the customer whose orders are to be found.

    Returns:
        list: A list of order details for the customer.
    """
    data = []
    for detail in OrderDetails:

        if detail['customer_id']==customerId:
            data.append(detail)
    return data

def getBillOfCustomer(customerId):
    """
    Get the billing details of a customer by customer ID.

    Args:
        customerId (int): The ID of the customer whose billing details are to be found.

    Returns:
        list: A list of billing details for the customer.
    """
    data = []
    for detail in Orders:

        if detail['customer_id']==customerId:
            data.append(detail)
    return data

def getPaymentDetaiilsOfCustomer(customerId):
    """
    Get the payment details of a customer by customer ID.

    Args:
        customerId (int): The ID of the customer whose payment details are to be found.

    Returns:
        list: A list of payment details for the customer.
    """
    data = []
    for detail in Payments:

        if detail['customer_id']==customerId:
            data.append(detail)
    return data

def findProducts(productName):
    """
    Get the payment details of a customer by customer ID.

    Args:
        customerId (int): The ID of the customer whose payment details are to be found.

    Returns:
        list: A list of payment details for the customer.
    """
    data = []
    for detail in Products:

        if detail['name']==productName.capitalize():
            data.append(detail)
    return data

def getReviewsOfProduct(productId):
    """
    Get reviews of a product by product ID.

    Args:
        productId (int): The ID of the product whose reviews are to be found.

    Returns:
        list: A list of reviews for the product.
    """
    data = []
    for detail in Reviews:

        if detail['product_id']==productId:
            data.append(detail)
    return data


