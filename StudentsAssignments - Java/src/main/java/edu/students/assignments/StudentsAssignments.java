/**
 * 
 */
package edu.students.assignments;

import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.client.Client;
import jakarta.ws.rs.client.ClientBuilder;
import jakarta.ws.rs.client.WebTarget;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

/**
 * 
 */
public class StudentsAssignments
{
	@GET
	@Path ("/numberofavailablejobs")
	@Produces (MediaType.TEXT_PLAIN)
	public String returnNumberOfAvailableJobs ()
	{
		Client client = ClientBuilder.newClient();
		WebTarget target = client.target("http://localhost:5000/numberofavailablejobs");
		Response response = target.request(MediaType.APPLICATION_JSON).get();

		if (response.getStatus() == HttpServletResponse.SC_OK)
		{
			String result = response.readEntity(String.class);
			response.close();
			
			return result;
		}
		else
		{
			response.close();
			return "{\"error\":\"Failed to fetch data from external service\"}";
		}
	}
	
	@GET
	@Path ("/studentsassignments")
	@Produces (MediaType.TEXT_PLAIN)
	public String assignStudentsToJobs ()
	{
		Client client = ClientBuilder.newClient();
		WebTarget target = client.target("http://localhost:5000/studentsassignments");
		Response response = target.request(MediaType.APPLICATION_JSON).get();

		if (response.getStatus() == 200)
		{
			String result = response.readEntity(String.class);
			response.close();
			return result;
		}
		else
		{
			response.close();
			return "{\"error\":\"Failed to fetch data from external service\"}";
		}
	}
	
	@GET
	@Path ("/about")
	@Produces (MediaType.TEXT_PLAIN)
	public String about ()
	{
		StringBuffer aboutString = new StringBuffer ("Student Assignment calls the Student Assignment library web service written in \n");
		
		aboutString.append ("Python to possible three end points where the first is initialization \"/initializate\"\n");
		aboutString.append ("This supports initialization where the input Excel files are read and made available for processing.\n");
		aboutString.append ("Student branching \"/studentAssignment\" uses read data to identify empry slots students have, organize\n");
		aboutString.append ("positions by students' and IMT's preferences, then slor students according to IMT's need.\n.");
		aboutString.append ("Student location \"/studentlocationpreferences\" assigns a student based on the student's zip code within a\n");
		aboutString.append ("50 mile radious.");
		
		return aboutString.toString ();
	}
}
