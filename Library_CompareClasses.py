#Requirements are a Python List containting of Dictionaries.
#There is a dictionary per degree requirement.
#Dictionary "key" is a Tuple of possible courses. (Dictionary keys cannot be Lists (mutable))
#Dictionary "value" is the number of courses req from that list.

#'*' indicates the class code can be anything.(16:137:* means any class from MBS dept.)

Business_Curriculum =[
{("16:137:530") : 1},
{("16:137:507", "16:137:650") : 1} ,
{("16:137:502") : 1} ,
{("16:137:501", "16:137:575", "16:137:650", "22:799:661", "22:620:691", "22:711:562", "22:799:607", "22:799:672", "38:533:540", "38:533:580", "34:832:515") :2 } ,
{("16:137:500") :1 } ,
{("16:137:600") :1 }
]

Engineering_Management =[
{("16:137:560", 
"16:540:580",
"16:540:585",
"22:799:692",
"22:799:691",
"16:180:545",
"16:180:546",
"16:540:520",
"16:540:560",
"16:540:575",
"16:540:594",
"16:540:595") : 3},

{(
  "16:125:*",
  "16:127:*",
  "16:155:*",
  "16:180:*",
  "16:198:*",
  "16:332:*",
  "16:540:*",
  "16:635:*",
  "16:731:*") : 5}
]

User_Experience = [
{("16:137:531") : 1},
{("16:137:532") : 1},
{("16:137:535") : 1},
{("16:137:533") : 1},
{("16:137:603", "16:137:536") : 1},

{("16:137:601",
"01:355:425",
"16:137:513",
"16:137:650",
"16:137:650",
"17:610:510",
"17:610:511",
"17:610:512",
"17:610:554",
"17:610:557",
"22:198:603",
"17:610:581",
"17:610:587",
"16:830:506",
"16:830:508",
"16:830:514",
"16:830:522",
"16:830:546",
"17:194:511",
"17:194:514",
"34:970:515:01",
"34:833:635",
"56:198:500") : 3}
]



Analytics =[

{("16:137:550") : 1},
{("16:137:601") : 1},
{("16:960:563") : 1},
{("17:610:557") : 1},
{("16:137:602") : 1},

{("16:137:550",
"16:137:560",
"16:137:601",
"16:137:602",
"16:960:588",
"16:960:563",
"26:198:644",
"17:610:561",
"16:220:507",
"16:332:569",
"16:198:541",
"16:332:503",
"16:332:566",
"16:332:572",
"16:332:573",
"17:610:557",
"56:137:500",
"16:137:602",
"26:198:641",
"56:198:500",
"16:137:531",
"17:610:554",
"17:610:560",
"17:610:558") : 3}

]


Applied_Computing =[
{("56:198:510") : 1},
{("56:198:551", "56:198:552") : 1},
{("56:198:575", "56:198:548") : 1},
{("56:198:546", "56:198:549") : 1},
{("56:198:510",
"56:198:551",
"56:198:552",
"56:198:575",
"56:198:548",
"56:198:546",
"56:198:549",
"56:198:523",
"56:198:559",
"56:198:556",
"16:332:*") : 3}

]


Personal_Care_Science =[
{("16:137:570") : 1},
{("16:137:571") : 1},

{("16:400:612",
"16:400:515",
"16:682:501",
"16:137:510",
"16:720:523",
"16:160:509",
"16:137:582") : 3},


{("11:776:312",
"11:776:495",
"11:776:496",
"16:137:511",
"16:137:580",
"16:137:581",
"16:155:501",
"16:155:506",
"16:155:511",
"16:155:514",
"16:155:532",
"16:155:544",
"16:155:545",
"16:155:546",
"16:155:547",
"16:155:548",
"16:155:549",
"16:155:550",
"16:160:503",
"16:160:509",
"16:160:512",
"16:160:531",
"16:400:521",
"16:400:605",
"16:400:606",
"16:400:610",
"16:400:611",
"16:400:613",
"16:540:560",
"16:540:572",
"16:540:580",
"16:663:502",
"16:663:505",
"16:720:507",
"16:720:509",
"16:720:550",
"30:715:453") : 3}

]


Kinesiology_and_Applied_Physiology =[
{("16:572:501") : 1},
{("16:572:503") : 1},
{("16:572:506") : 1},
{("16:572:502") : 1},
{("16:572:520") : 1},

{("01:377:406",
"01:377:412",
"16:572:510",
"16:572:510",
"16:572:509",
"16:572:507",
"16:572:505",
"16:572:508",
"16:761:507",
"16:761:508",
"16:761:513") : 3}

]

Global_Agriculture =[
{("16:137:576",
"16:395:502",
"11:015:440",
"16:765:531",
"16:375:534",
"01:960:XXX") : 5},

{("16:215:650",
"16:400:513",
"16:400:514",
"16:765::501",
"16:765:520",
"16:765:528",
"16:765:533",
"16:765:536",
"11:776:443") : 3}

]

Sustainability =[
{("16:137:556",
"34:970:620",
"16:137:603") : 2},

{("16:375:523",
"11:704:451",
"26:120:507",
"26:375:590",
"26:375:534") : 1},

{("34:970:571",
"22:799:672",
"16:375:534",
"26:120:522") : 1},

{("16:137:555") : 1},

{("11:680:491",
"11:704:466",
"16:180:561",
"16:180:562",
"16:180:563",
"16:180:564"
"16:180:566",
"16:180:567",
"16:180:568",
"16:180:574",
"16:180:588",
"16:180:590",
"16:215:650",
"16:375:504",
"16:375:510",
"16:375:524",
"16:375:527",
"16:375:531",
"16:450:501",
"16:450:510",
"16:450:511",
"16:450:523",
"11:117:492",
"14:155:453",
"16:155:512",
"16:155:514",
"16:155:518"
"16:155:531",
"16:155:533",
"16:155:543",
"01:160:425",
"16:160:521",
"16:160:525",
"16:160:575",
"16:160:503",
"16:400:515",
"16:400:613",
"16:635:529",
"16:720:523",
"16:160:512",
"16:160:571",
"16:160:504",
"16:400:521",
"16:160:543",
"16:160:544",
"16:160:579",
"14:180:429",
"16:180:564",
"16:180:565",
"16:180:568",
"16:375:510",
"16:375:517",
"16:375:522",
"16:375:522",
"16:375:523",
"16:375:534",
"16:375:563",
"01:680:491",
"11:704:466",
"01:750:451",
"16:332:581",
"16:332:583",
"16:332:594",
"16:335:501",
"16:335:502",
"14:635:413",
"16:635:511",
"16:635:604",
"16:160:541",
"16:635:527",
"16:635:566",
"14:650:461",
"14:650:462",
"14:650:474",
"16:650:570",
"16:650:574",
"16:650:578",
"16:650:670",
"16:650:674",
"16:750:611",
"16:750:612",
"16:765:602",
"34:970:672",
"16:395:509",
"16:450:502",
"16:450:503",
"16:450:511",
"16:450:526",
"17:194:501",
"17:194:501",
"22:373:609",
"34:833:632",
"34:833:572",
"34:970:523",
"34:970:618",
"34:970:619",
"34:970:622",
"34:970:670",
"34:970:672",
"26:120:507",
"26:120:523",
"26:120:590",
"26:120:534",
"26:120:551",
"26:120:580",
"26:120:593",
"26:375:560",
"26:375:602",
"26:380:521",
"26:380:561",
"26:380:576",
"26:380:608") : 4}

]

Horticulture_and_Turfgrass_Science =[
{("11:776:450",
"11:776:451",
"16:765:502",
"16:765:522",
"16:765:536",
"16:765:699") : 3},

{("16:137:604") : 1},

{("11:015:423",
"11:015:439",
"11:704:403",
"11:776:475",
"11:776:402",
"11:776:405",
"11:776:439",
"16:765:533",
"11:776:402",
"11:776:404",
"11:776:405",
"11:776:408",
"11:015:432",
"11:776:325",
"11:776:425",
"19:910:507",
"19:910:560",
"19:910:562",
"19:910:572") : 4}

]

Food_Science =[
{("16:400:513",
"16:400:514",
"16:400:507") : 2},

{("11:400:410",
"11:400:412",
"16:400:501",
"16:400:502",
"16:400:504",
"16:400:505",
"16:400:506",
"16:400:511",
"16:400:512",
"16:400:519",
"16:400:521",
"16:400:526",
"16:400:530",
"16:400:605",
"16:400:606",
"16:400:609",
"16:400:612",
"16:400:613") : 6}

]

Drug_Discovery_and_Development =[
{("16:137:510",
"16:137:511",
"16:137:580",
"16:137:582",
"16:137:581",
"16:115:511",
"16:115:512",
"16:148:514") : 5},

{("16:137:501") : 1},

{("16:137:582",
"16:137:613",
"16:115:511",
"16:125:509",
"16:148:652",
"16:718:680",
"16:148:504",
"16:681:502",
"16:710:555",
"16:137:615",
"16:137:584",
"16:340:616",
"16:155:545",
"16:155:514",
"16:137:585",
"16:137:602",
"16:960:590",
"16:137:615",
"16:137:616",
"56:198:500") : 4}

]

Chemistry =[
{("16:160:511",
"16:160:512",
"16:160:515",
"16:160:571",
"16:160:504",
"16:160:503",
"16:160:525",
"16:160:542",
"16:160:537",
"16:160:544") : 4},

{("16:160:607",
"16:160:608") : 1}

]

Biomedical_Engineering =[
{("16:125:571",
"16:125:572",
"16:125:573",
"16:125:574") : 1},

{("16:125:501") : 1},

{("16:125:586") : 1},

{("11:126:484",
"16:125:506",
"16:125:509",
"16:125:546",
"16:125:564",
"16:125:572",
"16:125:573",
"16:125:574",
"16:125:575",
"16:125:584",
"16:125:589",
"16:125:601",
"16:125:602",
"16:125:618",
"16:125:624",
"16:125:628",
"16:148:519",
"16:148:530",
"16:148:550",
"16:150:501",
"16:155:501",
"16:155:502",
"16:155:514",
"16:155:531",
"16:155:541",
"16:155:551",
"16:155:552",
"16:155:588",
"16:160:537",
"16:198:503",
"16:198:510",
"16:198:535",
"16:198:580",
"16:332:521",
"16:332:583",
"16:332:584",
"16:332:591",
"16:642:573",
"16:642:574",
"16:650:512"
"16:650:518",
"16:650:606",
"16:681:502",
"16:681:530",
"16:681:543",
"16:681:555",
"16:681:585",
"16:960:584",
"16:960:585") : 5}

]

Pharmaceutical_Engineering =[
{("16:155:545",
"16:155:546") : 2},

{("16:155:541",
"16:155:547",
"16:155:549") : 2},

{("16:137:501",
"16:137:510",
"16:137:511",
"16:137:580",
"16:137:581",
"16:155:501",
"16:155:502",
"16:155:506",
"16:155:507",
"16:155:511",
"16:155:514",
"16:155:532",
"16:155:544",
"16:155:548",
"16:155:150",
"16:155:586",
"16:155:587",
"16:540:530",
"16:540:555",
"16:540:560",
"16:540:572",
"16:540:580",
"16:540:585",
"16:540:586",
"16:540:595",
"16:540:685",
"16:650:554",
"16:663:502",
"16:663:505",
"16:190:540",
"16:190:542",
"16:190:580",
"16:190:590",
"16:720:507",
"16:720:509",
"16:720:550") : 4}

]

Quality_and_Reliability_Engineering =[
{("16:540:560",
"16:540:580",
"16:540:585",
"16:540:685",
"16:960:540",
"16:960:542",
"16:960:590") : 7},

{("16:540:530",
"16:540:555",
"16:540:572",
"16:540:586",
"16:540:595",
"16:960:580",
"26:960:580") : 1}

]



#students_transcript = []






def getRelevantDepts(majors = []): #returns a list of unique department codes for a given Majors list
    deptCodes = []
    for m in majors:
        #print(m)
        deptReq = []
        majorReqs = eval(m)
        for c1 in majorReqs:
            #print(c1)
            for c2 in c1:
                #print(c2)
                if type(c2) == type("string"):
                    deptCode = c2.split(":")[1]
                    #print(deptCode)
                    if deptCode not in deptCodes:
                        deptCodes.append(deptCode)
                else:
                    for c3 in c2:
                        #print(c3)
                        deptCode = c3.split(":")[1]
                        #print(deptCode)
                        if deptCode not in deptCodes:
                            deptCodes.append(deptCode)
                
    #print("\n", deptCodes)
    return deptCodes


def tuple_without(original_tuple, element_to_remove): #allows for adding/deleting to a tuple (unmutable)
    new_tuple = []
    #print("original Tuple:", original_tuple)
    #print("element: ",element_to_remove)
    for s in list(original_tuple):
        if not s == element_to_remove:
            new_tuple.append(s)
    #print("new Tuple:", new_tuple)
    return tuple(new_tuple)


def classIsAMatch(requirementName, className): #compares a requirement to a class code and sees if it satisfies (* means any)
    req = requirementName.split(":")
    cls = className.split(":")
    
    for i in range(len(req)): 
        if str(req[i]) == "*":
            return True
        if str(req[i]) != str(cls[i]):
                return False
    return True


def parseClassCode(classListing): #takes a list of course code elemtns and combines them into a string like "XX:YYY:ZZZ"
    classCode =  ":".join([classListing[0],classListing[1],classListing[2]])
    #print(classCode)
    return classCode


def checkTimeOverlap(classListing, setClasses = []): #returns True if classListing conflicts with any class time in setClasses
    classDay = classListing[5]
    classStart = int(classListing[6])
    classEnd = int(classListing[7])
    classPMCode = classListing[8]
    if classPMCode == "P":
        classStart += 1200
        classEnd += 1200
    
    for c in setClasses:
        day = c[5]
        start = int(c[6])
        end = int(c[7])
        PMCode = classListing[8]
        if PMCode == "P":
            start += 1200
            end += 1200
        if (classDay == day):
            if (classStart > start and classStart < end) or (classEnd > start and classEnd < end):
                return True
            else:
                return False
        else:
            return False









      
#print(str( classIsAMatch("16:540:32","16:540:21") ))

def satisfyRequirement(requirements, numNeeded, students_transcript):
    possibleClasses = dict()
    requirementsUsed = []
    for r in requirements:
        if type(r) == type("string"):
            r = (r,)#string to tuple
        #print("Num Needed: ",numNeeded, "\n","Original Requirements: ",r)
        
        for c in r:
            classesUsed = []
            #print("C: ",c)
            #print("transcript: ",students_transcript)
            for s in students_transcript:
                if numNeeded <=0:
                    break
                else:
                    if classIsAMatch(str(c), str(s)):
                        #print("FOUND ",s)
                        classesUsed.append(s)
                        requirementsUsed.append(c)
                        numNeeded -= 1
            for i in classesUsed:
                #print("removing from Transcript: ", i)
                students_transcript.remove(i)
        
    modifiedRequirement = tuple(requirements)[0]
    if type(modifiedRequirement) == type("string"): modifiedRequirement = (modifiedRequirement,)
    #print("modified Req",modifiedRequirement)
    for i in requirementsUsed:
        #print("i: ",i)
        modifiedRequirement = tuple_without(modifiedRequirement, i)
    #print("Modified Requirements: ",modifiedRequirement, " - ", numNeeded)
    #print("Transcript Unassigned: ", students_transcript)
    possibleClasses.update({modifiedRequirement: numNeeded})
    #print( possibleClasses)
    return possibleClasses, students_transcript
    #return modifiedRequirement, numNeeded


#print("Transcript Original: ", students_transcript)
def satisfyRequirementBlock(reqs = [], transcript = []):
    print("\nDegree Requirements:\n")
    for r in reqs:
        print(eval(r),"\n")
        
    classChoices = []
    for r1 in reqs:
        r2 = eval(r1)
        
        for i in r2:
             for j in dict(i):
                numNeeded = i.get(j)
                c, t = satisfyRequirement(i, i.get(j), transcript)
                classChoices.append(c)
                transcript = t
                #print("\n")
    

    return classChoices, transcript



#c = satisfyRequirementBlock(["Engineering_Management", "Business_Curriculum"], ["16:137:500", "16:180:545", "16:137:600", "22:222:222"])
#print(c)


#Business_Curriculum =[
#{("16:137:530") : 1},
#{("16:137:507", "16:137:650") : 1} ,
#{("16:137:502") : 1} ,
#{("16:137:501", "16:137:575", "16:137:650", "22:799:661", "22:620:691", "22:711:562", "22:799:607", "22:799:672", "38:533:540", "38:533:580", "34:832:515") :2 } ,
#{("16:137:500") :1 } ,
#{("16:137:600") :1 }
#]




def convertTimeTo24(timeString, PMCode):
    time24Hour = str(int(timeString) + 1200*(PMCode == "P") )
    #print(time24Hour)
    return time24Hour


def checkWithinMyHours(classListing, startTime, pmCode1, endTime, pmCode2):
    if classListing[6] is None or classListing[7] is None or classListing[8] is None:
        return True
    
    startTime1 = convertTimeTo24(classListing[6], classListing[8])
    endTime1 = convertTimeTo24(classListing[7], classListing[8])
    startTime2 = convertTimeTo24(startTime, pmCode1)
    endTime2 = convertTimeTo24(endTime, pmCode2)
    
    #if ( ((int(startTime1) < int(startTime2)) and (int(endTime1) < int(startTime2))) or  ((int(startTime1) < int(startTime2)) and (int(endTime1) < int(startTime2))) ):
    if( int(startTime1)> int(startTime2) and int(endTime1) < int(endTime2)):
        #print("Time Good")
        return True
    else:
        #print("OVERLAP TIME")
        return False

def checkNoTimeConflicts(schedule, classListing):
    if classListing[5] is None or classListing[6] is None or classListing[7] is None or classListing[8] is None:
        return True
    #print(classListing[5]," ",classListing[6]," ",classListing[7]," ",classListing[8])
    for c in schedule:
        if c[5] is not None and c[6] is not None and c[7] is not None and c[8] is not None:
            if classListing[5] == c[5]:
                startTime1 = convertTimeTo24(classListing[6], classListing[8])
                endTime1 = convertTimeTo24(classListing[7], classListing[8])
                startTime2 = convertTimeTo24(c[6], c[8])
                endTime2 = convertTimeTo24(c[7], c[8])
                if not ( ((int(startTime1) < int(startTime2)) and (int(endTime1) < int(startTime2))) or  ((int(startTime1) > int(startTime2)) and (int(endTime1) > int(startTime2))) ):
                    #print("time conflict with an already scheduled Class")
                    return False
        
    return True

        

def checkForDoubleClass(schedule, classCode):
    for i in schedule:
        if parseClassCode(i) == classCode:
            print("Repeat Class")
            return True
    return False

def createSchedule(majorName, transcript, targetNumClasses, next_semester, morningStart, pm1, eveningEnd, pm2):
    possibleClasses, unusedClasses = satisfyRequirementBlock([majorName, "Business_Curriculum"], transcript)
    print("Remaining Requirements: \n", possibleClasses)
    suggestedSchedule = []
    numClasses = 0
    print("Creating Schedule...")
    for i1 in next_semester:
        for i in i1:
            #print(i[3]) #Name
            day = i[5]
            startTime = i[6]
            endTime = i[7]
            pmCode = i[8]
            classCode = parseClassCode(i)
            #print("\nFind Class: ", classCode)
            for t1 in possibleClasses: #dictionary level
                for t2 in t1:   #tuple level
                    if t1.get(t2) >0:
                        for t3 in t2: #string level
                            #print(t3)
                            if classIsAMatch(t3, classCode): ###
                                if not checkForDoubleClass(suggestedSchedule, classCode) and checkNoTimeConflicts(suggestedSchedule, i) and checkWithinMyHours(i, morningStart, pm1, eveningEnd, pm2):
                                    numClasses +=1
                                    suggestedSchedule.append(i)
                                    #print("FOUND: ",classCode, " for ",t3)
                                    #print(t1)
                                    #print(t2)
                                    reqVal = t1.get(t2) -1
                                    #print(reqVal)
                                    t1[t2] = reqVal
                                    if numClasses >= targetNumClasses:
                                        return suggestedSchedule
    print("\nNon-Applicable Classes: ",unusedClasses)
    return suggestedSchedule




#majorName = "Engineering_Management"
#transcript = ["16:137:500", "16:180:545", "16:137:600", "22:222:222", '16:137:502', '16:137:650', '16:137:507']
#targetNumClasses = 7
#next_semester = [[['16', '540', '505', 'ENG DECISION MAKING', 1, 'M', '0640', '0930', 'P'], ['16', '540', '510', 'DET MODELS IN IE', 1, 'TH', '0640', '0930', 'P'], ['16', '540', '550', 'SPEC PROBS IN I.E.', 1, None, None, None, None], ['16', '540', '552', 'MFG PROJECT', 1, None, None, None, None], ['16', '540', '573', 'ADV MFG PROCESSES', 1, 'T', '0640', '0930', 'P'], ['16', '540', '580', 'QUALITY MANAGEMENT', 1, 'TH', '0640', '0930', 'P'], ['16', '540', '585', 'SYS RELIABILITY ENGI', 1, 'W', '0640', '0930', 'P'], ['16', '540', '616', 'ADV STOCH MOD ISE', 1, 'TH', '0320', '0620', 'P'], ['16', '540', '691', 'SEMINAR IN I & SE', 1, 'T', '0500', '0600', 'P'], ['16', '540', '694', 'ADV TOPICS IN I.E.', 0, 'M', '0320', '0620', 'P'], ['16', '540', '701', 'RESEARCH INDUS ENGG', 13, None, None, None, None], ['16', '540', '800', 'MATRICULATION CONTD', 1, None, None, None, None], ['16', '540', '811', 'GRADUATE FELLOWSHIP', 1, None, None, None, None], ['16', '540', '844', 'RESEARCH INTERNSHIP', 1, None, None, None, None], ['16', '540', '866', 'FULL GA APPOINTMENT', 1, None, None, None, None], ['16', '540', '867', 'PRAT GA APPOINTMENT', 1, None, None, None, None], ['16', '540', '877', 'FULL TA APPOINTMENT', 1, None, None, None, None], ['16', '540', '878', 'PART TA APPOINTMENT', 1, None, None, None, None]]]
next_semester = [[['16', '137', '500', 'ETHICS IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '502', 'PRINC OF COMM/LDRSHP', ['openSections'], 'M', '0140', '0440', 'P'], ['16', '137', '502', 'PRINC OF COMM/LDRSHP', ['openSections'], 'M', '0640', '0930', 'P'], ['16', '137', '503', 'COLL SCI/TECH MNGMT', ['openSections'], None, None, None, None], ['16', '137', '504', 'COLL PROFESSIONAL', ['openSections'], None, None, None, None], ['16', '137', '507', 'MARKT ASSES BUS & SC', ['openSections'], 'W', '0600', '0900', 'P'], ['16', '137', '511', 'DRUG DIS PRECLIN DEV', ['openSections'], 'M', '0640', '0930', 'P'], ['16', '137', '530', 'PRIN ACCT FINAN SCI', ['openSections'], 'T', '0640', '0930', 'P'], ['16', '137', '535', 'USABILITY EVALUATION', ['openSections'], None, None, None, None], ['16', '137', '541', 'ENTRPRS SFTWR ARCHIT', ['openSections'], 'M', '0640', '0930', 'P'], ['16', '137', '550', 'ANALYT DISC INFRMTCS', ['openSections'], 'TH', '0600', '0900', 'P'], ['16', '137', '561', 'CYBERSECURITY', ['openSections'], None, None, None, None], ['16', '137', '571', 'PRO DEV FORM PER CAR', ['openSections'], 'W', '0640', '0930', 'P'], ['16', '137', '582', 'FUND OF REG AFFAIRS', ['openSections'], 'T', '0640', '0930', 'P'], ['16', '137', '600', 'MNG SCI/TECH CAPSTNE', ['openSections'], 'W', '0640', '0930', 'P'], ['16', '137', '602', 'SPEC TPC IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '602', 'SPEC TPC IN SCI/TECH', ['openSections'], 'TH', '0500', '0630', 'P'], ['16', '137', '602', 'SPEC TPC IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '603', 'SPEC TPC IN SCI/TECH', ['openSections'], 'M', '0400', '0630', 'P'], ['16', '137', '605', 'SPECIAL PROBLEMS', ['openSections'], None, None, None, None], ['16', '137', '612', 'RESEARCH INTERNSHIP', ['openSections'], None, None, None, None], ['16', '137', '616', 'NEXTGEN BIOTECH/GENO', ['openSections'], 'TH', '0555', '0855', 'P'], ['16', '137', '617', 'BIOINFORMATICS', ['openSections'], 'W', '0355', '0655', 'P'], ['16', '137', '800', 'MATRICULATION CONTD', ['openSections'], None, None, None, None], ['16', '137', '877', 'TCHNG ASSISTANTSHIP', ['openSections'], None, None, None, None], ['16', '137', '581', 'STAT CLINICAL/TRAN', ['openSections'], None, None, None, None], ['16', '137', '609', 'PROFESSNAL INTRNSHP', ['openSections'], None, None, None, None], ['16', '137', '651', 'TPCS MNGMT & PRF DVL', ['openSections'], None, None, None, None], ['16', '137', '651', 'TPCS MNGMT & PRF DVL', ['openSections'], None, None, None, None]], [['22', '799', '580', 'OPERATIONS ANALYSIS', ['openSections'], 'T', '0640', '0940', 'P'], ['22', '799', '607', 'SUPPLY CHN MGT STRAT', ['openSections'], 'M', '0640', '0940', 'P'], ['22', '799', '608', 'PROCURMNT&GLOBL SORC', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '799', '640', 'SC FINANCIAL MGMT', ['openSections'], 'T', '0640', '0940', 'P'], ['22', '799', '647', 'PHARMA PURCH&SC MGT', ['openSections'], 'S', '0900', '1200', 'A'], ['22', '799', '653', 'PRDCT DSGN&SC ALGNMT', ['openSections'], 'S', '0900', '1200', 'A'], ['22', '799', '659', 'SC SOLUTN ERP/SAP I', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '799', '661', 'PROJECT MANAGEMENT', ['openSections'], 'TH', '0640', '0940', 'P'], ['22', '799', '663', 'ANLYS/MGT VALUE CHAI', ['openSections'], 'M', '0640', '0930', 'P'], ['22', '799', '668', 'SALES&OPERATION PLAN', ['openSections'], 'S', '0900', '1200', 'A'], ['22', '799', '676', 'LEAN SIX SIGMA', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '799', '691', 'PROJECT MGMT', ['openSections'], 'TH', '0640', '0940', 'P'], ['22', '799', '692', 'SC STRATEGY NON-RBS', ['openSections'], 'W', '0640', '0940', 'P']], [['22', '620', '585', 'ORGANIZATN BEHAVIOR', ['openSections'], 'U', '0100', '0400', 'P'], ['22', '620', '588', 'STRATEGIC MANAGEMENT', ['openSections'], 'TH', '0640', '0940', 'P'], ['22', '620', '601', 'MGT OF INNOV& TECH', ['openSections'], 'TH', '0640', '0930', 'P'], ['22', '620', '603', 'EXECUTIVE LEADERSHIP', ['openSections'], None, None, None, None], ['22', '620', '604', 'HUMAN RESOURCE MGT', ['openSections'], 'W', '0640', '0930', 'P'], ['22', '620', '606', "MG'G STRAT TRANSFORM", ['openSections'], 'S', '0100', '0430', 'P'], ['22', '620', '617', 'NEGOTIATIONS', ['openSections'], 'M', '0640', '0940', 'P'], ['22', '620', '648', 'CROSS CULTURAL MGT', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '620', '674', 'SOC ENTREP&PHILANTHR', ['openSections'], 'M', '0640', '0940', 'P'], ['22', '620', '680', 'MERGERS & ACQUISITIO', ['openSections'], 'T', '0640', '0930', 'P'], ['22', '620', '687', 'CTEC 2 MDL TO VENTUR', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '620', '688', 'CTEC 2: PRACTICUM', ['openSections'], None, None, None, None]], [['16', '711', '611', 'SEL TOPICS OPER RES', ['openSections'], 'N/A', 'N/A', 'N/A', 'N/A'], ['16', '711', '614', 'SEL TOPICS OPER RES', ['openSections'], None, None, None, None], ['16', '711', '695', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '696', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '697', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '698', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '699', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '702', 'RES IN OPERATNS RES', ['openSections'], None, None, None, None], ['16', '711', '800', 'MATRICULATION CONTD', ['openSections'], None, None, None, None], ['16', '711', '811', 'GRADUATE FELLOWSHIP', ['openSections'], None, None, None, None], ['16', '711', '855', 'GRADUATE TRAINEESHIP', ['openSections'], None, None, None, None], ['16', '711', '866', 'FULL GA APPOINTMENT', ['openSections'], None, None, None, None], ['16', '711', '867', 'PART GA APPOINTMENT', ['openSections'], None, None, None, None], ['16', '711', '877', 'FULL TA APPOINTMENT', ['openSections'], None, None, None, None], ['16', '711', '878', 'PART TA APPOINTMENT', ['openSections'], None, None, None, None]], [['38', '533', '533', 'MNG WORKFORCE FLOW', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '540', 'HR DEC MAK: FIN DECS', ['openSections'], 'M', '0720', '1000', 'P'], ['38', '533', '542', 'HR DEC MAK: D B D', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '565', 'ECON & DEM OF L M', ['openSections'], 'T', '0720', '1000', 'P'], ['38', '533', '566', 'EMPLOYMENT LAW', ['openSections'], 'W', '0720', '1000', 'P'], ['38', '533', '580', 'HR STRATEGY I: INTRO', ['openSections'], 'W', '0720', '1000', 'P'], ['38', '533', '590', 'HR STRATEGY II: BUS', ['openSections'], 'TH', '0430', '0710', 'P'], ['38', '533', '601', 'INDIV STDY IN HRM', ['openSections'], None, None, None, None], ['38', '533', '602', 'INDIV STDY IN HRM', ['openSections'], None, None, None, None], ['38', '533', '610', 'SEL PROBS IN HRM', ['openSections'], 'F', '0930', '1210', 'A'], ['38', '533', '613', 'SEL PROBS IN HRM', ['openSections'], 'F', '0100', '0340', 'P'], ['38', '533', '614', 'SEL PROBS IN HRM', ['openSections'], 'W', '0430', '0710', 'P'], ['38', '533', '616', 'SEL PROBLEMS IN HRM', ['openSections'], 'T', '0430', '0710', 'P'], ['38', '533', '617', 'SEL. PROBLEMS IN HRM', ['openSections'], 'W', '0430', '0710', 'P'], ['38', '533', '618', 'SEL. PROBLEMS IN HRM', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '634', 'DEV HUMAN CAPITAL', ['openSections'], 'TH', '0430', '0710', 'P'], ['38', '533', '635', 'MNG REWARDS SYSTEMS', ['openSections'], 'T', '0430', '0710', 'P'], ['38', '533', '636', 'CORPORATE GOVERNANCE', ['openSections'], 'TH', '0930', '1210', 'A'], ['38', '533', '665', 'MNG GLOBAL WORKFORCE', ['openSections'], 'T', '0430', '0710', 'P'], ['38', '533', '680', 'HR STRAT III:MEASUR', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '685', 'STRATEGIC ORG CHANGE', ['openSections'], 'TH', '1000', '1240', 'A'], ['38', '533', '690', 'HR STRAT IV:DESIGN', ['openSections'], 'W', '0430', '0710', 'P'], ['38', '533', '702', 'RESEARCH IN HRM', ['openSections'], None, None, None, None], ['38', '533', '703', "MASTER'S THESIS-HRM", ['openSections'], None, None, None, None], ['38', '533', '800', 'MATRIC CONT', ['openSections'], None, None, None, None]], [['34', '832', '502', 'PH PREPAREDNESS II', ['openSections'], 'T', '0430', '0720', 'P'], ['34', '832', '513', 'ISSUES IN HLTH DISPA', ['openSections'], 'M', '0110', '0410', 'P']]]
next_semester = [[['16', '137', '500', 'ETHICS IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '502', 'PRINC OF COMM/LDRSHP', ['openSections'], 'M', '0140', '0440', 'P'], ['16', '137', '502', 'PRINC OF COMM/LDRSHP', ['openSections'], 'M', '0640', '0930', 'P'], ['16', '137', '503', 'COLL SCI/TECH MNGMT', ['openSections'], None, None, None, None], ['16', '137', '504', 'COLL PROFESSIONAL', ['openSections'], None, None, None, None], ['16', '137', '507', 'MARKT ASSES BUS & SC', ['openSections'], 'W', '0600', '0900', 'P'], ['16', '137', '511', 'DRUG DIS PRECLIN DEV', ['openSections'], 'M', '0640', '0930', 'P'], ['16', '137', '530', 'PRIN ACCT FINAN SCI', ['openSections'], 'T', '0640', '0930', 'P'], ['16', '137', '535', 'USABILITY EVALUATION', ['openSections'], None, None, None, None], ['16', '137', '541', 'ENTRPRS SFTWR ARCHIT', ['openSections'], 'M', '0640', '0930', 'P'], ['16', '137', '550', 'ANALYT DISC INFRMTCS', ['openSections'], 'TH', '0600', '0900', 'P'], ['16', '137', '561', 'CYBERSECURITY', ['openSections'], None, None, None, None], ['16', '137', '571', 'PRO DEV FORM PER CAR', ['openSections'], 'W', '0640', '0930', 'P'], ['16', '137', '582', 'FUND OF REG AFFAIRS', ['openSections'], 'T', '0640', '0930', 'P'], ['16', '137', '600', 'MNG SCI/TECH CAPSTNE', ['openSections'], 'W', '0640', '0930', 'P'], ['16', '137', '602', 'SPEC TPC IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '602', 'SPEC TPC IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '602', 'SPEC TPC IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '603', 'SPEC TPC IN SCI/TECH', ['openSections'], None, None, None, None], ['16', '137', '605', 'SPECIAL PROBLEMS', ['openSections'], None, None, None, None], ['16', '137', '612', 'RESEARCH INTERNSHIP', ['openSections'], None, None, None, None], ['16', '137', '616', 'NEXTGEN BIOTECH/GENO', ['openSections'], 'TH', '0555', '0855', 'P'], ['16', '137', '617', 'BIOINFORMATICS', ['openSections'], 'W', '0355', '0655', 'P'], ['16', '137', '800', 'MATRICULATION CONTD', ['openSections'], None, None, None, None], ['16', '137', '877', 'TCHNG ASSISTANTSHIP', ['openSections'], None, None, None, None], ['16', '137', '581', 'STAT CLINICAL/TRAN', ['openSections'], None, None, None, None], ['16', '137', '609', 'PROFESSNAL INTRNSHP', ['openSections'], None, None, None, None], ['16', '137', '651', 'TPCS MNGMT & PRF DVL', ['openSections'], None, None, None, None], ['16', '137', '651', 'TPCS MNGMT & PRF DVL', ['openSections'], None, None, None, None]], [['22', '799', '580', 'OPERATIONS ANALYSIS', ['openSections'], 'T', '0640', '0940', 'P'], ['22', '799', '607', 'SUPPLY CHN MGT STRAT', ['openSections'], 'M', '0640', '0940', 'P'], ['22', '799', '608', 'PROCURMNT&GLOBL SORC', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '799', '640', 'SC FINANCIAL MGMT', ['openSections'], 'T', '0640', '0940', 'P'], ['22', '799', '647', 'PHARMA PURCH&SC MGT', ['openSections'], 'S', '0900', '1200', 'A'], ['22', '799', '653', 'PRDCT DSGN&SC ALGNMT', ['openSections'], 'S', '0900', '1200', 'A'], ['22', '799', '659', 'SC SOLUTN ERP/SAP I', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '799', '661', 'PROJECT MANAGEMENT', ['openSections'], 'TH', '0640', '0940', 'P'], ['22', '799', '663', 'ANLYS/MGT VALUE CHAI', ['openSections'], 'M', '0640', '0930', 'P'], ['22', '799', '668', 'SALES&OPERATION PLAN', ['openSections'], 'S', '0900', '1200', 'A'], ['22', '799', '676', 'LEAN SIX SIGMA', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '799', '691', 'PROJECT MGMT', ['openSections'], 'TH', '0640', '0940', 'P'], ['22', '799', '692', 'SC STRATEGY NON-RBS', ['openSections'], 'W', '0640', '0940', 'P']], [['22', '620', '585', 'ORGANIZATN BEHAVIOR', ['openSections'], 'U', '0100', '0400', 'P'], ['22', '620', '588', 'STRATEGIC MANAGEMENT', ['openSections'], 'TH', '0640', '0940', 'P'], ['22', '620', '601', 'MGT OF INNOV& TECH', ['openSections'], 'TH', '0640', '0930', 'P'], ['22', '620', '603', 'EXECUTIVE LEADERSHIP', ['openSections'], None, None, None, None], ['22', '620', '604', 'HUMAN RESOURCE MGT', ['openSections'], 'W', '0640', '0930', 'P'], ['22', '620', '606', "MG'G STRAT TRANSFORM", ['openSections'], 'S', '0100', '0430', 'P'], ['22', '620', '617', 'NEGOTIATIONS', ['openSections'], 'M', '0640', '0940', 'P'], ['22', '620', '648', 'CROSS CULTURAL MGT', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '620', '674', 'SOC ENTREP&PHILANTHR', ['openSections'], 'M', '0640', '0940', 'P'], ['22', '620', '680', 'MERGERS & ACQUISITIO', ['openSections'], 'T', '0640', '0930', 'P'], ['22', '620', '687', 'CTEC 2 MDL TO VENTUR', ['openSections'], 'W', '0640', '0940', 'P'], ['22', '620', '688', 'CTEC 2: PRACTICUM', ['openSections'], None, None, None, None]], [['16', '711', '611', 'SEL TOPICS OPER RES', ['openSections'], 'N/A', 'N/A', 'N/A', 'N/A'], ['16', '711', '614', 'SEL TOPICS OPER RES', ['openSections'], None, None, None, None], ['16', '711', '695', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '696', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '697', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '698', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '699', 'INDEPENDENT STUDY OR', ['openSections'], None, None, None, None], ['16', '711', '702', 'RES IN OPERATNS RES', ['openSections'], None, None, None, None], ['16', '711', '800', 'MATRICULATION CONTD', ['openSections'], None, None, None, None], ['16', '711', '811', 'GRADUATE FELLOWSHIP', ['openSections'], None, None, None, None], ['16', '711', '855', 'GRADUATE TRAINEESHIP', ['openSections'], None, None, None, None], ['16', '711', '866', 'FULL GA APPOINTMENT', ['openSections'], None, None, None, None], ['16', '711', '867', 'PART GA APPOINTMENT', ['openSections'], None, None, None, None], ['16', '711', '877', 'FULL TA APPOINTMENT', ['openSections'], None, None, None, None], ['16', '711', '878', 'PART TA APPOINTMENT', ['openSections'], None, None, None, None]], [['38', '533', '533', 'MNG WORKFORCE FLOW', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '540', 'HR DEC MAK: FIN DECS', ['openSections'], 'M', '0720', '1000', 'P'], ['38', '533', '542', 'HR DEC MAK: D B D', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '565', 'ECON & DEM OF L M', ['openSections'], 'T', '0720', '1000', 'P'], ['38', '533', '566', 'EMPLOYMENT LAW', ['openSections'], 'W', '0720', '1000', 'P'], ['38', '533', '580', 'HR STRATEGY I: INTRO', ['openSections'], 'W', '0720', '1000', 'P'], ['38', '533', '590', 'HR STRATEGY II: BUS', ['openSections'], 'TH', '0430', '0710', 'P'], ['38', '533', '601', 'INDIV STDY IN HRM', ['openSections'], None, None, None, None], ['38', '533', '602', 'INDIV STDY IN HRM', ['openSections'], None, None, None, None], ['38', '533', '610', 'SEL PROBS IN HRM', ['openSections'], 'F', '0930', '1210', 'A'], ['38', '533', '613', 'SEL PROBS IN HRM', ['openSections'], 'F', '0100', '0340', 'P'], ['38', '533', '614', 'SEL PROBS IN HRM', ['openSections'], 'W', '0430', '0710', 'P'], ['38', '533', '616', 'SEL PROBLEMS IN HRM', ['openSections'], 'T', '0430', '0710', 'P'], ['38', '533', '617', 'SEL. PROBLEMS IN HRM', ['openSections'], 'W', '0430', '0710', 'P'], ['38', '533', '618', 'SEL. PROBLEMS IN HRM', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '634', 'DEV HUMAN CAPITAL', ['openSections'], 'TH', '0430', '0710', 'P'], ['38', '533', '635', 'MNG REWARDS SYSTEMS', ['openSections'], 'T', '0430', '0710', 'P'], ['38', '533', '636', 'CORPORATE GOVERNANCE', ['openSections'], 'TH', '0930', '1210', 'A'], ['38', '533', '665', 'MNG GLOBAL WORKFORCE', ['openSections'], 'T', '0430', '0710', 'P'], ['38', '533', '680', 'HR STRAT III:MEASUR', ['openSections'], 'M', '0430', '0710', 'P'], ['38', '533', '685', 'STRATEGIC ORG CHANGE', ['openSections'], 'TH', '1000', '1240', 'A'], ['38', '533', '690', 'HR STRAT IV:DESIGN', ['openSections'], 'W', '0430', '0710', 'P'], ['38', '533', '702', 'RESEARCH IN HRM', ['openSections'], None, None, None, None], ['38', '533', '703', "MASTER'S THESIS-HRM", ['openSections'], None, None, None, None], ['38', '533', '800', 'MATRIC CONT', ['openSections'], None, None, None, None]], [['34', '832', '502', 'PH PREPAREDNESS II', ['openSections'], 'T', '0430', '0720', 'P'], ['34', '832', '513', 'ISSUES IN HLTH DISPA', ['openSections'], 'M', '0110', '0410', 'P']]]

#sched = (createSchedule(majorName, transcript, targetNumClasses, next_semester, "0900", "A", "1000", "P"))
#print("%%%%%%%%%")

def printFinalSchedule(schedule):
    print("\nYour Schedule: \n")
    for c in schedule:
        print(parseClassCode(c), " - ", c[3], " - ", c[5], " ", c[6], " - ", c[7], c[8])


#printFinalSchedule(sched)








