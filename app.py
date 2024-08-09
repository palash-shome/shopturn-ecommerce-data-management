from flask import Flask
from flasgger import Swagger
from blueprints.home import home_bp
from blueprints.customers import customer_bp
from blueprints.address import address_bp
from blueprints.orderdetails import orderdetails_bp
from blueprints.orders import orders_bp
from blueprints.payments import payments_bp
from blueprints.products import products_bp
from blueprints.reviews import reviews_bp
from blueprints.processedCustomer import processed_customer_bp
from blueprints.processedProductReviews import processProductReviews_bp



app = Flask(__name__) 

#for api documentation
swagger=Swagger(app, config={
    'headers': [],
    'specs': [
        {
            'endpoint': 'apispec_1',
            'route': '/apispec_1.json',
            'rule_filter': lambda rule: True,  
            'model_filter': lambda tag: True,  
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/apidocs/'
})


#routes
app.register_blueprint(home_bp)
app.register_blueprint(customer_bp, url_prefix='/customers')
app.register_blueprint(address_bp, url_prefix='/address')
app.register_blueprint(orderdetails_bp, url_prefix='/orderdetails')
app.register_blueprint(orders_bp, url_prefix='/orders')
app.register_blueprint(payments_bp, url_prefix='/payments')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(reviews_bp, url_prefix='/reviews')
app.register_blueprint(processed_customer_bp, url_prefix='/processedcustomer')
app.register_blueprint(processProductReviews_bp, url_prefix='/processedproduct')



if __name__=='__main__':
    app.run(host='127.1.1.1',debug=True)
