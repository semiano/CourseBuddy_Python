**PDF**
[Rutgers - Degree Buddy Demo.pdf](https://github.com/semiano/CourseBuddy_Python/files/14119121/Rutgers.-.Degree.Buddy.Demo.pdf)

**Degree Buddy**
**Detailed Design Specifications**
	The main goal of the application is to be a Degree Navigator for students in the MBS program.  The application will determine which classes the user still needs to take in order to finish his/her degree and make a recommended schedule for next semester.  
This will require taking input from the user about their current transcript as well as their personal preferences.  The student’s transcript will be in the form of a PDF, which can be downloaded from the Rutgers website.  This PDF will have to be converted to text and parsed.  To do this we will employ a custom library “ParseTranscript” which utilizes a 3rd party library “PDFMiner”.  The student’s preferences, which will include desired class topics in the form of keywords, as well as # classes they want to take can be entered from the application and stored locally in a text file.  A database would be a good choice here, but for the scope of this project, we will store each student’s preferences in a text file (CSV format).
Next we will need to know the degree requirements for each program in the MBS department.  This will have to be compiled manually from the program website.  This will not only capture course lists, but information such as “take 3 of the following 5 courses”.  This data will be static and stored in one or more text files in CSV format.  Again, a database would be another excellent choice for this data. 
![image](https://github.com/semiano/CourseBuddy_Python/assets/6520366/1c5c2619-e6fb-4ead-be1c-89e2ae2f8690)

The application will also need to know the schedule of classes for next semester.  Luckily, Rutgers provides a web API for grabbing such information.  For this, we will employ a custom library “GetSheduleOfClasses” that will take have functions that take parameters from regarding year, campus, and course level, a function that builds the URL string, a function that calls the API, and a function that parses the returned JSON.  This custom library will require 3rd party libraries “Requests” and “JSON”.

Finally, we will need a custom library which takes all of the input data and can determine the degree progress and build a schedule recommendation.   It will need two functions, the first will match each degree requirement with a course already taken to determine the degree requirements remaining.  The other function will match the remaining degree requirements with the schedule of classes for next semester, filtered by the student’s preferences.
The Object Oriented approach will have a Class “Student”, with properties “name”, “preferenceFileName”, “degreeEnroled”, “recommendedSchedule”.  The Student Class will have functions “changePreferences”, “loadTranscript”, and “calulateSchedule”.

![image](https://github.com/semiano/CourseBuddy_Python/assets/6520366/54314b02-7845-4d55-a337-fce67d31f102)
![image](https://github.com/semiano/CourseBuddy_Python/assets/6520366/14f34155-0d44-40df-91bc-97e6fe08a01d)
![image](https://github.com/semiano/CourseBuddy_Python/assets/6520366/69101c78-c344-4a41-99e4-bb85973e37c9)
![image](https://github.com/semiano/CourseBuddy_Python/assets/6520366/8c97b655-9af3-47fb-aa54-474cc7119b16)
![image](https://github.com/semiano/CourseBuddy_Python/assets/6520366/d24c366e-d3b4-49eb-be27-ed1d65a39276)
