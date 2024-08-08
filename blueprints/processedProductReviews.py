from flask import Blueprint, jsonify
from intermittentStorage.processProductsData import Processed_Product

processProductReviews_bp = Blueprint('processProductReviews', __name__)

@processProductReviews_bp.route('/reviews', methods=['GET'])
def getProcessedReviews():
    """
    Retrieves a list of processed product reviews.
    ---
    responses:
      200:
        description: A list of processed product reviews if available
        schema:
          type: array
          items:
            type: object
            properties:
              product_id:
                type: integer
                description: The unique identifier for the product
                example: 101
              review_id:
                type: integer
                description: The unique identifier for the review
                example: 1001
              review_text:
                type: string
                description: The text content of the review
                example: "Great product, very satisfied!"
              rating:
                type: integer
                description: The rating given by the reviewer
                example: 5
              created_at:
                type: string
                format: date-time
                description: The date and time when the review was created
                example: "2023-08-08T12:34:56Z"
      404:
        description: No processed reviews available
    """
    if Processed_Product:
        return jsonify(Processed_Product), 200
    return jsonify({'Error': 'No Products Listed'}), 404
