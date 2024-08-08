from datetime import datetime
from databases.Reviews import Reviews


def standardize_date_format(data, key):
    """
    Standardizes the date format in the given data.

    Args:
        data (list): A list of dictionaries containing date strings.
        key (str): The key in the dictionaries that holds the date string.

    Returns:
        list: The data with standardized date formats.
    """
    for item in data:
        if key in item:
            try:
                # Convert date from ISO 8601 format to desired format
                item[key] = datetime.strptime(item[key], "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y %H:%M:%S")
            except ValueError:
                # Handle parsing error if the date format is incorrect
                print(f"Error parsing date for item: {item}")
    return data


def average_rating(Reviews):

    """
    Calculate the average rating for each product based on the reviews.

    Args:
        reviews (list of dict): List of review dictionaries, each containing 'product_id' and 'rating'.

    Returns:
        dict: A dictionary with product IDs as keys and their average ratings as values.
    """

    product_rating = {}

    for review in Reviews:
        product_id = review['product_id']
        rating=review['rating']
        if product_id not in product_rating:
            product_rating[product_id]={"total_rating" : 0 , "count" : 0}
        product_rating[product_id]['total_rating']+=rating
        product_rating[product_id]['count']+=1


    average_ratings = {}
    for product_id, data in product_rating.items():
        average_ratings[product_id] = data['total_rating'] / data['count']

    return(average_ratings)
    
def process_data(data, transformation):
    """
    Process the given data by applying a transformation function to each string value.

    Args:
        data (dict): A dictionary containing the data to be processed. The transformation function is applied to each value in the dictionary if the value is a string.
        transformation (function): A function that takes a string and returns a transformed string.

    Returns:
        dict: A new dictionary with the same keys as `data`, but with transformed values for the string types.
    """
    processed_data = {}
    for key, value in data.items():
        processed_data[key] = transformation(value) if isinstance(value, str) else value
    return processed_data


def to_uppercase(value):
    """
    Convert a given string to uppercase.

    Args:
        value (str): The string to be converted to uppercase.

    Returns:
        str: The uppercase version of the input string. If the input is not a string, it is returned unchanged.
    """
    return value.upper()

def removeExtraSpaceFromLeft(value):
    """Remove Extra Spaces from the left side of a string

    Args:
        value (str): The string with extra spaces on left side

    Returns:
        str: The normal version of the input string. If the input is not a string, it is returned unchanged.
    """
    return value.lstrip()

def removeExtraSpaceFromRight(value):
    """Remove Extra Spaces from the right side of a string

    Args:
        value (str): The string with extra spaces on right side

    Returns:
        str: The normal version of the input string. If the input is not a string, it is returned unchanged.
    """
    return value.rstrip()