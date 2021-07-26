#24.02.2021
#ID-P4 (Pavan)

invalidSyntaxMesg = "Invalid syntax press ‘help –‘ to check valid command list "

def beginEndScreen(displayMsg):
    #displays a message surrounded by stars
    for i in range(2):
        print("*"*95)
    print(displayMsg.center(95,"*"))
    for i in range(2):
        print("*"*95)
    return

isNameValid=lambda name:name.isalpha()  #check on name validity

def checkErrorInName(name):
    #display the relevant errors in the name
    if " " in name:
        print("Student name should not have white spaces")
        name=name.replace(" ","")
    if not(name.isalpha()):
        print("Student name should not have numbers included")
    return

isMarkValid=lambda mark:(mark.isdigit() and (len(mark)==2 or mark=='100' or mark=='0')) #check on mark validity

def checkErrorInMark(mark):
    #display the relevant errors in the mark
    if (mark[1:].find("-")>0 or not(mark.isdigit())): 
        print("Student mark should be a number")
        return
    if int(mark)<0:
        print("Student mark should be greater than zero")
    elif int(mark)>100:
        print("Student mark should be less or equal to 100")
    return

def addStudent(name,studentInfo):
    #checks name validity, if name not in student dictionary, name gets added,return updated student dictionary
    name=name.rstrip() #to remove accidental spaces's at the end of the name
    if not(isNameValid(name)):
        checkErrorInName(name)
    else:
        if name not in studentInfo:
            studentInfo[name]=None
        else:
            print("Two students can not have same name")
    return studentInfo
                
def removeStudent(name,studentInfo):
    #checks name validity, if name in dictionary, name gets removed,return updated student dictionary
    name=name.rstrip() #to remove accidental spaces's at the end of the name
    if not(isNameValid(name)):
        checkErrorInName(name)
    else:
        if name not in studentInfo:
            print("Student "+name+" does not exist")
        else:
            del studentInfo[name]
    return studentInfo

def addMark(name,mark,studentInfo):
    #checks name validity, checks mark validity
    #if name and/or mark not in student dictionary, mark gets added,return updated student dictionary
    name=name.rstrip() #to remove accidental spaces's at the end of the name
    if not(isNameValid(name)):
        checkErrorInName(name)
        return studentInfo
    mark=mark.lstrip("0") #to remove accidental  zero's from the front of the mark
    if not(isMarkValid(mark)):
        checkErrorInMark(mark)
    else:
        if studentInfo.get(name)!= None:
            print("Student "+name+" already has a score")
        else:
            studentInfo[name]=mark
    return studentInfo
    
def removeMark(name,studentInfo):
    #removes the student's mark from the student dictionary
    name=name.rstrip() #to remove accidental spaces's at the end of the name
    if not(isNameValid(name)):
        checkErrorInName(name)
        return studentInfo
    if name not in studentInfo:
        print("Student "+name+" does not exist")
        return studentInfo
    mark=studentInfo[name]
    if mark==None:
        print("Student "+name+" has no score to clear")
        return studentInfo
    if not(isMarkValid(mark)):
        checkErrorInMark(mark)
    else:
        studentInfo[name]=None
    return studentInfo

def findMaxLengthOfNames(studentInfo):
    #finds the suitable length for the Name column
    names=list(studentInfo.keys())
    for i in range(len(names)):
        names[i]=len(names[i])
    return max(names)
    
def showSummary(studentInfo):
    #prints detailed summary of students Name and Score
    length=len("Name")
    if len(studentInfo)>0:
        nameLength=findMaxLengthOfNames(studentInfo)
        if nameLength>length:
            length=nameLength   
    totalLength=length+7+len("Score")
    print("="*totalLength)
    print("| "+"Name".center(length," ")+" | Score |")
    print("="*totalLength)
    for student in studentInfo:
        score=studentInfo[student]
        if score==None:
            score=""
        print("|"+student.center(length+2," ")+"|"+score.center(7," ")+"|")
    return

def helpUser():
    #Show syntax, operation description, details of each error message of all the available commands.
    print("List of commands: \n")
    #add_student
    print("1. add_student<student_name> - Keep a note about the student name until application terminates. Name is case sensitive")
    print("   Error messages:")
    print("\tTwo students can not have same name")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    #remove_student
    print("2. add_mark <student_name> <student_score> - remove a student name from application")
    print("   Error messages:")
    print("\tStudent with <student_name> does not exist")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    #add_mark
    print("3. remove_student <student_name> - Keep a note about the student’s score until application terminates. Once score added, it can not be modified")
    print("   Error messages:")
    print("\tStudent <student_name> already has a score")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tStudent mark should be a number")
    print("\tStudent mark should be greater than zero")
    print("\tStudent mark should be less or equal to 100")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    #remove_mark
    print("4. remove_mark <student_name> - Clear student’s score. After clearing score , user can add it again.")
    print("   Error messages:")
    print("\tStudent with <student_name> does not exist")
    print("\tStudent <student_name> has no score to clear")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    #show_summary
    print("5. show_summary - Show all students and their marks in a printed table.")
    print("   Error messages:")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    #exit
    print("6. exit - Exit the application showing following message.")
    print("   Error messages:")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    return
    
#main
studentDict={}
beginEndScreen("Welcome to Smart student evaluation System")
while(True):
    syntax=input().split(" ",1)
    
    if syntax[0]=="add_student":
        if len(syntax)==2:
            addStudent(syntax[1],studentDict)
        else:
            print(invalidSyntaxMesg)
            
    elif syntax[0]=="remove_student":
        if len(syntax)==2:
            removeStudent(syntax[1],studentDict)
        else:
            print(invalidSyntaxMesg)
            
    elif syntax[0]=="add_mark":
        if len(syntax)==2:
            syntax.extend(syntax.pop(1).rstrip().rsplit(" ",1))  #rstrip is to remove accidental spaces at the end of the command. #rsplit is seperate the name and mark.
            if len(syntax)==3:                              
                addMark(syntax[1],syntax[2],studentDict)
            else:                                                           
                print(invalidSyntaxMesg)            
        else:
            print(invalidSyntaxMesg)
            
    elif syntax[0]=="remove_mark":
        if len(syntax)==2:
            removeMark(syntax[1],studentDict)
        else:
            print(invalidSyntaxMesg)
            
    elif syntax[0]=="show_summary":
        showSummary(studentDict)
        print("")
        
    elif syntax[0]=="help":
        helpUser()
        
    elif syntax[0]=="exit":
        beginEndScreen("Good Bye !! Have a nice day")
        break
    
    else:
        print(invalidSyntaxMesg)

    
    

