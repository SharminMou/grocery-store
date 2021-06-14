import datetime
import mysql.connector

cnx = None

def get_sql_connection():
  print("Creating mysql connection!")
  global cnx

  if cnx is None:
    cnx = mysql.connector.connect(user='root', password='abc123', database='grocery_store', auth_plugin='mysql_native_password')

  return cnx