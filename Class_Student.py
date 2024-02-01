class student:

    def __init__(self):
        self.myCourses = []

    def setStudentID(self,studentID):
        self.id = studentID

    def getStudentID(self):
        return self.id
    
    def setFirstName(self, name):
        self.firstName = name

    def getFirstName(self):
        return self.firstName

    def setLastName(self, name):
        self.lastName = name

    def getLastName(self):
        return self.lastName

    def setClassAmount(self, number):
        self.classAmount = number

    def getClassAmount(self):
        return self.classAmount

    def setStartTime(self, number):
        self.startTime = number

    def getStartTime(self):
        return self.startTime

    def setEndTime(self, number):
        self.endTime = number

    def getEndTime(self):
        return self.endTime

    def setCourses(self,course):
        self.myCourses.append(course)

    def getCourses(self):
        return self.myCourses
