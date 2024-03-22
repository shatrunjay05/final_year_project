from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['student_database']
collection = db['students']

# Endpoint to save student data
@app.route('/student', methods=['POST'])
def save_student():
    data = request.json
    if data:
        # Insert student data into MongoDB
        collection.insert_one(data)
        return jsonify({"message": "Student data saved successfully"}), 201
    else:
        return jsonify({"error": "No data provided"}), 400

# Endpoint to get list of all students
@app.route('/students', methods=['GET'])
def get_students():
    students = list(collection.find({}, {'_id': 0}))
    return jsonify(students), 200

if __name__ == '__main__':
    app.run(debug=True)
