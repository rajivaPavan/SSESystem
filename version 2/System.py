from StudentDataHandler import addStudentHandler,modifyStudentHandler,removeStudentHandler,helpStudentHandler
from SubjectDataHandler import addSubjectHandler,modifySubjectHandler,removeSubjectHandler,showSubjectHandler
from StudentSubjectRelationHandler import addMarkHandler,modifyMarkHandler,removeMarkHandler,showMarkHandler,showAllMarksHandler,showAllStudentsHandler
from MainUserCommands import helpUser

invalidSyntaxMesg="Invalid syntax press \"help\" to check valid command list "

def addElementsToList(mainList,index,elementList):
    """adds elements from a list to a another list at the specified index."""
    "eg: addElementsToList([a,e,u],2,[i,o])"
    "   return---->[a,e,i,o,u]"
    for element in elementList:
        mainList.insert(index,element)
        index+=1
    return mainList;

def getSyntaxIntoList(syntax,lenOfSyntax):
    """return the  in the syntax in the form of a list when length of syntax is specified"""
    "if incase length is not properly satisfied print the invalidsyntaxMessage and return the incomplete syntaxList anyway"
    currentLength=2
    while len(syntax)!=lenOfSyntax:
        if len(syntax)==currentLength:
            syntax=addElementsToList(syntax,1,syntax.pop(1).strip().rsplit(" ",1)) 
            currentLength+=1
        else:
            print(invalidSyntaxMesg)
            break
    return syntax;

def beginEndScreen(displayMsg):
    """displays a message surrounded by stars"""
    for i in range(2):
        print("*"*95)
    print(displayMsg.center(95,"*"))
    for i in range(2):
        print("*"*95)
    return;

#main
beginEndScreen("Welcome to Smart student evaluation System")

while True:
    syntax=input().split(" ",1) #seperate out the main command
    
    if syntax[0]=="add_student": #add_student <student_name> <DOB>
        syntax=getSyntaxIntoList(syntax,3)
        if len(syntax)==3:                              
            addStudentHandler(syntax[1],syntax[2])

    elif syntax[0]=="modify_student": #modify_student <old_student_name> <new_student_name> <DOB>
        syntax=getSyntaxIntoList(syntax,4)
        if len(syntax)==4:
            modifyStudentHandler(syntax[1],syntax[2],syntax[3])
    
    elif syntax[0]=="remove_student": #remove_student <student_name>
        syntax=getSyntaxIntoList(syntax,2)
        if len(syntax)==2:
            removeStudentHandler(syntax[1])
            
    elif syntax[0]=="help_student": #help_student <student_name>
        syntax=getSyntaxIntoList(syntax,2)
        if len(syntax)==2:
            helpStudentHandler(syntax[1])

    elif syntax[0]=="add_subject": #add_subject <name> <stream>
        syntax=getSyntaxIntoList(syntax,3)
        if len(syntax)==3:                            
            addSubjectHandler(syntax[1],syntax[2])


    elif syntax[0]=="modify_subject":#modify_subject <old_ subject _name> <new_ subject _name> <stream>
        syntax=getSyntaxIntoList(syntax,4)
        if len(syntax)==4:                          
            modifySubjectHandler(syntax[1],syntax[2],syntax[3])

    elif syntax[0]=="remove_subject": #remove_subject <subject_name>
        syntax=getSyntaxIntoList(syntax,2)
        if len(syntax)==2:
            removeSubjectHandler(syntax[1])

    elif syntax[0]=="show_subject": #show_subject <subject_name>
        syntax=getSyntaxIntoList(syntax,2)
        if len(syntax)==2:
            showSubjectHandler(syntax[1])

    elif syntax[0]=="add_mark": #add_mark <student_name> <subject_name> <score>
        syntax=getSyntaxIntoList(syntax,4)
        if len(syntax)==4:                             
            addMarkHandler(syntax[1],syntax[2],syntax[3])


    elif syntax[0]=="modify_mark": #modify_mark <old_student_name> <old_subject_name> <new_student_name> <new_subject_name> <score>
        syntax=getSyntaxIntoList(syntax,6)
        if len(syntax)==6:                            
            modifyMarkHandler(syntax[1],syntax[2],syntax[3],syntax[4],syntax[5])     

    elif syntax[0]=="remove_mark": #remove_mark <student_name> <subject_name>
        syntax=getSyntaxIntoList(syntax,3)
        if len(syntax)==3:
            removeMarkHandler(syntax[1],syntax[2])
            
    elif syntax[0]=="show_mark": #show_mark <student_name> <subject_name>
        syntax=getSyntaxIntoList(syntax,3)
        if len(syntax)==3:
            showMarkHandler(syntax[1],syntax[2])

    elif syntax[0]=="show_all_mark": #show_all_marks <student_name>
        syntax=getSyntaxIntoList(syntax,2)
        if len(syntax)==2:
            showAllMarksHandler(syntax[1])

    elif syntax[0]=="show_all_students": #show_all_students <subject_name>
        syntax=getSyntaxIntoList(syntax,2)
        if len(syntax)==2:
            showAllStudentsHandler(syntax[1])
            
    elif syntax[0]=="help": #help
        helpUser()
        
    elif syntax[0]=="exit": #exit
        beginEndScreen("Good Bye !! Have a nice day")
        break #End of the program
    
    else:
        print(invalidSyntaxMesg)
