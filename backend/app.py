from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS  # Required to allow requests from the Frontend

app = Flask(__name__)
CORS(app) # Enables CORS so that the Frontend can communicate with this API

# --- MongoDB Connection ---
# Replace <PASSWORD> with your actual MongoDB password
client = MongoClient("mongodb+srv://sachin85085_db_user:<PASSWORD>@cluster0.3a00rnp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['flask_db']
collection = db['users']

@app.route('/')
def home():
    return "Backend is Running Successfully!"

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.json  # Extracts JSON data sent from the Frontend
        username = data.get('username')
        
        if not username:
            return jsonify({"message": "Username is required", "status": "error"}), 400

        # Save data to the MongoDB collection
        collection.insert_one({"username": username})
        return jsonify({"message": "Data Saved to MongoDB!", "status": "success"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # The server will run on port 5000 by default
    app.run(host='0.0.0.0', port=5000, debug=True)