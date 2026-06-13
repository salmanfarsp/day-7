from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return "Flask is working"

@app.route('/add-student', methods=['POST'])
def add_student():
    student = request.get_json()
    students.append(student)

    return jsonify({
        "message": "Student Added Successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)