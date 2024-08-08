from flask import jsonify, Blueprint
from utility.helper import getPaymentDetaiilsOfCustomer

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/paid/<int:customerId>', methods=['GET'])
def payments(customerId):
    """
    Retrieves payment details for a customer based on Customer ID.
    ---
    parameters:
      - name: customerId
        in: path
        type: integer
        required: true
        description: The unique identifier for the customer.
    responses:
      200:
        description: Bill payment details of the customer if found
        schema:
          type: object
          properties:
            customer_id:
              type: integer
              description: The customer ID
              example: 1
            order_id:
              type: integer
              description: The order ID
              example: 101
            payment_amount:
              type: number
              description: The amount paid by the customer
              example: 99.99
            payment_date:
              type: string
              format: date
              description: The date when the payment was made
              example: "2023-08-08"
      404:
        description: No orders found for the customer
    """
    data = getPaymentDetaiilsOfCustomer(customerId)
    if data:
        return jsonify(data), 200
       
    return jsonify({"error": "No orders found for Customer"}), 404
