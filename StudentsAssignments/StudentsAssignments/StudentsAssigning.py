# import pandas lib as pd
import pandas as pd
import numpy as np

from studentsassignments.JobConstants import JobConstants

class StudentsAssigning:

    def fillEmptyAssignments (self, studentJobs, imtPriorities, branchNumbers, noneSelects = None, adNonSelectNumbers = None, branchNumberOverfill = 1):
        # If nonSelects is not None, then append the noneSelects to the studentJobs
        if noneSelects is not None:
            # Concatenate noneSelects to studentJobs
            studentJobs = pd.concat ([studentJobs, noneSelects], ignore_index = True)

        print ('Number of Students: ', len (studentJobs))

        # Arrange the cadet preferences in order of what IMT gives us if they only order some of the branches
        for Student in studentJobs['UniqueID'].unique(): 
            # Get the row that the cadet is on in cadetBranches 
            studentRow = studentJobs[studentJobs['UniqueID'] == Student].copy() 
            
            # Remove everything except their branch preferencing 
            studentRow = studentRow.loc[:, JobConstants.FIRST_JOB_COL:JobConstants.LAST_JOB_COL].dropna(axis=1).transpose().reset_index()

            studentRow.columns = ['index', 'V1'] 
            studentRow = studentRow.sort_values(by='V1').reset_index(drop=True) 
            
            # Remove the branches that have already been ordered and keep only the branches that the cadet has not ordered 
            imtPriorities2 = imtPriorities[~imtPriorities['JobCode'].isin(studentRow['index'])].copy() 
            imtPriorities2['V1'] = range(len(studentRow), len(studentRow) + len(imtPriorities2)) 
            imtPriorities2.rename(columns={'JobCode': 'index'}, inplace=True) 
            
            # Preserve the order of preference for the cadet and then also order the rest of the branches for them that have not been preferenced 
            cadet_preferences = pd.concat([studentRow, imtPriorities2], ignore_index=True).sort_values(by='index').reset_index(drop=True) 
            
            # Add this ordering back into the original DataFrame cadetBranches 
            for column in cadet_preferences['index']: 
                studentJobs.loc[studentJobs['UniqueID'] == Student, column] = cadet_preferences.loc[cadet_preferences['index'] == column, 'V1'].values[0]

        # need the branch columns being slotted to cadets for a couple of downstream coding reasons:
        branchColumns = studentRow.loc[:, JobConstants.FIRST_JOB_COL:JobConstants.LAST_JOB_COL].columns
        branches = pd.DataFrame({'Branch': branchColumns})
        
        return self.slotStudents (studentJobs, branchNumbers, branchNumberOverfill)

    def slotStudents (self, studentJobs, branchNumbers, branchNumberOverfill):
        sortedStudentBranches = studentJobs.copy ()

        # Apply the lambda function to the 'Vacancies_RCMS' column with the provided scaling factor
        localBranchNumbers = branchNumbers.copy ()
        localBranchNumbers['Vacancies_RCMS'] = localBranchNumbers['Vacancies_RCMS'].apply(lambda x: int(x * branchNumberOverfill))

        # Initialize the jobAssignments DataFrame
        jobAssignments = pd.DataFrame (columns=studentJobs.columns)

        # Find the column indices corresponding to the range
        startIndex = studentJobs.columns.get_loc (JobConstants.FIRST_JOB_COL)
        endIndex = studentJobs.columns.get_loc (JobConstants.LAST_JOB_COL) + 1
        branchColumns = studentJobs.columns[startIndex:endIndex]

        for index, row in studentJobs.iterrows():
            branchValues = row[branchColumns]
            branchValuesArray = [''] * (endIndex - startIndex + 1)

            # Iterate through the row and assign the column name to the in an array
            for columnIndex, rowValue in enumerate (branchValues):
                if not pd.isna (rowValue):
                    branchValuesArray[int (rowValue) - 1] = branchColumns[columnIndex]

            # Place the sorted values back into the sortedStudentBranches DataFrame
            for columnIndex, column in enumerate (branchColumns):
                sortedStudentBranches.at[index, column] = branchValuesArray[columnIndex]

        # Change the column headings for all the jobs
        new_columns = {col: i + 1 for i, col in enumerate (branchColumns)}
        sortedStudentBranches.rename (columns=new_columns, inplace=True)

        # Move Unique ID column to the beginning
        sortedStudentBranches = sortedStudentBranches[['UniqueID'] + [col for col in sortedStudentBranches.columns if col != 'UniqueID']]

        jobColumns = sortedStudentBranches.columns[startIndex:endIndex]
        rowNumber = 0

        # Slot cadets
        for index, row in sortedStudentBranches.iterrows():
            branchValues = row[list(new_columns.values())]
            branchValuesArray = [''] * len (branchValues)
            rowValueIndex = 0
            rowNumber += 1

            jobAssigned = 0
            
             # Iterate through the row and assign the column name in an array based on the rank value
            for colName, rowValue in branchValues.items():
                if not pd.isna (rowValue):
                    try:
                        branchValuesArray[rowValueIndex] = rowValue
                        rowValueIndex = rowValueIndex + 1
                    except (ValueError, TypeError) as e:
                        print (f"Error occurred {colName} : {rowValue}")
                        print (f"Error message: {str(e)}")
                        continue

            # Check against branchNumbers for available slots and assign jobs
            for jobIndex, job in enumerate (branchValuesArray):

                if job and job in localBranchNumbers['JobCode'].values:
                    availableSlots = localBranchNumbers.loc[localBranchNumbers['JobCode'] == job, 'Vacancies_RCMS'].values[0]

#                    print ("Extracted number of job: ", availableSlots, " for job code ", job)
                    
                    # Slot cadet if available slots are greater than zero. Build cadet's row to store results
                    if availableSlots > 0:

                        jobAssignments.at[index, 'UniqueID'] = row['UniqueID']
                        jobAssignments.at[index, 'StudentID'] = row['StudentID']

                        jobAssignments.at[index, 'UsarInputOML'] = int (rowNumber)

                        # Append the job columns to jobAssignments
                        for col in jobColumns:
                            jobAssignments.at[index, col] = row[col]

                        jobAssignments.at[index, 'OML'] = row['OML']
                        jobAssignments.at[index, 'JobAssigned'] = job
                        jobAssignments.at[index, 'StudentsPickNum'] = int (jobIndex + 1)
                        jobAssignments.at[index, 'dup'] = int (0)
                        
                        # Determine ranking error where if the student enters a same value more than once in the rankings
                        # Check if any value in branchColumns exists more than once for the row
                        if branchValues.duplicated().any():
                            jobAssignments.at[index, 'RankingError'] = int (1)
                        else:
                            jobAssignments.at[index, 'RankingError'] = int (0)
                    
                        localBranchNumbers.loc[localBranchNumbers['JobCode'] == job, 'Vacancies_RCMS'] -= 1

                        # Replace NaN values with values from studentJobs for columns from FIRST_JOB_COL to LAST_JOB_COL
                        for col in branchColumns:
                            if pd.isna(jobAssignments.at[index, col]):
                                jobAssignments.at[index, col] = studentJobs.at[index, col]

                        jobAssigned = 1

                        break  # Once assigned, break out of the loop
            if jobAssigned == 0:
                print ("Row #:", index, rowNumber, " Identifier: ", row['StudentID'], job)

        print ("jobAssignments")
        print (jobAssignments)

        print ('Number of job Assignments: ', len (jobAssignments), index, rowNumber)


        return jobAssignments 
        

        # Get the subset of columns to be sorted
 
#        print (sortedStudentBranches)
        
    def slotStudent (self, studentJobs, branchNumbers, branchNumberOverfill):
        # Apply the lambda function to the 'Vacancies_RCMS' column with the provided scaling factor
        branchNumbers['Vacancies_RCMS'] = branchNumbers['Vacancies_RCMS'].apply(lambda x: int(x * branchNumberOverfill))

        # Loop through the each cadet, to find subsequent rankings according to IMT's dictates

        # Find the column indices corresponding to the range
        startIndex = studentJobs.columns.get_loc (JobConstants.FIRST_JOB_COL)
        endIndex = studentJobs.columns.get_loc (JobConstants.LAST_JOB_COL) + 1

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