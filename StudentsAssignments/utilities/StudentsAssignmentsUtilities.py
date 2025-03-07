# import pandas lib as pd
import pandas as pd

class StudentsAssignmentsUtilities:

    def readExcel (self, path):
        # read by default 1st sheet of an excel file
        excelContents = pd.read_excel (path)

        return excelContents

    def testOutput (self):
        return "Instantiated StudentsAssignmentsUtilities"
    

