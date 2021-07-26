#here stores all the relationship between student and score
import pickle

with open("StudentSubjectRelationData.txt", "rb") as f:
    try:
        studentSubjectRelations = pickle.load(f)
    except EOFError:
        studentSubjectRelations = []

def addStudentSubjectRelation(id, studentId, subjectId, score):
    "adds a relationship to the system. return True if operation is successful"

    #add the new StudentSubjectRelation
    newStudentSubjectRelation={}
    newStudentSubjectRelation["id"]=id
    newStudentSubjectRelation["studentId"]=studentId
    newStudentSubjectRelation["subjectId"]=subjectId
    newStudentSubjectRelation["score"]=score
    studentSubjectRelations.append(newStudentSubjectRelation)
    return True

def modifyStudentSubjectRelation(id, studentId, subjectId, score):
    "modify a relationship in the system. return True if operation is successful"
    
    #choose the StudentSubjectRelation
    for relationship in studentSubjectRelations:
        if(relationship["id"]==id):
            selectedRelationship=relationship
            break
    selectedRelationship["studentId"]=studentId
    selectedRelationship["subjectId"]=subjectId
    selectedRelationship["score"]=score
    return True

def deleteStudentSubjectRelation(id):
    "delete a Relationship from the system. return True if operation is successful"

    #choose the StudentSubjectRelation
    for relationship in studentSubjectRelations:
        if(relationship["id"]==id):
            selectedRelationship=relationship
            break
    studentSubjectRelations.remove(selectedRelationship)
    return True

def getRelationshipsBySubjectId(subjectId):
    "return the relationship list which has mentioned subjectId"
    
    selectedRelationships=[]
    for relationship in studentSubjectRelations:
        if(relationship["subjectId"]==subjectId):
            selectedRelationships.append(relationship.copy())
    return selectedRelationships

def getRelationshipsByStudentId(studentId):
    "return the relationship list which has mentioned studentId"

    selectedRelationships=[]
    for relationship in studentSubjectRelations:
        if(relationship["studentId"]==studentId):
            selectedRelationships.append(relationship.copy())
    return selectedRelationships

def getRelationshipByRelationId(relationId):
    "return a copy of a relationship when relation id is given"
    for relationship in studentSubjectRelations:
        if(relationship["id"]==relationId):
            return relationship.copy()
    return None

def isMarkGiven(studentId,subjectId):
    "return True if student and subject has a mark, else return False"
    for relationship in studentSubjectRelations:
        if(relationship["studentId"]==studentId and relationship["subjectId"]==subjectId):
            return True
    return False

def getRelationId(studentId,subjectId):
    "return relation id when student id and subject id is given"
    for relationship in studentSubjectRelations:
        if(relationship["studentId"]==studentId and relationship["subjectId"]==subjectId):
            return relationship["id"]

        
def saveStudentSubjectData():
    """saves subject data in text file in write binary mode"""
    with open("StudentSubjectRelationData.txt", "wb") as f:
        pickle.dump(studentSubjectRelations, f)