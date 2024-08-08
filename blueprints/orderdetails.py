from flask import jsonify, request, Blueprint
from utility.helper import findOrdersforCustomer

orderdetails_bp = Blueprint('orderdetails', __name__)

@orderdetails_bp.route('/incart/<int:customerId>', methods=['GET'])
def getOrderDetails(customerId):
    """
    Retrieves order details for a customer based on Customer ID.
    ---
    parameters:
      - name: customerId
        in: path
        type: integer
        required: true
        description: The unique identifier for the customer.
    responses:
      200:
        description: Order details of the customer if present
        schema:
          type: object
          properties:
            order_id:
              type: integer
              description: The order ID
              example: 123
            product_name:
              type: string
              description: The name of the product in the order
              example: "Widget"
            quantity:
              type: integer
              description: The quantity of the product ordered
              example: 2
            total_price:
              type: number
              description: The total price for the order
              example: 39.98
            order_date:
              type: string
              format: date-time
              description: The date and time when the order was placed
              example: "2023-08-08T12:34:56Z"
      404:
        description: No orders found in Cart for Customer
    """
    data = findOrdersforCustomer(customerId)
    if data:
        return jsonify(data), 200
       
    return jsonify({"error": "No orders found in Cart for Customer"}), 404
