/**
 * 
 */
package edu.students.assignments;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import edu.students.assignments.dataoperations.DataOperations;
import edu.students.assignments.utilities.StudentsAssignmentsUtilities;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

/**
 * 
 */
@WebServlet ("/processandsave")
public class StudentAssignments extends HttpServlet
{
	/**
	 * 
	 */
	private static final long serialVersionUID = -6555670927749416729L;

	/**
	 * 
	 */

	@Override
	protected void doGet (HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		StudentsAssignmentsUtilities assignmentUtilities = new StudentsAssignmentsUtilities ();
		DataOperations databaseOperations = new DataOperations ();
		String responseData;
		
		// Create HttpClient
		HttpClient client = HttpClient.newHttpClient();

		// Create a GET request
		HttpRequest httpRequest = HttpRequest.newBuilder().uri(URI.create("http://localhost:5000/studentsassignments")).build();

		try
		{
			// Send the request and get the response
			HttpResponse<String> httpResponse = client.send(httpRequest, HttpResponse.BodyHandlers.ofString());

			// Check if the request was successful
			if (httpResponse.statusCode() == HttpServletResponse.SC_OK)
			{
				// Process the response data as needed
				responseData = httpResponse.body();

				try
				{
					// Save the records to the database after parsing all records
					// Prepare the database operations for execution
//					databaseOperations.saveStudentsAssignments (assignmentUtilities.parseRecord(responseData));
				}
				catch (Exception e)
				{
					responseData = e.getStackTrace() + "\n" + responseData;
				}
				
				response.getOutputStream().println(responseData);
				// response.getOutputStream().println("Response from server: " + responseData);
			}
			else
			{
				response.getOutputStream().println("Failed to retrieve data. Status code: " + httpResponse.statusCode());
			}

		}
		catch (InterruptedException | IOException e)
		{
			throw new ServletException("Error making the HTTP request", e);
		}

		// response.getOutputStream().println("Hello World");
	}
}
