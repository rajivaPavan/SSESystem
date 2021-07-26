from StudentDataCenter import addStudent,getStudentById,modifyStudent,getStudentByName,deleteStudent
from SubjectDataCenter import getSubjectBySubjectName,getSubjectById,deleteSubject,modifySubject,addSubject
from StudentSubjectRelation import addStudentSubjectRelation,modifyStudentSubjectRelation,deleteStudentSubjectRelation,getRelationshipsBySubjectId,getRelationshipsByStudentId

#add a subject into data center
studentIncrementer=1
#todo write code 
addStudent(studentIncrementer,"Kasun","23/08/1993")
#todo write code 
studentIncrementer+=1
addStudent(studentIncrementer,"Nimal","24/08/1993")

studentEntity=getStudentById(1)
print("Student id", studentEntity["id"])
print("Student Name", studentEntity["name"])
print("Student DOB", studentEntity["dob"])

#modify existing student in data center
modifyStudent(1,"KasunLakMal","23/08/1993")

studentEntity=getStudentById(1)
print("Student id", studentEntity["id"])
print("Student Name", studentEntity["name"])
print("Student DOB", studentEntity["dob"])


studentEntityByNameList=getStudentByName("KasunLakMal")
for sa in studentEntityByNameList:
    print("Student id", sa["id"])
    print("Student Name", sa["name"])
    print("Student DOB", sa["dob"])

#delete a student
deleteStudent(1)
studentEntity=getStudentById(1)
if studentEntity is None:
    print("Student deletion is successful")
else:
    print("Student deletion is unsuccessful")

#######################################################
#add a subject into data center
addSubject(1,"Sinhala","A/L")

subjectEntity=getSubjectById(1)
print("Subject id", subjectEntity["id"])
print("Subject Name", subjectEntity["subjectName"])
print("Subject DOB", subjectEntity["stream"])

#modify existing subject in data center
modifySubject(1,"Buddhism","O/L")

subjectEntity=getSubjectById(1)
print("Subject id", subjectEntity["id"])
print("Subject Name", subjectEntity["subjectName"])
print("Subject DOB", subjectEntity["stream"])


subjectEntityByNameList=getSubjectBySubjectName("Buddhism")
for s in subjectEntityByNameList:
    print("Subject id", s["id"])
    print("Subject Name", s["subjectName"])
    print("Subject DOB", s["stream"])

#delete a subject
deleteSubject(1)
subjectEntity=getSubjectById(1)
if subjectEntity is None:
    print("Subject deletion is successful")
else:
    print("Subject deletion is unsuccessful")

###################################################
#add a relationship
addStudent(111,"Kasun","23/08/1993")
addStudent(567,"Nimall","23/08/1993")
addSubject(12,"Sinhala","A/L")
addStudentSubjectRelation(1,111,12,98)

#modify existing subject in data center
modifyStudentSubjectRelation(1, 567, 12, 56)

relationships=getRelationshipsBySubjectId(12)
for r in relationships:
    print("Relationship id", r["id"])
    print("Relationship studentId", r["studentId"])
    print("Relationship subjectId", r["subjectId"])
    print("Relationship score", r["score"])

relationships=getRelationshipsByStudentId(111)
for r in relationships:
    print("Relationship id", r["id"])
    print("Relationship studentId", r["studentId"])
    print("Relationship subjectId", r["subjectId"])
    print("Relationship score", r["score"])
