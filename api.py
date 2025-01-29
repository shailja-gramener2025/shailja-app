from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load student data from JSON file
with open("q-vercel-python.json") as f:
    students = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    
    # Debugging: print the names requested
    print(f"Requested names: {names}")
    
    # Case-insensitive name matching
    marks = [student["marks"] for student in students if student["name"].lower() in [n.lower() for n in names]]
    
    # Debugging: print the marks found
    print(f"Marks found: {marks}")
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
