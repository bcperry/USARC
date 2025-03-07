# import pandas lib as pd
import pandas as pd

from studentsassignments.StudentAssigning import StudentAssigning
from studentsassignments.StudentsLocationPreferences import StudentsLocationPreferences
from studentsprocessing.StudentsDataManagement import StudentsDataManagement

class StudentsAssignments:

    def __init__ (self): 
        self.dataManagement = StudentsDataManagement ()
        self.assigning = StudentAssigning ()
        self.locationPreferences = StudentsLocationPreferences ()

    def initialize (self):
        self.readAllAssignmentData ()

        print ("Assignment Command initialization complete")

    def readAllAssignmentData (self):
        self.dataManagement.readAssignmentBranchPreferences ()
        self.dataManagement.readIMTPreferences ()
        self.dataManagement.readBranchNumbers ()
#        self.dataManagement.readADNoneSelectNumbers ()

    def fillEmptyAssignmentBranches (self):
        if self.dataManagement.getAssignmentsBranchPreferences () is None:
            raise ValueError("AssignmentCommand: fillEmptyAssignmentBranches: Input DataFrames 'studentsBranches' must not be None") 
        else:
            print ("AssignmentCommand: fillEmptyAssignmentBranches: studentsBranches has records")

        assignments = self.assigning.fillEmptyAssignmentBranches (self.dataManagement.getAssignmentsBranchPreferences (), self.dataManagement.getIMTPreferences (), self.dataManagement.getBranchNumbers ())
#        self.setAssignmentsBranchPreferences (assignments)
    
    def returnAssignmentsBranches (self):
        return self.dataManagement.convertAssignmentsBranchesToJSON ()

    def assignLocationByPreferences (self):
        for index, row in self.imtPreferenceList.iterrows(): 
            # Process each row from imtPreferenceList 
            print(f"IMT Preference row {index}: {row}")

            self.locationPreferences.matchAssignmentPreferencesAgainstLocations (self.dataManagement.getAssignmentsBranchPreferences ())
