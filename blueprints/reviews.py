from flask import jsonify, Blueprint
from utility.helper import getReviewsOfProduct
from databases.Reviews import Reviews

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/given/<int:productId>', methods=['GET'])
def reviews(productId):
    """
    Retrieves reviews of the product posted by customers based on Product ID.
    ---
    parameters:
      - name: productId
        in: path
        type: integer
        required: true
        description: The unique identifier for the product.
    responses:
      200:
        description: Reviews of the product if present
        schema:
          type: array
          items:
            type: object
            properties:
              review_id:
                type: integer
                description: The review ID
                example: 101
              product_id:
                type: integer
                description: The product ID
                example: 1
              customer_id:
                type: integer
                description: The customer ID who posted the review
                example: 5
              rating:
                type: integer
                description: The rating given by the customer
                example: 4
              comment:
                type: string
                description: The review comment by the customer
                example: "Great product, highly recommend!"
              review_date:
                type: string
                format: date-time
                description: The date and time when the review was posted
                example: "2023-08-08T12:34:56Z"
      404:
        description: No reviews listed for the product
    """
    data = getReviewsOfProduct(productId)

    if data:
        return jsonify(data), 200
    return jsonify({"error": "No Reviews listed for Product"}), 404



@reviews_bp.route('/all', methods=['GET'])
def getAllReviews():
    """
    Retrieves a list of all reviews.
    ---
    responses:
      200:
        description: A list of all reviews if available
        schema:
          type: array
          items:
            type: object
            properties:
              review_id:
                type: integer
                description: The unique identifier for the review
                example: 1
              product_id:
                type: integer
                description: The unique identifier for the product
                example: 101
              customer_id:
                type: integer
                description: The unique identifier for the customer who posted the review
                example: 1
              rating:
                type: integer
                description: The rating given by the customer
                example: 5
              comment:
                type: string
                description: The comment provided by the customer
                example: "Great product!"
              created_at:
                type: string
                format: date-time
                description: The date and time when the review was posted
                example: "2023-08-08T12:34:56Z"
      404:
        description: No reviews listed
    """
    if Reviews:
        return jsonify(Reviews), 200
    return jsonify({'Error': 'No Reviews Listed'}), 404
