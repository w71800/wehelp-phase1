import mysql.connector as connector
db = connector.connect(host="localhost", user="root", password="0000", database="website")
cursor = db.cursor()

def check_exist(username):
  sql = "SELECT username from member"
  cursor.execute(sql)
  signed_members = cursor.fetchall()
  signed_members = [ item[0] for item in signed_members ]
  if username in signed_members:
    return True
  else:
    return False