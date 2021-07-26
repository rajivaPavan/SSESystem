from SubjectDataCenter import addSubject,modifySubject,deleteSubject,showSubject,getSubjectById,getSubjectBySubjectName,getSubjectId
from StudentSubjectRelation import getRelationshipsBySubjectId   
###########################################################################
    
def isValidSubjectName(subjectName):
    for letter in subjectName:
        if letter.isdigit():
            print("Subject name should not have numbers included")
            return False;
        if letter.isspace():
            print("Subject name should not have white spaces")
            return False;
    return True;

def isValidStream(stream):
    if stream!= "A/L" and stream!= "O/L" :
        print("Stream should be either A/L or O/L")
        return False;
    return True;
        
###########################################################################
subjectIdSeq=0
def addSubjectHandler(subjectName,stream):
    if ( (isValidStream(stream))and (isValidSubjectName(subjectName))):
        global subjectIdSeq
        subjectIdSeq+=1
        isSubjectAdded=addSubject(subjectIdSeq,subjectName,stream)
        if isSubjectAdded:
            print("Subject added correctly")
    return;

def modifySubjectHandler(oldName,newName,Stream):
    if ( (isValidStream(Stream))and(isValidSubjectName(oldName)) and (isValidSubjectName(newName))):
        if getSubjectBySubjectName(oldName)==[]:
            print("Subject with " ,oldName ," does not exist")
        else:
            if getSubjectBySubjectName(newName)!=[]:
                print("Two subjects can not have same name")
            else:
                subId=getSubjectId(oldName)
                isSubjectModified=modifySubject(subId,newName,Stream)
                if (isSubjectModified):
                    print("Subject modified correctly")       
    return;
        

def removeSubjectHandler(subjectName):
    if (isValidSubjectName(subjectName)):
        if getSubjectBySubjectName(subjectName)==[]:
            print("Subject with",subjectName,"does not exist")
            return;
    subjectId=getSubjectId(subjectName)       
    relations=getRelationshipsBySubjectId(subjectId)
    if relations==[]:
        isDeleted=deleteSubject(subjectId)
        if isDeleted:
            print("subject deleted correctly")
    else:
        print("Can not be deleted. Subject has scores stored in the system")
    return;        


def showSubjectHandler(subject):
    if (isValidSubjectName(subject)):
        if getSubjectBySubjectName(subject)==[]:
            print("Subject with ",subject," does not exist")
        else:
            showSubject(subject)    
    return;


    
