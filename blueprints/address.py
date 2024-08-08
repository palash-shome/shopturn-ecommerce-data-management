from flask import jsonify, request, Blueprint
from databases.Addresses import Address


address_bp = Blueprint('address',__name__)

@address_bp.route('/load/<int:customerId>', methods=['GET'])
def getAddress(customerId):
    """
    Retrieve address information based on customer ID.
    ---
    parameters:
      - name: customerId
        in: path
        type: integer
        required: true
        description: The unique identifier for the customer to address relationship.
    responses:
      200:
        description: Address details if the customer is found
        schema:
          type: object
          properties:
            customer_id:
              type: integer
              description: The customer ID
            address:
              type: string
              description: The customer address
      404:
        description: Customer not found
    """
       
    for addr in Address:
        if addr['customer_id']==customerId:
            return addr,200
    return jsonify({"error": "Customer not found"}), 404
