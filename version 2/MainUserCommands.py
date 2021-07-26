def helpUser():
    #Show syntax, operation description, details of each error message of all the available commands.
    print("List of commands: \n")
    #add_student
    print("1. add_student <student_name> <DOB> - keep a note about the student name and Date of Birth until application terminates. Two students from same name can not exist. Student name should be \nsingle word with only letters(case-sentitive).")
    print("   Error messages:")
    print("\tTwo students can not have same name")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tDOB should match with DD/MM/YYYY format")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    
    #modify_student
    print("2. modify_student <old_student_name> <new_student_name> <DOB> - modify student DOB and name.")
    print("   Error messages:")
    print("\tTwo students can not have same name")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tStudent with <student_name> does not exist")
    print("\tDOB should match with DD/MM/YYYY format")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")


    #remove_student
    print("3. remove_student <student_name> - remove a student from application. System should not allow to remove student if there is scores stored for this student. ")
    print("   Error messages:")
    print("\tStudent with <student_name> does not exist")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tCan not be deleted. Student has scores stored in the system")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #help_student
    print("4. help_student <student_name> - show all details of the student.")
    print("   Error messages:")
    print("\tStudent with <student_name> does not exist")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    
    #add_subject

    print("5. add_subject <name> <stream> - add subject name and stream (O/L or A/L) into the system. Subject is a single word with only letters(case-sencitive). ")
    print("   Error messages:")
    print("\tTwo subjects can not have same name")
    print("\tSubject name have should have no white spaces")
    print("\tSubject name should not have numbers included")
    print("\tStream should be either A/L or O/L")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #modify_subject

    print("6. modify_subject <old_ subject _name> <new_ subject _name> <stream> - modify subject stream and name.")
    print("   Error messages:")
    print("\tTwo subjects can not have same name")
    print("\tSubject name have should have no white spaces")
    print("\tSubject name should not have numbers included")
    print("\tSubject with <subject_name> does not exist")
    print("\tStream should be either A/L or O/L")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #remove_subject

    print("7. remove_subject <subject_name> - remove a subject from application. System should not allow to remove subject if there is scores stored for this subject.")
    print("   Error messages:")
    print("\tSubject with <subject_name> does not exist")
    print("\tCan not be deleted. Subject has scores stored in the system")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #show_subject

    print("8. show_subject <subject_name> - show all details of the subject.")
    print("   Error messages:")
    print("\tSubject with <subject_name> does not exist")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    
    #add_mark
    print("9. add_mark <student_name> <subject_name> <score> - Keep a note about the student’s score until application terminates.")
    print("   Error messages:")
    print("\tStudent with <student_name> does not exist")
    print("\tSubject with <subject_name> does not exist")
    print("\tThis student has marks for this subject already")
    print("\tStudent mark should be a number")
    print("\tStudent mark should be greater than zero")
    print("\tStudent mark should be less or equal to 100")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #modify_mark
    print("10. modify_mark <old_student_name> <old_subject_name> <new_student_name> <new_subject_name> <score> - Update student name, subject name and score.")
    print("   Error messages:")
    print("\tStudent with <student_name> does not exist")
    print("\tSubject with <subject_name> does not exist")
    print("\tThis student has no marks for this subject yet")
    print("\tStudent mark should be a number")
    print("\tStudent mark should be greater than zero")
    print("\tStudent mark should be less or equal to 100")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")


    #remove_mark
    print("11. remove_mark <student_name> <subject_name> - Clear student’s score. After clearing score , user can add it again.")
    print("   Error messages:")
    print("\tStudent <student_name> has no score to clear")
    print("\tStudent name have should have no white spaces")
    print("\tStudent name should not have numbers included")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    
    #show_mark
    print("12. show_mark <student_name> <subject_name> - show all details of the score.")
    print("   Error messages:")
    print("\tSubject with <subject_name> does not exist\n")
    print("\tStudent with <student_name> does not exist\n")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #show_all_marks

    print("13. show_all_marks <student_name> - Show all marks related to the student as a table.")
    print("   Error messages:")
    print("\tStudent with <student_name> does not exist\n")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #show_all_students
    print("14. show_all_students <subject_name> - Show all students related to the subject as a table.")
    print("   Error messages:")
    print("\tSubject with <subject_name> does not exist\n")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #help
    print("15. help - Show syntax, operation description, details of each error message of all the available commands.")
    print("   Error messages:")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")

    #exit
    print("16. exit - Exit the application showing following message.")
    print("   Error messages:")
    print("\tInvalid syntax press ‘help –‘ to check valid command list\n")
    return;
