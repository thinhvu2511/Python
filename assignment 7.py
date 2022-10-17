import json
from flask import Flask, jsonify, render_template, request
import pandas as pd
import csv
from flask_csv import*

app = Flask(__name__)

class Student:
    def __init__(self, code, name, math):
        self.code = code
        self.name = name
        self.math = math
    

def read_list_from_csv():
    students = []
    with open('test.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in list(reader)[1:]:
            students.append(Student(row[0], row[1], row[2]))
    return students

def write_list_to_csv(students):
    fields = ['No', 'Name', 'Math']
    with open('test.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(fields)
        for student in students:
            write.writerow([student.code, student.name, student.math])

@app.route('/')
def data():
    # pd.read_csv('test.csv').to_json('student.json')
    # with open('student.json', 'r') as file:
    #     students = json.load(file)
    # return jsonify(students)
    students = read_list_from_csv()
    return json.dumps(students, default=vars)


@app.route('/create', methods=['POST'])
def create():
    request_data = request.get_json()
    with open('test.csv', 'a', newline='') as f_object:
        writer = csv.writer(f_object)
        writer.writerow([request_data['code'], request_data['name'], request_data['math']])
        f_object.close()
    return "Create Successfully"


@app.route('/update/<int:code>', methods=['POST'])
def update(code):
    request_data = request.get_json()
    students = read_list_from_csv()
    update_student = [student for student in students if student.code == str(code)][0]
    update_student.name = request_data['name']
    update_student.math = request_data['math']
    write_list_to_csv(students)
    return "Update successfully"


@app.route('/get/<int:code>')
def get(code):
    students = read_list_from_csv()
    get_student = [student for student in students if student.code == str(code)][0]
    return json.dumps(get_student, default=vars)


@app.route('/delete/<int:code>', methods=['DELETE'])
def delete(code):
    students = read_list_from_csv()
    students.remove([student for student in students if student.code == str(code)][0]) 
    write_list_to_csv(students)
    return "Delete Successfully"


if __name__ == '__main__':
    app.run(debug=True)

# # pd.read_json('test.json').to_csv('test.csv')
# data = pd.read_csv('test.csv')
# pd.read_csv('test.csv').to_json('new.json')


