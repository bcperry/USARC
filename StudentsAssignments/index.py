from flask import Flask, jsonify, request

from flask import Response
from studentsassignments.StudentsAssignments import StudentsAssignments

import pandas as pd

app = Flask(__name__)

# Instantiate student command class for usage
studentAssignments = StudentsAssignments ()

# Initialize student command with all required data and input
studentAssignments.initialize ()

@app.route('/initialize')
def initialize ():
    studentAssignments.initialize ()

#    return utilities.testOutput (), 200, {'ContentType':'text/html'}

    return  "Student Assignments initialized", 200, {'ContentType':'text/html'}

@app.route('/studentsassignments')
def studentBAssigning ():
    studentAssignments.fillEmptyAssignments ()
   
    return studentAssignments.returnAssignmentsBranches (), 200, {'ContentType':'text/html'}

#    return  "Student branching complete", 200, {'ContentType':'text/html'}


@app.route('/studentslocationpreferences')
def studentLocationPreferences ():
    studentAssignments.assignLocationByPreferences ()

    return  "Student location preferences complete", 200, {'ContentType':'text/html'}

@app.route ('/numberofavaiablejobs')
def numberOfAvaiableJobs ():
    return studentAssignments.returnNumberOfAvaiableJobs (), 200, {'ContentType':'text/html'}


""" 
@app.route('/processBranches')
def processBranches():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return "", 204


@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 204
 """

if __name__ == "__main__":
    app.run()