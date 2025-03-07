/**
 * 
 */
package edu.students.assignments.utilities;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import edu.students.assignments.dataobjects.StudentsAssignmentsDataObject;

/**
 * 
 */
public class StudentsAssignmentsUtilities
{

	public List<StudentsAssignmentsDataObject> parseRecord (String csvData)
	{
		List<StudentsAssignmentsDataObject> records = new ArrayList<StudentsAssignmentsDataObject> ();
		String[] rows = csvData.split("\n");;
		int studentIdentifier;
		String[] data;
		StudentsAssignmentsDataObject record;

		// Time stamp entry 
		Date timeStamp = new Date ();
		
		// Remove the header row if it exists
		try
		{
			Integer.parseInt (rows[0].split (",")[0]);
		}
		catch (NumberFormatException nfe)
		{
			// Non numeric row found so assume that it is the header. Remove.
			csvData = csvData.substring(csvData.indexOf('\n') + 1);
		}
		
		rows = csvData.split("\n");
		
		
		for (String row : rows)
		{
			data = row.split(",");
			studentIdentifier = Integer.parseInt(data[0]);
			record = new StudentsAssignmentsDataObject();
			
			record.setRecordIdentifier (String.format ("%d-%d", timeStamp.getTime(), studentIdentifier));
			record.setEntryTimeStamp (timeStamp);
			record.setStudentID(studentIdentifier);
			record.setLastName(data[1]);
			record.set11A(data[2]);
			record.set12A(data[3]);
			record.set25A(data[4]);
			record.set31A(data[5]);
			record.set35A(data[6]);
			record.set36A(data[7]);
			record.set42B(data[8]);
			record.set66H(data[9]);
			record.set70B(data[10]);
			record.set74A(data[11]);
			record.set88A(data[12]);
			record.set91A(data[13]);
			record.set92A(data[14]);
			record.setOml(data[15]);
			record.setUniqueID(data[16]);
			record.setUsarInputOML(data[17]);
			record.set1(data[18]);
			record.set2(data[19]);
			record.set3(data[20]);
			record.set4(data[21]);
			record.set5(data[22]);
			record.set6(data[23]);
			record.set7(data[24]);
			record.set8(data[25]);
			record.set9(data[26]);
			record.set10(data[27]);
			record.set11(data[28]);
			record.set12(data[29]);
			record.setJobAssigned(data[30]);
			record.setStudentsPickNum(data[31]);
			record.setDup(data[32]);
			record.setRankingError(data[33]);
			
			records.add(record);
		}
		
		return records;
	}
}
