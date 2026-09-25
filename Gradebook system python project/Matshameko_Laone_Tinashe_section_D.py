
def get_grade(name_of_subject):
    while True:   # intentionally made to run forever no exit condition
        try: #skips to except when entering anything that is not a number
            grade=float(input(f"Enter {name_of_subject} grade:"))
            if  grade >= 0 and grade <= 100: #checks if marks are between 0 and 100 and stops loop if it is so
               return(grade)
            else:
                print("invalid grade. Enter a grade between 0 and 100!")
        except ValueError:
            print("Please enter a number!")
    return()

def add_student():
    while True:
        
        try:
        
            new_students_to_add = int (input("enter the number of new students:"))
            break
        except ValueError:
            print("Please enter a number!")
    for i in range(new_students_to_add):
        
            while True:
                
                name = input("enter name:")
                if all(c.isalpha() for c in name):  #checks all characters in the name if are they words and if "all" are true it returns true if all characters are words
                    break
                else:
                    print("Invalid name!. Use only letters!")
            
            
            maths_grade = get_grade("Maths")
                    
           
            maths.append(maths_grade)
           
            
            english_grade = get_grade("English")
            
                
                
                
            english.append(english_grade)
           
            
            science_grade = get_grade("Science")
            
            science.append(science_grade)
            
            student=(name , maths_grade , english_grade, science_grade) # 
            students.append(student) #
            
            #student={name : students[1:4]}
            studentss[name]=  {"Maths": maths_grade ,"English":english_grade ,"Science" : science_grade} #add each student to main dictionary instead of replacing it for the values only
            print(studentss)

    
    return ()


def remove_student():
    while True:
        
        try:
        
            students_to_remove = int (input("enter the number of students you want to remove:"))
            break
        except ValueError:
            print("Please enter a number!")

    for i in range(students_to_remove):
            
        while True:
            
            name = input("enter name:")  # first find name 
            if all(c.isalpha() for c in name):  #checks all characters in the name if are they words and if "all" are true it returns true if all characters are words
                break
            else:
                print("Inavalid name!. Use only letters!") 
    
        if name in studentss:#check if name exists in dictionary
            remove_student=studentss.pop(name) #creates new dictionary that holds deleted name's grades
            maths.remove(remove_student["Maths"])
            english.remove(remove_student["English"])  #locates the grade of the deleted name in remove_student dictionary and deletes it from the neccesary subject tuple
            science.remove(remove_student["Science"])
            print(name,"has been deleted successfully!")
            print("New student list",studentss)
        else:
            print("student not found")
    
    
    return()
def update_student():
    
    while True:
        
        try:
        
            students_to_update = int (input("enter the number of students you want to update thier grades:"))
            break
        except ValueError:
            print("Please enter a number!")
    
    for i in range(students_to_update):
            
        while True:
            
            name = input("enter name:")  # first find name 
            if all(c.isalpha() for c in name):  #checks all characters in the name if are they words and if "all" are true it returns true if all characters are words
                break
            else:
                print("Inavalid name!. Use only letters!") 
    
    
        if name in studentss:#check if name exists in dictionary
            grades=studentss[name] #get the grades of name choosen
        
            print("For the following question pick either 'yes' or 'no' ONLY")
            update_maths=input("Do you want to update the maths grade?(yes/no):")
            if update_maths=="yes":
                
                
                
                new_maths_grade = get_grade("Maths")
                          
                    
                    
                    
                    
                    
                old_maths= grades["Maths"]
                maths.remove(old_maths) # removing old maths value 
                maths.append(new_maths_grade)
                grades["Maths"]=new_maths_grade #value for maths key is now changed        
                print("Maths grade successfully updated!")
                print(studentss)
                
            print("For the following question pick either 'yes' or 'no' ONLY")
            update_english=input("Do you want to update the english grade?(yes/no):")
            if update_english=="yes":
                
                
                new_english_grade = get_grade("English")
                      
                    
                    
                    
                    
                    
                old_english=grades["English"]
                english.remove(old_english)
                english.append(new_english_grade)
                grades["English"]=new_english_grade
                print("English grade changed successfully!")
                print(studentss)
       
        
            print("For the following question pick either 'yes' or 'no' ONLY")
            update_science=input("Do you want to update the science grade?(yes/no):")
            if update_science=="yes":
                
                
               
                new_science_grade = get_grade("Science")
                             
                    
                    
                    
                old_science=grades["Science"]
                science.remove(old_science)
                science.append(new_science_grade)
                grades["Science"]=new_science_grade
            
                print("science grade changed succussfully!")
                print(studentss)
            
        
        else:
            print("student not found")
    
    return()
def enter_student():
    while True:
        
        try:
        
            no_of_students_in_class = int (input("enter the number of students in class:"))
            break
        except ValueError:
            print("Please enter a number!")
        
    
    for i in range(no_of_students_in_class):
            
            while True:
                
                name = input("enter name:")  # first find name 
                if all(c.isalpha() for c in name):  #checks all characters in the name if are they words and if "all" are true it returns true if all characters are words
                    break
                else:
                    print("Inavalid name!. Use only letters!") 
        
            
            maths_grade = get_grade("Maths")
                
            
           
            maths.append(maths_grade)
            
            english_grade = get_grade("English")
                    
            
                
                
                
            english.append(english_grade)
            
            science_grade = get_grade("Science")
                    
            
                
                
                
                
            science.append(science_grade)
            student=(name , maths_grade , english_grade, science_grade) # does this get replaced?
            students.append(student) #does this get replaced
            
            #student={name : students[1:4]}
            studentss[name]=  {"Maths": maths_grade ,"English":english_grade ,"Science" : science_grade} #add each student to main dictionary instead of replacing it for the values only
            print(studentss)
            
    return()
def subject_summary(): 
    while True:
        
        print("For the following question pick either 'yes' or 'no' ONLY")
        view_subject=input("Do you want to view the results for a specific subject?(yes/no):").lower()
        if view_subject=="yes":
            subject_choice=input("Choose one out of the following(Maths,English,Science):") .capitalize()
            if subject_choice=="Maths":

                print("Maths Grades:",Maths)
                break
            elif subject_choice=="English":
                print("English Grades:",English)
                break
            elif subject_choice=="Science":
                print("Science Grades:",Science)
                break
            else:
                print("Invalid subject name")
        elif view_subject=="no":
            break
        else:
            print("You did not choose a specific subject")
    return()

def student_search():
    
    while True:
        
        name = input("enter name:")  # first find name 
        if all(c.isalpha() for c in name):  #checks all characters in the name if are they words and if "all" are true it returns true if all characters are words
            break
        else:
            print("Inavalid name!. Use only letters!") 
 
    
    if name in studentss:#check if name exists in dictionary
        grades=studentss.get(name) # just retrieved values under key /specific name
        average = sum(grades.values())/len(grades)
        print(name,"'s Grades:",grades,"Average",round(average,2),"%")
    else:
        print("student not found")
        
    return()
def grade_max_and_min():
    max_maths=ask_yes_or_no("Do you want to see the highest maths grade?(yes/no):")
    if max_maths=="yes":
       print("The highest grade in maths is",max(maths),"%") 
    min_maths=ask_yes_or_no("Do you want to see the lowest maths grade?(yes/no):")
    if min_maths=="yes":
       print("The lowest grade in maths is",min(maths),"%") 
    max_english=ask_yes_or_no("Do you want to see the highest english grade?(yes/no):")
    if max_english=="yes":
        print("The highest grade in english is",max(english),"%")
    min_english=ask_yes_or_no("Do you want to see the lowest english grade?(yes/no):")
    if min_english=="yes":
        print("The lowest grade in english is",min(english),"%")
    max_science=ask_yes_or_no("Do you want to see the highest science grade?(yes/no):")
    if max_science=="yes":
        print("The highest grade in science is",max(science),"%")
    min_science=ask_yes_or_no("Do you want to see the lowest science grade?(yes/no):")
    if min_science=="yes":
        print("The lowest grade in science is",min(science),"%")
    
    return()

def run():
    print("Entry of student records")
    print("For the following question pick either 'yes' or 'no' ONLY")
    desire_to_enter=ask_yes_or_no("Do you want to enter student records ?(yes/no):")
    if desire_to_enter=="yes":
        enter_student()
    else:
        print("There is no desire to enter any student records")
        
    enter_again=ask_yes_or_no("Do you want to enter more student records  ?(yes/no):") #incase they want to enter more that they were not able to enter the first time
    if enter_again=="yes":
         enter_student()
         
    


    print("Possibilty for addition of students")
    print("For the following question pick either 'yes' or 'no' ONLY")
    desire_to_add=ask_yes_or_no("Do you want to add  new students ?(yes/no):")
    if desire_to_add =="yes":
        add_student()
    else:
        print("There is no desire to add any students")
    
    add_again=ask_yes_or_no("Do you want to add  more new students ?(yes/no):")
    if add_again=="yes":
        add_student()
        
        

        
    print("Possibilty for removing students")
    print("For the following question pick either 'yes' or 'no' ONLY")
    desire_to_remove=ask_yes_or_no("Do you want to remove students from the system ?(yes/no):")
    if desire_to_remove== "yes":
        remove_student()
    else:
        print("there is no desire to remove any students")
        
    remove_again=ask_yes_or_no("Do you want to remove more students from the system ?(yes/no):")
    if remove_again=="yes":
        remove_student()
        
        
    print("Possibilty for updating existing grades")
    print("For the following question pick either 'yes' or 'no' ONLY")
    desire_to_update=ask_yes_or_no("Do you want to update existing grades ?(yes/no):")
    if desire_to_update== "yes":
        update_student()
        
    else:
        print("There is no desire to update existing grades")
    
    update_again=ask_yes_or_no("Do you want to update more existing grades ?(yes/no):")
    if update_again=="yes":
        update_student()
    
    
    
     


           



    print("Grade Max and Min")
    print("For the following question pick either 'yes' or 'no' ONLY")
    desire_to_view_max_and_min=ask_yes_or_no("Do you want to view the highest and lowest grades across all the subjects ?(yes/no):") 
    if desire_to_view_max_and_min== "yes":
        grade_max_and_min()
        
    else:
        print("There is no desire to view the highest and lowest grades across all the subjects")
    
    max_min_again=ask_yes_or_no("Do you want to view the highest and lowest grades across all the subjects again ?(yes/no):")
    if max_min_again=="yes":
        grade_max_and_min()
    
    
    print("Subject Summary") 
    print("For the following question pick either 'yes' or 'no' ONLY")
    desire_to_view_summary=ask_yes_or_no("Do you want to view the subject summary?(yes/no):")
    if desire_to_view_summary== "yes":
        subject_summary()
        
    else:
        print("There is no desire to view the subject summary")
    view_again=ask_yes_or_no("Do you want to view the subject summary again?(yes/no):")
    if view_again=="yes":
        subject_summary()
    
    print("Student search")
    print("For the following question pick either 'yes' or 'no' ONLY")
    
    desire_to_search=ask_yes_or_no("Do you want to search for a specific student via name?(yes/no):")
    if desire_to_search == "yes":
        student_search()
    
    else:
        print("Not searching")
    search_again=ask_yes_or_no("Do you want to search for a specific student via name again?(yes/no):")
    if search_again=="yes":
        student_search()
        

    return()
def ask_yes_or_no(prompt): #prompt is placeholder for actual question to promote reusability abd not typing each question for different function
    while True:
        answer=input(prompt).strip().lower()  #strip removes spaces in words
        if answer in ["yes","no"]:
            
            return (answer)
        print("Please answer 'yes' or 'no' only!")

students=[]  

maths=[]
english=[]
science=[]
Maths={"Maths":maths}
English={"English": english}
Science={"Science": science}
studentss={} # both the name and value as another dictionary

run()  # calling the function that has all other function inside

