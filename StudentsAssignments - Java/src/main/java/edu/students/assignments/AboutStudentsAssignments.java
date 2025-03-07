/**
 * 
 */
package edu.students.assignments;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

/**
 * 
 */
@WebServlet("/aboutstudentsjob")
public class AboutStudentsAssignments extends HttpServlet
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 7022980209307072311L;

	@Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException 
	{
		StringBuffer aboutString = new StringBuffer ("Student Assignment calls the Student Assignment library web service written in \n");
		
		aboutString.append ("Python to possible three end points where the first is initialization \"/initializate\"\n");
		aboutString.append ("This supports initialization where the input Excel files are read and made available for processing.\n");
		aboutString.append ("Student branching \"/studentAssignment\" uses read data to identify empry slots students have, organize\n");
		aboutString.append ("positions by students' and IMT's preferences, then slor students according to IMT's need.\n");
		aboutString.append ("Student location \"/studentlocationpreferences\" assigns a student based on the student's zip code within a\n");
		aboutString.append ("50 mile radius.");
		
        resp.getOutputStream().println(aboutString.toString ());
    }

}
