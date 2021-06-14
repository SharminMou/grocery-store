from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/products', methods=['GET'])
def get_produtcs():
   products = products_dao.get_all_products_uom(connection)
   response = jsonify(products) #converted response into json
   response.headers.add('Access-Control-Allow-Origin', '*') #indicates whether the response can be shared with requesting code form the given origin
   return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
