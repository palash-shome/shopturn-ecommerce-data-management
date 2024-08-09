from flask import Blueprint, jsonify
from startPreprocessing import process_customers

data = []

processed_customer_bp = Blueprint('processed_customer', __name__)

@processed_customer_bp.route('/fetch', methods=['GET'])
def process_customer():
    """
    Retrieves a list of processed customer data.
    ---
    responses:
      200:
        description: A list of processed customer data if available
        schema:
          type: array
          items:
            type: object
            properties:
              customer_id:
                type: integer
                description: The unique identifier for the customer
                example: 1
              name:
                type: string
                description: The full name of the customer, combining first and last names
                example: "John Doe"
              email:
                type: string
                description: The email address of the customer
                example: "john.doe@example.com"
              created_at:
                type: string
                format: date-time
                description: The date and time when the customer was created
                example: "03-01-2023 12:00:00"
      404:
        description: No processed customer data available
    """

    data = process_customers()
    if data:
        return jsonify(data), 200
    return jsonify({'Error': 'No Customers Listed'}), 404
