from flask import Flask, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Use your MongoDB Atlas connection string
# Make sure to replace <password> with your actual password and consider using environment variables for better security practices
mongo_uri = "mongodb+srv://admin:admin@cluster0.fda6te7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client.userdb  # Assuming 'userdb' is your database name

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    db.users.insert_one({"name": name, "email": email})  # Assuming 'users' is your collection name
    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
