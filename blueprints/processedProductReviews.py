from flask import Blueprint, jsonify
from startPreprocessing import averageReviews

process_data=[]

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
              average_rating:
                type: integer
                description: The rating given by the reviewer
                example: 5
              price:
                type: number
                description: The price of the product
                example: 55.09
              name:
                type: string
                description: The name of the product
                example: "Widget"
              description:
                type: string
                description: The description of the product
                example: "A handy gadget"
              created_at:
                type: string
                format: date-time
                description: The date and time when the review was created
                example: "30-01-2023 12:00:00"
      404:
        description: No processed reviews available
    """
    process_data = averageReviews()
    if process_data:
        
        return jsonify(process_data), 200
    return jsonify({'Error': 'No Products Listed'}), 404
