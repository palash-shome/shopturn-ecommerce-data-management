from flask import jsonify, Blueprint
from utility.helper import findProducts
from databases.Products import Products

products_bp = Blueprint('products', __name__)

@products_bp.route('/fetch/<string:productName>', methods=['GET'])
def products(productName):
    """
    Retrieves product details based on product name.
    ---
    parameters:
      - name: productName
        in: path
        type: string
        required: true
        description: The name of the product.
    responses:
      200:
        description: Product information if found
        schema:
          type: object
          properties:
            product_id:
              type: integer
              description: The product ID
              example: 1
            product_name:
              type: string
              description: The name of the product
              example: "Widget"
            price:
              type: number
              description: The price of the product
              example: 19.99
            stock:
              type: integer
              description: The number of items in stock
              example: 100
      404:
        description: Product not found
    """
    data = findProducts(productName)
    if data:
        return jsonify(data), 200
       
    return jsonify({"error": "Sorry this item is out of stock"}), 404



@products_bp.route('/all', methods=['GET'])
def getAllProducts():
    """
    Retrieves a list of all products.
    ---
    responses:
      200:
        description: A list of all products if available
        schema:
          type: array
          items:
            type: object
            properties:
              product_id:
                type: integer
                description: The unique identifier for the product
                example: 101
              product_name:
                type: string
                description: The name of the product
                example: "Widget"
              price:
                type: number
                description: The price of the product
                example: 19.99
              stock:
                type: integer
                description: The number of items available in stock
                example: 100
              created_at:
                type: string
                format: date-time
                description: The date and time when the product was added
                example: "2023-08-08T12:34:56Z"
      404:
        description: No products listed
    """
    if Products:
        return jsonify(Products), 200
    return jsonify({'Error': 'No Products Listed'}), 404
