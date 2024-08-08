import json
import requests
import pandas as pd
from utility.preprocessing import standardize_date_format, process_data, to_uppercase, average_rating


def process_customers():

    #api endpoint for fetch customer data 
    url = "http://127.1.1.1:5000/customers/all"

    #pulling custommer data from api
    data = requests.get(url)

    #extract the data
    response = json.loads(data.text)
    
    #restructuring the date format
    response = standardize_date_format(response, 'created_at')

    #create a pandas dataframe for further processing
    df = pd.DataFrame(response)

    # Creating a new column 'name' by combining 'first_name' and 'last_name'
    df['name'] = df['first_name'] + " " + df['last_name']

    # Remove the 'first_name' and 'last_name' columns
    df = df.drop(columns=['first_name', 'last_name'])

    #Reordering the columns
    df = df[['customer_id','name','email','created_at']]

    #additional converting the names to uppercase
    df['name'] = process_data(df['name'],to_uppercase)
    
    #convert dataframe to list
    processed_data = df.to_dict(orient='records')

    return processed_data

def averageReviews():

    review_url = "http://127.1.1.1:5000/reviews/all"
    product_url= "http://127.1.1.1:5000/products/all"

    reviews_data = requests.get(review_url)

    reviews_response = json.loads(reviews_data.text)
    #restructuring the date format
    reviews_response = standardize_date_format(reviews_response, 'created_at')
    df1 = pd.DataFrame(reviews_response)

    
    # Assuming your DataFrame is named df
    average_ratings_df = df1.groupby('product_id')['rating'].mean().reset_index()

    # Rename columns for clarity
    average_ratings_df.columns = ['product_id', 'average_rating']

    # fetch product data
    product_data = requests.get(product_url)

    product_response = json.loads(product_data.text)
    #restructuring the date format
    product_response = standardize_date_format(product_response, 'created_at')
    df2 = pd.DataFrame(product_response)

    merged_df = pd.merge(df2, average_ratings_df, on='product_id', how='outer')

    
    
     # Convert the DataFrame to a list of dictionaries
    return( merged_df.to_dict(orient='records'))

    



    




