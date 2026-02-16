import os
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# --- MongoDB Connection Setup ---
client = MongoClient("mongodb+srv://sachin85085_db_user:12Prince@cluster0.3a00rnp.mongodb.net/?appName=Cluster0")
db = client['flask_db']
collection = db['users']

# --- TASK 1: API Route ---
@app.route('/api')
def get_api_data():
    file_path = os.path.join(app.root_path, 'data.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

# --- TASK 2: Home Form & MongoDB ---
@app.route('/', methods=['GET', 'POST'])
def home():
    error_message = None
    if request.method == 'POST':
        user_name = request.form.get('username')
        user_email = request.form.get('email')
        try:
            # This line must be indented (pushed right)
            collection.insert_one({"name": user_name, "email": user_email})
            return redirect(url_for('success'))
        except Exception as e:
            error_message = f"Submission Failed: {e}"
    return render_template('index.html', error=error_message)

@app.route('/success')
def success():
    return render_template('success.html')

# --- TASK 3: To-Do List Routes ---
@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')
    collection.insert_one({'name': item_name, 'desc': item_desc})
    return "To-Do Item Added Successfully!"

# --- SERVER START (Keep this at the very bottom) ---
if __name__ == '__main__':
    app.run(debug=True)