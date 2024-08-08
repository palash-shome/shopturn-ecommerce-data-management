from flask import jsonify, Blueprint
from utility.helper import getBillOfCustomer

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/generatebill/<int:customerId>', methods=['GET'])
def orders(customerId):
    """
    Retrieves bill amount for orders for a customer based on Customer ID.
    ---
    parameters:
      - name: customerId
        in: path
        type: integer
        required: true
        description: The unique identifier for the customer.
    responses:
      200:
        description: Bill details of the customer if present
        schema:
          type: object
          properties:
            customer_id:
              type: integer
              description: The customer ID
              example: 1
            total_amount:
              type: number
              description: The total amount of the bill for the orders
              example: 199.99
            currency:
              type: string
              description: The currency of the bill amount
              example: "USD"
            billing_date:
              type: string
              format: date-time
              description: The date and time when the bill was generated
              example: "2023-08-08T12:34:56Z"
      404:
        description: No orders found for the customer
    """
    data = getBillOfCustomer(customerId)
    if data:
        return jsonify(data), 200
       
    return jsonify({"error": "No orders found for Customer"}), 404
