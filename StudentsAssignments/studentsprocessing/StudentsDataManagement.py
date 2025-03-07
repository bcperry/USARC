# import pandas lib as pd
from flask import Flask, jsonify
from io import StringIO

from utilities.StudentsAssignmentsUtilities import StudentsAssignmentsUtilities

import pandas as pd


class StudentsDataManagement:
    utilities = StudentsAssignmentsUtilities ()
    filePath = "C:\\Projects\\Proof of Concept\\Data\\"

    def __init__ (self): 
        self.utilities = StudentsAssignmentsUtilities () 
        self.studentJobs = None
        self.assignedStudentsJobs = None
        self.imtPreferenceList = None 
        self.jobNumbers = None
        self.adNonSelectNumbers = None
        self.sortedStudentsJobPreferences = None

    def readADNoneSelectNumbers (self):
        self.adNonSelectNumbers = self.utilities.readExcel (self.filePath + "Available Job Positions.xlsx")

        # THe raw file does not contain column names so assign names to them
        self.adNonSelectNumbers = self.adNonSelectNumbers.sort_values(by=[2]).loc[:, [2, 1]]
        self.adNonSelectNumbers.columns = ['RCMS_Vacancy', 'JOB_CD', 'Vacancies_RCMS']
 
    def readCompanyPreferences (self):
        self.jobNumbers = self.utilities.readExcel (self.filePath + "Second Round Available Job Positions.xlsx")
 
        # The raw file does not contain column names so assign names to them
        self.jobNumbers.columns = ['JobType', 'Vacancies_RCMS', 'JobCode']

        # Ensure the column 'Vacancies_RCMS' exists
        if 'Vacancies_RCMS' not in self.jobNumbers.columns:
            raise KeyError("'Vacancies_RCMS' column is not found after renaming.")
        
    def readStudentsAssignmentsPreferences (self):
        self.studentJobs = self.utilities.readExcel (self.filePath + "Students Preferences.xlsx")
        
        self.studentJobs['UniqueID'] = self.studentJobs.apply(lambda row: f"{row['StudentID']}-{row['LastName']}", axis=1)

        if self.studentJobs is None:
            raise ValueError("StudentDataManagement: readStudentBranchPreferences: Input DataFrames 'studentJobs' must not be None") 
        else:
            print ("StudentDataManagement: readStudentBranchPreferences: studentJobs has records")

        print(self.studentJobs.columns.tolist())

    def readAvailableJobPositions (self):
        self.imtPreferenceList = self.utilities.readExcel (self.filePath + "Available Job Positions.xlsx")

        if self.imtPreferenceList is None:
            raise ValueError("StudentDataManagement: readIMTPreferences: Input DataFrames 'imtPreferenceList' must not be None") 
        else:
            print ("StudentDataManagement: readIMTPreferences: imtPreferenceList has records")

        print(self.imtPreferenceList.columns.tolist())

    def convertStudentsBranchesToJSON (self):
        # Convert DataFrame to JSON
        return jsonify (self.assignedStudentsJobs.to_json (orient='records'))
    
    def convertStudentsAssignmentsToCSV (self):
       csv_buffer = StringIO ()

       self.assignedStudentsJobs.to_csv(csv_buffer, index=False)

       return csv_buffer.getvalue ()

    def convertNumberOfAvailableJobs (self):
       csv_buffer = StringIO ()

       self.imtPreferenceList.to_csv(csv_buffer, index=False)

       return csv_buffer.getvalue ()

    def getADNoneSelectNumbers (self):
        return self.adNonSelectNumbers
    
    def getAssignedStudentsJobs (self):
        return self.assignedStudentsJobs
        
    def getBranchNumbers (self):
        return self.jobNumbers

    def getNumberOfAvailableJobs (self):
        return self.imtPreferenceList
    
    def getStudentsBranchPreferences (self): 
         return self.studentJobs 

    def setStudentsBranchPreferences (self, studentJobs) :
        self.studentJobs = studentJobs

    def setAssignedStudentsJobs (self, assignedStudentsJobs):
        self.assignedStudentsJobs = assignedStudentsJobs

    def getIMTPreferences (self): 
        return self.imtPreferenceList

    def setSortedJobPreferences (self, jobPreference):
        self.sortedStudentsJobPreferences = jobPreference
