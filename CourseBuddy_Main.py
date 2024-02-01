import Library_CompareClasses as scheduler
import getScheduleOfClassesRutgers as SOC
from Class_Student import student
import os.path
import time

def studentInfo():
    print("Hello, welcome to Degree Buddy.")
    localTime = time.asctime(time.localtime(time.time()))
    print(localTime)
    studentID = input("Please enter your student ID:")
    studentIDFileName = studentID + '.txt'

    if(os.path.exists(studentIDFileName) == True):
        studentIDFile = open(studentIDFileName,"r")
        studentData = studentIDFile.read()
        
        studentData = studentData.split('\n')
        myStudent = student()

        studentDataID = studentData[0].split(",")[1]
        studentDataFirstName = studentData[1].split(",")[1]
        studentDataLastName = studentData[2].split(",")[1]
        studentDataClassAmount = studentData[3].split(",")[1]
        studentDataStartTime = studentData[4].split(",")[1]
        studentDataEndTime = studentData[5].split(",")[1]

        myStudent.setStudentID(studentDataID)
        myStudent.setFirstName(studentDataFirstName)
        myStudent.setLastName(studentDataLastName)
        myStudent.setClassAmount(studentDataClassAmount)
        myStudent.setStartTime(studentDataStartTime)
        myStudent.setEndTime(studentDataEndTime)
 
        for i in studentData[6:-1]:
            myStudent.setCourses(i.split(",")[1])

        print("\nWelcome Back ", myStudent.getFirstName())
        print("Here's what we have in your profile...\n")
        print("Courses per semester :",myStudent.getClassAmount())
        print("Your classes will start no earlier than ",myStudent.getStartTime(), " and end before " , myStudent.getEndTime())
 
    else:

        myStudent = student()
        courseTimes = []

        for i in range(7,23):
            AMPM = "A"
            normalTime = i
 
            if (i > 11):
                AMPM = "P"
                if(i > 12):
                    normalTime = normalTime - 12
                
            mytime =  str(normalTime) + ":00" + AMPM
            courseTimes.append([i - 6,mytime])
                
        print("\n")
        studentIDFile = open(studentIDFileName,"w")
        studentIDFile.write("StudentID," + studentID + "\n")
        
        print("Welcome, we see you've never been here before! We need to create a brief profile about yourself...\n")
        print("Please enter the following information...")
        studentFirstName = input("Please enter your first name:")
        studentIDFile.write("firstName," + studentFirstName + "\n")
        myStudent.setFirstName(studentFirstName)
        
        
        studentLastName = input("Please enter your last name:")
        studentIDFile.write("lastName," + studentLastName + "\n")
        myStudent.setLastName(studentLastName)

        print("\n")
        print("Thanks ",studentFirstName,",")
        print("Now lets get some of your preferences...")
        studentClassAmount = input("How many classes are you looking to take each semester?:")
        studentIDFile.write("classCount," + studentClassAmount + "\n")
        myStudent.setClassAmount(studentClassAmount)
        print("\n")

        for i in courseTimes:
            print (i[0],":",i[1])

        studentStartTime = input("Whats the earliest you would like to start class? \nEnter a number from the list above:")
        
        for i in courseTimes:
            if(str(i[0]) == studentStartTime):
            
               print(i[1])
               studentStartTime = i[1]
               studentIDFile.write("startTime," + studentStartTime + "\n")
               myStudent.setStartTime(studentStartTime)
               
        print("\n")

        studentEndTime = input("Whats the latest you would like to leave class? \nEnter a number from the list above:")

       
        for i in courseTimes:
            if(str(i[0]) == studentEndTime):
            
               print(i[1])
               studentEndTime = i[1]
               studentIDFile.write("startTime," + studentEndTime + "\n")
               myStudent.setEndTime(studentEndTime)
        print("\n")

        print("Great, now we need to you to enter the course numbers for the classes you've already taken.")
        count = 1;
        continueCourses = True

        takenClasses = "" 
        while(takenClasses != "N" and takenClasses != "Y"):
            takenClasses = input("Have you taken any courses towards your degree yet?(Y/N):").upper()
            if(takenClasses == "N" or takenClasses == "NO"):
                continueCourses = False
                takenClasses = "N"
                print("Thanks! Welcome to Rutgers, as you continue to take courses, your profile and degree navigator will be updated.")
            elif(takenClasses == "Y" or takenClasses == "YES"):
                takenClasses = "Y"
                print("\n Great! Please enter the course numbers for the ones you've taken already.")
            else:print("Invalid response, please enter yes or no (Y/N)")
    
        while(continueCourses):
            courseCounter = 'Course ' + str(count) + ":"
            courseNumber = input(courseCounter)
            studentIDFile.write('course' + str(count) + "," + courseNumber + "\n")
            myStudent.setCourses(courseNumber)
            count = count + 1
            
            addMore = input("add another course?(y/n):").upper()
            
            if(addMore == "N" or addMore == "NO"):
                continueCourses = False
                print("Thanks for adding your courses!")
                print("As you continue to take courses, your profile and degree navigator will be updated.")
                print("Course List: \n")
                print(myStudent.getCourses())
                                
        
                        ## close the file
    studentIDFile.close()
    return studentID#myStudent.id

ruID = studentInfo() # Calls routine to get stored info

def extractStoredPreferences(myID):
    transcript = []
    numClasses = 0
    studentIDFile = open((str(myID)+".txt"),"r")
    studentData = studentIDFile.read()
    data = studentData.split('\n')
    startTime = data[4].split(",")[1]
    endTime = data[5].split(",")[1]
    
    numClasses = data[3].split(",")[1]
    for i in data[6:-1]:
        transcript.append(i.split(",")[1])

    return transcript, numClasses, startTime, endTime


majorList = ["Engineering_Management",
"User_Experience",
"Analytics",
"Applied_Computing",
"Personal_Care_Science",
"Kinesiology_and_Applied_Physiology",
"Global_Agriculture",
"Sustainability",
"Horticulture_and_Turfgrass_Science",
"Food_Science",
"Drug_Discovery_and_Development",
"Chemistry",
"Biomedical_Engineering",
"Pharmaceutical_Engineering",
"Quality_and_Reliability_Engineering" ]

print("\nMBS Majors List: \n")
idx = 0
for m in majorList:
    idx += 1
    print(idx,". ",m)
        
majorName = majorList[int(input("\nWhich Major do you want to match your transcipt to:"))-1]
print("OK Building schedule for ", majorName)
#majorName = "Engineering_Management"

semester = "12016" #Next Spring 2016
checkDepartmentNames = ["Business_Curriculum"]
checkDepartmentNames.append(majorName)
releventDepartments = scheduler.getRelevantDepts(checkDepartmentNames)#ask user
#['137', '540', '799', '180', '125', '127', '155', '198', '332', '635', '731', '620', '711', '533', '832']

masterClassList = SOC.buildMasterClassList(semester = semester, subjList = releventDepartments)
#print(masterClassList)
#for c1 in masterClassList:
    #print("\n")
    #for c2 in c1:
        #print(c2)
        
transcript, targetNumClasses, startString, endString = extractStoredPreferences(ruID)
print("\n$$$$$$$$$$$$$$$$$$$$$")
print("Transcript: ",transcript)

sched = (scheduler.createSchedule(majorName, transcript, int(targetNumClasses), masterClassList, startString[:-1].replace(":", ""), startString[-1], endString[:-1].replace(":", ""), endString[-1]))
scheduler.printFinalSchedule(sched)

