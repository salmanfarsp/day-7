from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "John", "course": "Python"},
    {"id": 2, "name": "Sara", "course": "Java"},
    {"id": 3, "name": "Ali", "course": "Web Development"}
]

@app.route('/students/<int:id>')
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)