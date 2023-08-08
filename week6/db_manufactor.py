import mysql.connector as connector
db = connector.connect(host="localhost", user="root", password="ww171717", database="website")
cursor = db.cursor()