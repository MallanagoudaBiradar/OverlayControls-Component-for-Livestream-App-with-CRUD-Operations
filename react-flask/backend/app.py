from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dataBase'
mongo = PyMongo(app)

# CRUD Endpoints for Overlays
# Create
@app.route('/overlay/create', methods=['POST'])
def create_overlay():
    data = request.json
    mongo.db.overlays.insert_one(data)
    return jsonify({'message': 'Overlay created successfully'})

# Read
@app.route('/overlay/read', methods=['GET'])
def read_overlays():
    overlays = list(mongo.db.overlays.find())
    return jsonify({'overlays': overlays})

# Update
@app.route('/overlay/update/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    data = request.json
    mongo.db.overlays.update_one({'_id': overlay_id}, {'$set': data})
    return jsonify({'message': 'Overlay updated successfully'})

# Delete
@app.route('/overlay/delete/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    mongo.db.overlays.delete_one({'_id': overlay_id})
    return jsonify({'message': 'Overlay deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
