/**
 * 
 */
package edu.students.assignments.dataobjects;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 */
public class StudentAssignmentDataObj 
{
	private String uniqueIdentifier;
	private int studentIdentifier;
	private String lastName;
	private List<JobRanking> jobRanking = new ArrayList<JobRanking> ();
	private float oml;
	private int usarInput;
	private List<JobRanking> sortedJobRanking = new ArrayList<JobRanking> ();
	private String branchAssigned;
	private int cadetsPickNumber;
	private int duplicate;
	private int rankingError;
	
	/**
	 * @return the uniqueIdentifier
	 */
	public String getUniqueIdentifier ()
	{
		return uniqueIdentifier;
	}
	
	/**
	 * @param uniqueIdentifier the uniqueIdentifier to set
	 */
	public void setUniqueIdentifier (String uniqueIdentifier)
	{
		this.uniqueIdentifier = uniqueIdentifier;
	}
	
	/**
	 * @return the studentIdentifier
	 */
	public int getStudentIdentifier ()
	{
		return studentIdentifier;
	}
	
	/**
	 * @param studentIdentifier the studentIdentifier to set
	 */
	public void setStudentIdentifier (int studentIdentifier)
	{
		this.studentIdentifier = studentIdentifier;
	}
	
	/**
	 * @return the lastName
	 */
	public String getLastName ()
	{
		return lastName;
	}
	
	/**
	 * @param lastName the lastName to set
	 */
	public void setLastName (String lastName)
	{
		this.lastName = lastName;
	}
	
	/**
	 * @return the jobRanking
	 */
	public List<JobRanking> getJobRanking ()
	{
		return jobRanking;
	}
	
	/**
	 * @param jobRanking the jobRanking to set
	 */
	public void setJobRanking (List<JobRanking> jobRanking)
	{
		this.jobRanking = jobRanking;
	}
	
	/**
	 * @return the oml
	 */
	public float getOml ()
	{
		return oml;
	}
	
	/**
	 * @param oml the oml to set
	 */
	public void setOml (float oml)
	{
		this.oml = oml;
	}
	
	/**
	 * @return the usarInput
	 */
	public int getUsarInput ()
	{
		return usarInput;
	}
	
	/**
	 * @param usarInput the usarInput to set
	 */
	public void setUsarInput (int usarInput)
	{
		this.usarInput = usarInput;
	}
	
	/**
	 * @return the sortedJobRanking
	 */
	public List<JobRanking> getSortedJobRanking ()
	{
		return sortedJobRanking;
	}
	
	/**
	 * @param sortedJobRanking the sortedJobRanking to set
	 */
	public void setSortedJobRanking (List<JobRanking> sortedJobRanking)
	{
		this.sortedJobRanking = sortedJobRanking;
	}
	
	/**
	 * @return the branchAssigned
	 */
	public String getBranchAssigned ()
	{
		return branchAssigned;
	}
	
	/**
	 * @param branchAssigned the branchAssigned to set
	 */
	public void setBranchAssigned (String branchAssigned)
	{
		this.branchAssigned = branchAssigned;
	}
	
	/**
	 * @return the cadetsPickNumber
	 */
	public int getCadetsPickNumber ()
	{
		return cadetsPickNumber;
	}
	
	/**
	 * @param cadetsPickNumber the cadetsPickNumber to set
	 */
	public void setCadetsPickNumber (int cadetsPickNumber)
	{
		this.cadetsPickNumber = cadetsPickNumber;
	}
	
	/**
	 * @return the duplicate
	 */
	public int getDuplicate ()
	{
		return duplicate;
	}
	
	/**
	 * @param duplicate the duplicate to set
	 */
	public void setDuplicate (int duplicate)
	{
		this.duplicate = duplicate;
	}
	
	/**
	 * @return the rankingError
	 */
	public int getRankingError ()
	{
		return rankingError;
	}
	
	/**
	 * @param rankingError the rankingError to set
	 */
	public void setRankingError (int rankingError)
	{
		this.rankingError = rankingError;
	}
}
