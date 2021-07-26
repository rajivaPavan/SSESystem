from StudentDataCenter import addStudent,modifyStudent,deleteStudent,showStudent,getStudentById,getStudentByStudentName,getStudentId
from StudentSubjectRelation import getRelationshipsByStudentId   
###########################################################################
    
def isValidStudentName(studentName):
    for letter in studentName:
        if letter.isdigit():
            print("Student name should not have numbers included")
            return False;
        if letter.isspace():
            print("Student name should not have white spaces")
            return False;
    return True;
    
    
def isValidDOB(date):
    "when a date is given in DD/MM/YYYY format as a string, checks whether the date is valid."
    "If date is valid return True. Else False"
    import datetime
    if len(date)!=len("DD/MM/YYYY"):
        print("DOB should match with DD/MM/YYYY format")
        return False;
    date=date.strip().split("/",2)
    for i in date:
        if not(i.isdigit()):
            print("DOB should match with DD/MM/YYYY format")
            return False;
    year=int(date[2])
    month=int(date[1])
    day=int(date[0])
    try:
        datetime.datetime(year,month,day)
        return True;
    except ValueError:
        print("DOB should match with DD/MM/YYYY format")
        return False;


        
###########################################################################
studentIdSeq=0
def addStudentHandler(studentName,dob):
    if ((isValidDOB(dob))and(isValidStudentName(studentName))):
        global studentIdSeq
        studentIdSeq+=1
        isStudentAdded=addStudent(studentIdSeq,studentName,dob)
        if isStudentAdded:
            print("Student added correctly")
    return;

def modifyStudentHandler(oldName,newName,dob):
    if ( (isValidDOB(dob)) and (isValidStudentName(oldName)) and (isValidStudentName(newName))):
        if getStudentByStudentName(oldName)==[]:
            print("Subject with " ,oldName ," does not exist")
        else:
            if getStudentByStudentName(newName)!=[]:
                print("Two students can not have same name")
            else:
                stuId=getStudentId(oldName)
                isStudentModified=modifyStudent(stuId,newName,dob)
                if (isStudentModified):
                    print("Student modified correctly")       
    return;
        

def removeStudentHandler(studentName):
    if (isValidStudentName(studentName)):
        if getStudentByStudentName(studentName)==[]:
            print("Student with",studentName,"does not exist")
            return;
    studentId=getStudentId(studentName)       
    relations=getRelationshipsByStudentId(studentId)
    if relations==[]:
        isDeleted=deleteStudent(studentId)
        if isDeleted:
            print("subject deleted correctly")
    else:
        print("Can not be deleted. Student has scores stored in the system")
    return;        


def helpStudentHandler(student):
    if (isValidStudentName(student)):
        if getStudentByStudentName(student)==[]:
            print("Student with ",student," does not exist")
        else:
            showStudent(student)    
    return;


    
