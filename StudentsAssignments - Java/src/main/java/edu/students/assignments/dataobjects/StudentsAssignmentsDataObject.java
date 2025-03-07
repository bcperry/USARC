/**
 * 
 */
package edu.students.assignments.dataobjects;

import java.util.Date;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * 
 */
@Entity
@Table(name = "StudentsAssignments") // Explicitly specifying the table name
public class StudentsAssignmentsDataObject
{
	@Id
	@Column(nullable = false)
	private String recordIdentifier;
	
	@Column(nullable = false)
    private Date entryTimeStamp;

    @Column(nullable = false)
	private int studentID;

    @Column(nullable = false)
    private String lastName;
	private String _11A;
	private String _12A;
	private String _25A;
	private String _31A;
	private String _35A;
	private String _36A;
	private String _42B;
	private String _66H;
	private String _70B;
	private String _74A;
	private String _88A;
	private String _91A;
	private String _92A;
	private String oml;
	private String uniqueID;
	private String usarInputOML;
	private String _1;
	private String _2;
	private String _3;
	private String _4;
	private String _5;
	private String _6;
	private String _7;
	private String _8;
	private String _9;
	private String _10;
	private String _11;
	private String _12;
	private String jobAssigned;
	private String studentsPickNum;
	private String dup;
	private String rankingError;

	// Getters and Setters for each field
	public String getRecordIdentifier ()
	{
		return recordIdentifier;
	}
	
	public void setRecordIdentifier (String recordIdentifier)
	{
		this.recordIdentifier = recordIdentifier;
	}
	
	public int getStudentID ()
	{
		return studentID;
	}

	public void setStudentID (int studentID)
	{
		this.studentID = studentID;
	}

	public String getLastName ()
	{
		return lastName;
	}

	public void setLastName (String lastName)
	{
		this.lastName = lastName;
	}

	public String get11A ()
	{
		return _11A;
	}

	public void set11A (String _11A)
	{
		this._11A = _11A;
	}

	public String get12A ()
	{
		return _12A;
	}

	public void set12A (String _12A)
	{
		this._12A = _12A;
	}

	public String get25A ()
	{
		return _25A;
	}

	public void set25A (String _25A)
	{
		this._25A = _25A;
	}

	public String get31A ()
	{
		return _31A;
	}

	public void set31A (String _31A)
	{
		this._31A = _31A;
	}

	public String get35A ()
	{
		return _35A;
	}

	public void set35A (String _35A)
	{
		this._35A = _35A;
	}

	public String get36A ()
	{
		return _36A;
	}

	public void set36A (String _36A)
	{
		this._36A = _36A;
	}

	public String get42B ()
	{
		return _42B;
	}

	public void set42B (String _42B)
	{
		this._42B = _42B;
	}

	public String get66H ()
	{
		return _66H;
	}

	public void set66H (String _66H)
	{
		this._66H = _66H;
	}

	public String get70B ()
	{
		return _70B;
	}

	public void set70B (String _70B)
	{
		this._70B = _70B;
	}

	public String get74A ()
	{
		return _74A;
	}

	public void set74A (String _74A)
	{
		this._74A = _74A;
	}

	public String get88A ()
	{
		return _88A;
	}

	public void set88A (String _88A)
	{
		this._88A = _88A;
	}

	public String get91A ()
	{
		return _91A;
	}

	public void set91A (String _91A)
	{
		this._91A = _91A;
	}

	public String get92A ()
	{
		return _92A;
	}

	public void set92A (String _92A)
	{
		this._92A = _92A;
	}

	public String getOml ()
	{
		return oml;
	}

	public void setOml (String oml)
	{
		this.oml = oml;
	}

	public String getUniqueID ()
	{
		return uniqueID;
	}

	public void setUniqueID (String uniqueID)
	{
		this.uniqueID = uniqueID;
	}

	public String getUsarInputOML ()
	{
		return usarInputOML;
	}

	public void setUsarInputOML (String usarInputOML)
	{
		this.usarInputOML = usarInputOML;
	}

	public String get1 ()
	{
		return _1;
	}

	public void set1 (String _1)
	{
		this._1 = _1;
	}

	public String get2 ()
	{
		return _2;
	}

	public void set2 (String _2)
	{
		this._2 = _2;
	}

	public String get3 ()
	{
		return _3;
	}

	public void set3 (String _3)
	{
		this._3 = _3;
	}

	public String get4 ()
	{
		return _4;
	}

	public void set4 (String _4)
	{
		this._4 = _4;
	}

	public String get5 ()
	{
		return _5;
	}

	public void set5 (String _5)
	{
		this._5 = _5;
	}

	public String get6 ()
	{
		return _6;
	}

	public void set6 (String _6)
	{
		this._6 = _6;
	}

	public String get7 ()
	{
		return _7;
	}

	public void set7 (String _7)
	{
		this._7 = _7;
	}

	public String get8 ()
	{
		return _8;
	}

	public void set8 (String _8)
	{
		this._8 = _8;
	}

	public String get9 ()
	{
		return _9;
	}

	public void set9 (String _9)
	{
		this._9 = _9;
	}

	public String get10 ()
	{
		return _10;
	}

	public void set10 (String _10)
	{
		this._10 = _10;
	}

	public String get11 ()
	{
		return _11;
	}

	public void set11 (String _11)
	{
		this._11 = _11;
	}

	public String get12 ()
	{
		return _12;
	}

	public void set12 (String _12)
	{
		this._12 = _12;
	}

	public String getJobAssigned ()
	{
		return jobAssigned;
	}

	public void setJobAssigned (String jobAssigned)
	{
		this.jobAssigned = jobAssigned;
	}

	public String getStudentsPickNum ()
	{
		return studentsPickNum;
	}

	public void setStudentsPickNum (String studentsPickNum)
	{
		this.studentsPickNum = studentsPickNum;
	}

	public String getDup ()
	{
		return dup;
	}

	public void setDup (String dup)
	{
		this.dup = dup;
	}

	public String getRankingError ()
	{
		return rankingError;
	}

	public void setRankingError (String rankingError)
	{
		this.rankingError = rankingError;
	}

	/**
	 * @return the entryTimeStamp
	 */
	public Date getEntryTimeStamp ()
	{
		return entryTimeStamp;
	}

	/**
	 * @param entryTimeStamp the entryTimeStamp to set
	 */
	public void setEntryTimeStamp (Date entryTimeStamp)
	{
		this.entryTimeStamp = entryTimeStamp;
	}
}
