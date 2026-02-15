#task 1 completed
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
# TODO: Replace the string below with your actual MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://sachin85085_db_user:<12Prince>@cluster0.3a00rnp.mongodb.net/?appName=Cluster0"

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client.get_database('flask_db')   # Use a database named 'flask_db'
    collection = db.users                  # Use a collection named 'users'
    print("Connected to MongoDB!")
except Exception as e:
    print("Error connecting to MongoDB:", e)


# --- TASK 1: API Route ---
@app.route('/api')
def get_api_data():
    # Read data from the backend file (data.json)
    file_path = os.path.join(app.root_path, 'data.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


# --- TASK 2: Form & MongoDB ---
@app.route('/', methods=['GET', 'POST'])
def home():
    error_message = None

    if request.method == 'POST':
        # Get data from the form
        user_name = request.form.get('username')
        user_email = request.form.get('email')

        try:
            # Insert into MongoDB
            collection.insert_one({"name": user_name, "email": user_email})
            
            # Redirect to success page upon successful submission
            return redirect(url_for('success'))
            
        except Exception as e:
            # If error, stay on page and show error message
            error_message = f"Submission Failed: {e}"

    return render_template('index.html', error=error_message)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)