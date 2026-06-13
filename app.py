from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "James",
        "age": 20,
        "college": "ABC College",
        "branch": "Computer Science"
    },
    {
        "id": 2,
        "name": "John",
        "age": 21,
        "college": "XYZ College",
        "branch": "Mechanical Engineering"
    },
    {
        "id": 3,
        "name": "Sarah",
        "age": 19,
        "college": "PQR College",
        "branch": "Electronics"
    },
    {
        "id": 4,
        "name": "David",
        "age": 22,
        "college": "LMN College",
        "branch": "Civil Engineering"
    },
    {
        "id": 5,
        "name": "Emma",
        "age": 20,
        "college": "DEF College",
        "branch": "Information Technology"
    }
]

@app.route('/students')
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)