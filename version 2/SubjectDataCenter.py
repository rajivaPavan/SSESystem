subjectEntities=[]
  
def addSubject(id, subjectName, stream):
    "store the subject inside the subject data list. return True if operation is successful"
    for subject in subjectEntities:
        if subject["id"]==id:
            return False;
        if subject["subjectName"]==subjectName :
            print("Two subjects can not have same name")
            return False;

    #add the new Subject
    newSubject={}
    newSubject["id"]=id
    newSubject["subjectName"]=subjectName
    newSubject["stream"]=stream
    subjectEntities.append(newSubject)
    return True;

def modifySubject(id, subjectName, stream):
    "modify content of a already stored subject. return True if operation is successful"
    for subject in subjectEntities:
        if(subject["id"]==id):
            selectedSubject=subject
            selectedSubject["subjectName"]=subjectName
            selectedSubject["stream"]=stream
            return True;
    return False;

def deleteSubject(id):
    "delete a subject from the system. return True if operation is successful"
    for subject in subjectEntities:
        if(subject["id"]==id):
            selectedSubject=subject
            subjectEntities.remove(selectedSubject)
            return True;
    return False;
    

def showSubject(subjectName):
    "prints dictionary with subject details"
    for subject in subjectEntities:
        if(subject["subjectName"]==subjectName):
            selectedSubjectCopy=subject.copy()
            break
    del selectedSubjectCopy["id"]
    print("Subject Name: "+selectedSubjectCopy["subjectName"])
    print("Stream: "+selectedSubjectCopy["stream"])
    return;

def getSubjectById(id):
    "return the subjct that has given id. Otherwise return None"

    for subject in subjectEntities:
        if(subject["id"]==id):
            return subject.copy(); 
    return None;
    

def getSubjectBySubjectName(subjectName):
    "return the subjct that has given id. Otherwise return None"

    subjectEntityList=[]
     
    for subject in subjectEntities:
        if(subject["subjectName"]==subjectName):
            subjectEntityList.append(subject.copy()) # give a copy of the dictionary as returned value.
    return subjectEntityList;
    
def getSubjectId(name):
    "return subject id when name is given"
    for subject in subjectEntities:
        if subject["subjectName"]==name:
           return(subject["id"]);
