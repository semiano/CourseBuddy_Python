import json, requests #3rd party Libraries

global SOC_KEY
SOC_KEY = "d0f1ee9f0b4836d7a0060b433d16b397" #developer Key provided by Rutgers to SM
#masterClassList = []

def buildURLstring(semester, subj, campus, level):
    #semester = "92015"
    #subj = "137"
    #campus = "NB"
    #level = "G"
    url = "http://sauron.rutgers.edu/~rfranknj/soc/api.php?key=%s&semester=%s&subj=%s&campus=%s&level=%s"%(SOC_KEY, semester, subj, campus, level)
    print(url)
    return url

def queryAPI(url):
    import json, requests
    resp = requests.get(url=url)
    json = json.loads(resp.text)
    return json
    
def builtDepartmentClassList(json):
    classList = []
    #print(json)
    for i in json:
        offeringCode = i["offeringUnitCode"]
        subject = i["subject"]
        courseNumber = i["courseNumber"]
        title = i["title"]
        openSections = ["openSections"]
        try: meetingDay = i["sections"][0].get("meetingTimes")[0].get("meetingDay")
        except: meetingDay = "N/A"
        try: startTime = i["sections"][0].get("meetingTimes")[0].get("startTime")
        except: startTime = "N/A"
        try:endTime = i["sections"][0].get("meetingTimes")[0].get("endTime")
        except: endTime = "N/A"
        try:pmCode = i["sections"][0].get("meetingTimes")[0].get("pmCode")
        except: pmCode = "N/A"
        
        classListing = [offeringCode, subject, courseNumber, title, openSections, meetingDay, startTime, endTime, pmCode]
        classList.append(classListing)

        #classList.append([offeringCode, subject, courseNumber, title ,  openSections, meetingDay,  startTime, endTime, pmCode])
        #print(i["offeringUnitCode"],":", i["subject"],":", i["courseNumber"], " --- ", i["title"] , " --- ", i["openSections"]," - ", i["sections"][0].get("meetingTimes")[0].get("meetingDay"), " - ", i["sections"][0].get("meetingTimes")[0].get("startTime"), " - ", i["sections"][0].get("meetingTimes")[0].get("endTime"), " - ", i["sections"][0].get("meetingTimes")[0].get("pmCode"))
        #classList.append([i["offeringUnitCode"], i["subject"], i["courseNumber"], i["title"] ,  i["openSections"], i["sections"][0].get("meetingTimes")[0].get("meetingDay"),  i["sections"][0].get("meetingTimes")[0].get("startTime"), i["sections"][0].get("meetingTimes")[0].get("endTime"), i["sections"][0].get("meetingTimes")[0].get("pmCode")])
    return classList


def buildMasterClassList(semester = "92015", subjList = ["137"], campus = "NB", level = "G"):
    masterClassList = []
    print("\nClasses for Department %s"%(subjList))
    for subj in subjList:
        #import time
        #time.sleep(1)
        url = buildURLstring(semester, subj, campus, level)
        json = queryAPI(url)
        
        classList = builtDepartmentClassList(json)
        masterClassList.append(classList)

    return masterClassList

#buildMasterClassList(subjList = ["137", "540"]) #BUILDS MASTER CLASS LIST; now called in main program
#print("\n\n Double Checking List\n\n")
#for c in masterClassList: #test print
#    print(c)
#    print("\n")


#!!!! JSON fields - For Reference !!!!:

#preReqNotes
#expandedTitle
#coreCodes
#credits
#offeringUnitCode
#offeringUnitTitle
#courseNotes
#unitNotes
#courseNumber
#sections #SUB DICTIONARY SHOWN BELOW

#{'subtitle': None,
#'legendKey': None,
#'openStatus': True,
#'specialPermissionDropCode': None,
#'majors': [],
#'specialPermissionAddCode': None,
#'comments': [],
#'printed': 'Y',
#'examCode': 'A',
#'sectionEligibility': None,
#'sessionDatePrintIndicator': 'Y',
#'subtopic': None,
#'sessionDates': None,
#'sectionNotes': 'THIS SECTION IS FOR PART TIMESTUDENTS ONLY. FULL TIME STUDENTMUST REGISTER FOR DAY SECTION.',
#'instructors': [{'name': 'CASHMAN'}],
#'minors': [],
#'crossListedSections': [],
#'index': '09071',
#'campusCode': 'NB',
#'honorPrograms': [],
#'number': '01',
#'meetingTimes': [{'baClassHours': None, 'buildingCode': 'BRR', 'campusAbbrev': 'LIV', 'meetingModeCode': '02', 'meetingDay': 'M', 'campusLocation': '3', 'meetingModeDesc': 'LEC', 'campusName': 'LIVINGSTON', 'endTime': '0930', 'pmCode': 'P', 'roomNumber': '4073', 'startTime': '0640'}],
#'specialPermissionAddCodeDescription': None,
#'unitMajors': [{'unitCode': '26', 'majorCode': '137'},{'unitCode': '16', 'majorCode': '137'}, {'unitCode': '56', 'majorCode': '137'}],
#'specialPermissionDropCodeDescription': None}
#END OF "SECTIONS" dictionary

#subjectGroupNotes
#synopsisUrl
#title
#subjectNotes
#supplementCode
#openSections
#subject
#courseDescription
#campusCode

#Debugging print statements:
#1]
#for i in data:
#    print(i["offeringUnitCode"],":", i["subject"],":", i["courseNumber"], " --- ", i["title"] , " --- ", i["openSections"]," - ", i["sections"][0].get("meetingTimes")[0].get("meetingDay"), " - ", i["sections"][0].get("meetingTimes")[0].get("startTime"), " - ", i["sections"][0].get("meetingTimes")[0].get("endTime"), " - ", i["sections"][0].get("meetingTimes")[0].get("pmCode"))


#2]
#print(data[1]["sections"])
