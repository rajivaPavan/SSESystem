import RelationshipsDataCenter as rdc
import pickle

with open("SubjectData.txt", "rb") as f:
    try:
        subjectEntities = pickle.load(f)
    except EOFError:
        subjectEntities = []
        
def getSubjectId(name):
    """return subject id when subject name is given (this function is for the system usage)"""
    for subject in subjectEntities:
        if subject["subjectName"] == name:
            return subject["id"]


def getSubjectById(subjectId):
    """return the subject that has given id. Otherwise return None"""
    for subject in subjectEntities:
        if subject["subjectId"] == subjectId:
            return subject.copy()
    return None

def addSubject(subjectName, stream):
    "store the subject inside the subject data list. return True if operation is successful"
    for subject in subjectEntities:
        if subject["subjectName"]==subjectName :
            print("Two subjects can not have same name")
            return False

    # generating ID
    if subjectEntities == []:
        lastSavedIdNumber = "0"
    else:
        lastSavedId = subjectEntities[-1]["subjectId"]  # update subjectId as first element in teacherEntities list
        lastSavedIdNumber = lastSavedId[2:]
    numberOfDigitsInID = 3
    if lastSavedIdNumber == "9" * len(lastSavedIdNumber):
        numberOfDigitsInID = len(lastSavedIdNumber) + 1
    subjectId = "SB" + str(int(lastSavedIdNumber) + 1).rjust(numberOfDigitsInID, "0")

    #add the new Subject
    newSubject={}
    newSubject["subjectId"] = subjectId
    newSubject["subjectName"]=subjectName
    newSubject["stream"]=stream
    subjectEntities.append(newSubject)
    print(f"Subject is added into the system, Subject Id is {subjectId}.")
    return True

def modifySubject(subjectId, subjectName, stream):
    "modify content of a already stored subject. return True if operation is successful"
    for subject in subjectEntities:
        if subject["subjectId"] == subjectId:
            selectedSubject=subject
            selectedSubject["subjectName"]=subjectName
            selectedSubject["stream"]=stream
            return True
    return False

def deleteSubject(subjectId):
    """delete a subject from the system. return True if operation is successful"""
    for subject in subjectEntities:
        if subject["subjectId"] == subjectId:
            selectedSubject = subject
            subjectEntities.remove(selectedSubject)
            return True
    return False
    

def showSubject(subjectId):
    """prints dictionary with subject details"""
    selectedSubjectCopy = getSubjectById(subjectId)
    print("Subject Name: "+selectedSubjectCopy["subjectName"])
    print("Stream: "+selectedSubjectCopy["stream"])
    return

def saveSubjectsData():
    """saves subject data in text file in write binary mode"""
    with open("SubjectData.txt", "wb") as subjectData:
        pickle.dump(subjectEntities, subjectData)