from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "James", "age": 20, "college": "ABC College"},
    {"id": 2, "name": "John", "age": 21, "college": "XYZ College"},
    {"id": 3, "name": "Emma", "age": 19, "college": "DEF College"}
]

@app.route('/search-student/<name>')
def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return jsonify(student)

    return jsonify({"message": "Student not found"})

if __name__ == '__main__':
    app.run(debug=True)