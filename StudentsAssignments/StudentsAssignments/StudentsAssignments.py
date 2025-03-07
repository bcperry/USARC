# import pandas lib as pd
import pandas as pd

from studentsassignments.StudentsAssigning import StudentsAssigning
from studentsassignments.StudentsLocationPreferences import StudentsLocationPreferences
from studentsprocessing.StudentsDataManagement import StudentsDataManagement

class StudentsAssignments:

    def __init__ (self): 
        self.dataManagement = StudentsDataManagement ()
        self.assigning = StudentsAssigning ()
        self.locationPreferences = StudentsLocationPreferences ()

    def initialize (self):
        self.readAllAssignmentData ()

        print ("Assignment Command initialization complete")

    def readAllAssignmentData (self):
        self.dataManagement.readStudentsAssignmentsPreferences ()
        self.dataManagement.readCompanyPreferences ()
        self.dataManagement.readAvailableJobPositions ()

    def fillEmptyAssignments (self):
        if self.dataManagement.getStudentsBranchPreferences () is None:
            raise ValueError("AssignmentCommand: fillEmptyAssignmentBranches: Input DataFrames 'studentsJobs' must not be None") 

        self.dataManagement.setAssignedStudentsJobs (self.assigning.fillEmptyAssignments (self.dataManagement.getStudentsBranchPreferences (), self.dataManagement.getIMTPreferences (), self.dataManagement.getBranchNumbers (), branchNumberOverfill = 10))
    
    def returnAssignmentsBranches (self):
        return self.dataManagement.convertStudentsAssignmentsToCSV ()

    def assignLocationByPreferences (self):
        for index, row in self.imtPreferenceList.iterrows(): 
            # Process each row from imtPreferenceList 
            print(f"IMT Preference row {index}: {row}")

            self.locationPreferences.matchAssignmentPreferencesAgainstLocations (self.dataManagement.getStudentsBranchPreferences ())

    def returnNumberOfAvaiableJobs (self):
        return self.dataManagement.convertNumberOfAvailableJobs ()