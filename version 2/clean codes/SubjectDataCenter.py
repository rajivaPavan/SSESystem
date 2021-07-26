#here stores all the subjects
#CRUD Create Read Update Delete

subjectEntities=[]

def getSubjectId(name):
    #return subject id when subject name and stream is given (this function is for the system usage)
    for subject in subjectEntities:
        if(subject["name"]==name and subject["stream"]==stream):
            return subject["id"];
        
def addSubject(id, subjectName, stream):
    "store the subject inside the subject data list. return True if operation is successful"
    #todo- check the a subject with this id already exist in system. If so, return false
    #todo- check the a subject with this subject name already exist in system. If so, return false
    #return False;

    #add the new Subject
    newSubject={}
    newSubject["id"]=id
    newSubject["subjectName"]=subjectName
    newSubject["stream"]=stream
    subjectEntities.append(newSubject)
    return True;

def modifySubject(id, subjectName, stream):
    "modify content of a already stored subject. return True if operation is successful"
    #todo- check the a subject with this id already exist in system. If not, return false
    #return False;

    #choose the Subject
    for subject in subjectEntities:
        if(subject["id"]==id):
            selectedSubject=subject

    selectedSubject["subjectName"]=subjectName
    selectedSubject["stream"]=stream
    return True;

def deleteSubject(id):
    "delete a subject from the system. return Tue if operation is successful"
    #todo- check the a subject with this id already exist in system. If not, return false
    #return False;

    #choose the Subject
    for subject in subjectEntities:
        if(subject["id"]==id):
            selectedSubject=subject
    subjectEntities.remove(selectedSubject)
    return True;

def getSubjectById(id):
    "return the subjct that has given id. Otherwise return None"

    #choose the Subject
    for subject in subjectEntities:
        if(subject["id"]==id):
            return subject.copy(); # give a copy of the dictionary as returned value.
    return None;
    #we can check this using if statement 'if ret_value is not None'

def getSubjectBySubjectName(subjectName):
    "return the subjct that has given id. Otherwise return None"

    subjectEntityList=[]
    #choose the Subject
    for subject in subjectEntities:
        if(subject["subjectName"]==subjectName):
            subjectEntityList.append(subject.copy()) # give a copy of the dictionary as returned value.
    return subjectEntityList;
    #we can check this using if statement 'if ret_value is not None'
