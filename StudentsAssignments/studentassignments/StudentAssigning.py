# import pandas lib as pd
import pandas as pd
import numpy as np

from studentsassignments.JobConstants import JobConstants

class StudentAssigning:

    def fillEmptyStudentBranches (self, studentJobs, imtPriorities, branchNumbers, noneSelects = None, adNonSelectNumbers = None, branchNumberOverfill = 1):
        # If nonSelects is not None, then append the noneSelects to the studentJobs
        if noneSelects is not None:
            # Concatenate noneSelects to studentJobs
            studentJobs = pd.concat ([studentJobs, noneSelects], ignore_index = True)

        # Arrange the cadet preferences in order of what IMT gives us if they only order some of the assignments
        for Student in studentJobs['UniqueID'].unique(): 
            # Get the row that the cadet is on in cadetBranches 
            cadetRow = studentJobs[studentJobs['UniqueID'] == Student].copy() 
            
            # Remove everything except their branch preferencing 
            cadetRow = cadetRow.loc[:, JobConstants.FIRST_MOS_COL:JobConstants.LAST_MOS_COL].dropna(axis=1).transpose().reset_index()

            cadetRow.columns = ['index', 'V1'] 
            cadetRow = cadetRow.sort_values(by='V1').reset_index(drop=True) 
            
            # Remove the assignments that have already been ordered and keep only the assignments that the cadet has not ordered 
            imtPriorities2 = imtPriorities[~imtPriorities['MOS'].isin(cadetRow['index'])].copy() 
            imtPriorities2['V1'] = range(len(cadetRow), len(cadetRow) + len(imtPriorities2)) 
            imtPriorities2.rename(columns={'MOS': 'index'}, inplace=True) 
            
            # Preserve the order of preference for the cadet and then also order the rest of the assignments for them that have not been preferenced 
            cadet_preferences = pd.concat([cadetRow, imtPriorities2], ignore_index=True).sort_values(by='index').reset_index(drop=True) 
            
            # Add this ordering back into the original DataFrame cadetBranches 
            for column in cadet_preferences['index']: 
                studentJobs.loc[studentJobs['UniqueID'] == Student, column] = cadet_preferences.loc[cadet_preferences['index'] == column, 'V1'].values[0]

        # need the branch columns being slotted to cadets for a couple of downstream coding reasons:
        branchColumns = cadetRow.loc[:, JobConstants.FIRST_MOS_COL:JobConstants.LAST_MOS_COL].columns
        assignments = pd.DataFrame({'Branch': branchColumns})

        print ("fillEmptyStudentsBranches 1")
        print (studentJobs)

#        print ("fillEmptyStudentsBranches 3")
#        print (studentJobs)

        return self.slotStudents (studentJobs, branchNumbers, branchNumberOverfill)

    def slotStudents (self, studentJobs, branchNumbers, branchNumberOverfill):
        sortedStudentBranches = studentJobs.copy ()

        # Apply the lambda function to the 'Vacancies_RCMS' column with the provided scaling factor
        localBranchNumbers = branchNumbers.copy ()
        localBranchNumbers['Vacancies_RCMS'] = localBranchNumbers['Vacancies_RCMS'].apply(lambda x: int(x * branchNumberOverfill))

        # Initialize the branchAssignments DataFrame
        branchAssignments = pd.DataFrame (columns=studentJobs.columns)
        branchAssignments['AssignedJob'] = np.nan

        # Find the column indices corresponding to the range
        startIndex = studentJobs.columns.get_loc (JobConstants.FIRST_MOS_COL)
        endIndex = studentJobs.columns.get_loc (JobConstants.LAST_MOS_COL) + 1
        branchColumns = studentJobs.columns[startIndex:endIndex]

        for index, row in studentJobs.iterrows():
            branchValues = row[branchColumns]
            branchValuesArray = [''] * (endIndex - startIndex + 1)

            # Iterate  through the row and assign the column name to the in an array
            for columnIndex, rowValue in enumerate (branchValues):
                if not pd.isna(rowValue):
                    branchValuesArray[int (rowValue) - 1] = branchColumns[columnIndex]

            # Place the sorted values back into the sortedStudentBranches DataFrame
            for columnIndex, column in enumerate(branchColumns):
                sortedStudentBranches.at[index, column] = branchValuesArray[columnIndex]

        # Change the column headings for all the MOS
        new_columns = {col: i + 1 for i, col in enumerate(branchColumns)}
        sortedStudentBranches.rename(columns=new_columns, inplace=True)

        # Slot cadets
        for index, row in sortedStudentBranches.iterrows():
            branchValues = row[list(new_columns.values())]
            branchValuesArray = [''] * len(branchValues)

            # Iterate through the row and assign the column name in an array based on the rank value
            for col_name, rowValue in branchValues.items():
                if not pd.isna(rowValue):
                    try:
                        rowValueIndex = int(rowValue) - 1
                        branchValuesArray[rowValueIndex] = col_name
                    except (ValueError, TypeError):
                        continue

            # Check against branchNumbers for available slots and assign jobs
            for job in branchValuesArray:
                if job and job in localBranchNumbers['RCMS_VacancyMOS_CD'].values:
                    available_slots = localBranchNumbers.loc[localBranchNumbers['RCMS_VacancyMOS_CD'] == job, 'Vacancies_RCMS'].values[0]

                    # Slot cadet if available slots are greater than zero. Build cadet's row to store results
                    if available_slots > 0:
                        branchAssignments.at[index, 'StudentID'] = row['StudentID']
                        branchAssignments.at[index, 'AssignedJob'] = job
                        localBranchNumbers.loc[localBranchNumbers['RCMS_VacancyMOS_CD'] == job, 'Vacancies_RCMS'] -= 1
                        break  # Once assigned, break out of the loop

        return branchAssignments 
        

        # Get the subset of columns to be sorted
 
#        print (sortedStudentBranches)
        
    def slotStudent (self, studentJobs, branchNumbers, branchNumberOverfill):
        # Apply the lambda function to the 'Vacancies_RCMS' column with the provided scaling factor
        branchNumbers['Vacancies_RCMS'] = branchNumbers['Vacancies_RCMS'].apply(lambda x: int(x * branchNumberOverfill))

        # Loop through the each cadet, to find subsequent rankings according to IMT's dictates

        # Find the column indices corresponding to the range
        startIndex = studentJobs.columns.get_loc (JobConstants.FIRST_MOS_COL)
        endIndex = studentJobs.columns.get_loc (JobConstants.LAST_MOS_COL) + 1

        # Get the subset of columns to be sorted
        branchColumns = studentJobs.columns[startIndex:endIndex]

        def sortRow (row):
            sortedRow = row[branchColumns].sort_values ().values
            row[branchColumns] = sortedRow

            return row
        
        studentJobs = studentJobs.apply (sortRow, axis = 1)
        
        print (studentJobs)
        print (branchNumbers)

        return studentJobs