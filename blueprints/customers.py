from flask import jsonify, Blueprint, request
from databases.Customers import Customers
from utility.helper import findCustomers, addNewCustomer

customer_bp = Blueprint('customers', __name__)

@customer_bp.route('/all', methods=['GET'])
def allCustomer():
    """
    Retrieves a list of all customers.
    ---
    responses:
      200:
        description: A list of all customers if available
        schema:
          type: array
          items:
            type: object
            properties:
              customer_id:
                type: integer
                description: The unique identifier for the customer
                example: 1
              first_name:
                type: string
                description: The first name of the customer
                example: "John"
              last_name:
                type: string
                description: The last name of the customer
                example: "Doe"
              email:
                type: string
                description: The email address of the customer
                example: "john.doe@example.com"
              phone:
                type: string
                description: The phone number of the customer
                example: "+1234567890"
              created_at:
                type: string
                format: date-time
                description: The date and time when the customer was created
                example: "2023-08-08T12:34:56Z"
      404:
        description: No customers listed
    """
    if Customers:
        return jsonify(Customers), 200
    return jsonify({'Error': 'No Customers Listed'}), 404


@customer_bp.route('/fetch/<int:customerId>', methods=['GET'])
def getCustomer(customerId):
    """
    Retrieve customer information based on customer ID.
    ---
    parameters:
      - name: customerId
        in: path
        type: integer
        required: true
        description: The unique identifier for the customer.
    responses:
      200:
        description: Customer details if found
        schema:
          type: object
          properties:
            customer_id:
              type: integer
              description: The customer ID
              example: 1
            first_name:
              type: string
              description: The first name of the customer
              example: "John"
            last_name:
              type: string
              description: The last name of the customer
              example: "Doe"
            email:
              type: string
              description: The email address of the customer
              example: "john.doe@example.com"
            phone:
              type: string
              description: The phone number of the customer
              example: "+1234567890"
            created_at:
              type: string
              format: date-time
              description: The date and time when the customer was created
              example: "2023-08-08T12:34:56Z"
      404:
        description: Customer not found
    """
    data = findCustomers(customerId)
    if data:
        return jsonify(data)
    
    # If no customer is found
    return jsonify({"error": "Customer not found"}), 404


@customer_bp.route('/add', methods=['POST'])
def addCustomer():
    """
    Add a new customer to the customer list.
    ---
    parameters:
      - name: customer
        in: body
        required: true
        schema:
          type: object
          properties:
            customer_id:
              type: integer
              description: The unique identifier for the customer.
              example: 1
            first_name:
              type: string
              description: The first name of the customer.
              example: "John"
            last_name:
              type: string
              description: The last name of the customer.
              example: "Doe"
            email:
              type: string
              description: The email address of the customer.
              example: "john.doe@example.com"
            phone:
              type: string
              description: The phone number of the customer.
              example: "+1234567890"
            created_at:
              type: string
              format: date-time
              description: The date and time when the customer was created.
              example: "2023-08-08T12:34:56Z"
    responses:
      201:
        description: Customer successfully added
        schema:
          type: object
          properties:
            customer_id:
              type: integer
              description: The customer ID
              example: 1
            first_name:
              type: string
              description: The first name of the customer
              example: "John"
            last_name:
              type: string
              description: The last name of the customer
              example: "Doe"
            email:
              type: string
              description: The email address of the customer
              example: "john.doe@example.com"
            phone:
              type: string
              description: The phone number of the customer
              example: "+1234567890"
            created_at:
              type: string
              format: date-time
              description: The date and time when the customer was created
              example: "2023-08-08T12:34:56Z"
      400:
        description: Bad request due to invalid input or existing customer ID
    """
    # Get data from request
    data = request.json

    # Validate required fields
    required_fields = ['customer_id', 'first_name', 'last_name', 'email', 'phone', 'created_at']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if customer_id already exists
    if findCustomers(data['customer_id']):
        return jsonify({"error": "Customer ID already exists"}), 400

    # Add new customer to the list
    addNewCustomer(data)
    
    # Return the newly added customer
    return jsonify(data), 201
