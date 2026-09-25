
def add_student():
    new_students_to_add = int (input("enter the number of new students:"))
    for i in range(new_students_to_add):
            
            name = input("enter name:")
            maths_grade = float(input("enter maths grade:"))
            
            while maths_grade < 0 or maths_grade > 100:
                print("invalid grade")
                maths_grade = float(input("enter maths grade:"))
            maths.append(maths_grade)
            english_grade = float(input("enter english grade:"))
            
            while english_grade < 0 or english_grade > 100:
                print("invalid grade")
                english_grade = float(input("enter english grade:"))
            english.append(english_grade)
            science_grade = float(input("enter science grade:"))
            
            while science_grade < 0 or science_grade > 100:
                print("invalid grade")
                science_grade = float(input("enter science grade:"))
            science.append(science_grade)
            student=(name , maths_grade , english_grade, science_grade) # does this get replaced?
            students.append(student) #does this get replaced
            
            #student={name : students[1:4]}
            studentss[name]=  {"Maths": maths_grade ,"English":english_grade ,"Science" : science_grade} #add each student to main dictionary instead of replacing it for the values only
            print(studentss)

    
    return ()
def remove_student():
    
    name= input("Enter student name:") # first find name 
    
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
    name= input("Enter student name:") # first find name 
    
    if name in studentss:#check if name exists in dictionary
        grades=studentss[name] #get the grades of name choosen
        
        
        update_maths=input("Do you want to update the maths grade?(yes/no):")
        if update_maths=="yes":
            new_maths_grade=  float(input("enter maths grade:"))
            
            while new_maths_grade < 0 or new_maths_grade > 100:
                print("invalid grade")
                new_maths_grade = float(input("enter maths grade:"))
            old_maths= grades["Maths"]
            maths.remove(old_maths) # removing old maths value 
            maths.append(new_maths_grade)
            grades["Maths"]=new_maths_grade #value for maths key is now changed        
            print("Maths grade successfully updated!")
            print(studentss)
         
        update_english=input("Do you want to update the english grade?(yes/no):")
        if update_english=="yes":
            new_english_grade= float(input("enter english grade:"))
                 
            while new_english_grade < 0 or new_english_grade > 100:
                print("invalid grade")
                new_english_grade = float(input("enter english grade:"))
            old_english=grades["English"]
            english.remove(old_english)
            english.append(new_english_grade)
            grades["English"]=new_english_grade
            print("English grade changed successfully!")
            print(studentss)
       
        
        update_science=input("Do you want to update the science grade?(yes/no):")
        if update_science=="yes":
            new_science_grade=float(input("enter science grade:"))
                
            while new_science_grade < 0 or new_science_grade > 100:
                print("invalid grade")
                new_science_grade = float(input("enter science grade:"))
            old_science=grades["Science"]
            science.remove(old_science)
            science.append(new_science_grade)
            grades["Science"]=new_science_grade
            
            print("science grade changed succussfully!")
            print(studentss)
            
        
    else:
        print("student not found")
    
    return()
        
no_of_students_in_class = int (input("enter the number of students in class:"))


students=[]  

maths=[]
english=[]
science=[]
Maths={"Maths":maths}
English={"English": english}
Science={"Science": science}
studentss={} # both the name and value as another dictionary
for i in range(no_of_students_in_class):
        
        name = input("enter name:")
        maths_grade = float(input("enter maths grade:"))
        
        while maths_grade < 0 or maths_grade > 100:
            print("invalid grade")
            maths_grade = float(input("enter maths grade:"))
        maths.append(maths_grade)
        english_grade = float(input("enter english grade:"))
        
        while english_grade < 0 or english_grade > 100:
            print("invalid grade")
            english_grade = float(input("enter english grade:"))
        english.append(english_grade)
        science_grade = float(input("enter science grade:"))
        
        while science_grade < 0 or science_grade > 100:
            print("invalid grade")
            science_grade = float(input("enter science grade:"))
        science.append(science_grade)
        student=(name , maths_grade , english_grade, science_grade) # does this get replaced?
        students.append(student) #does this get replaced
        
        #student={name : students[1:4]}
        studentss[name]=  {"Maths": maths_grade ,"English":english_grade ,"Science" : science_grade} #add each student to main dictionary instead of replacing it for the values only
        print(studentss)

#print("Student Summary") # Does the student summary go away

#for name, maths_grade, english_grade, science_grade in students:
#    average = (maths_grade + english_grade + science_grade)/3
    
#    print("Name:", name, "Maths grade=" , maths_grade,"%", "English grade=" , english_grade,"%", "Science grade=" , science_grade,"%" ,"Average =",round( average,2),"%")
#   for all these addition,updating and remaoval should i add while loops so that they can do this for multiple students without restarting the entire program again
print("Possibilty for addition of students")
desire_to_add=input("Do you want to add  new students ?(yes/no):").lower()
if desire_to_add =="yes":
    add_student()
else:
    print("There is no desire to add any students")
    

    
print("Possibilty for removing students")
desire_to_remove=input("Do you want to remove students from the system ?(yes/no):").lower()
if desire_to_remove== "yes":
    remove_student()
else:
    print("there is no desire to remove any students")
    
print("Possibilty for updating existing grades")
desire_to_update=input("Do you want to update existing grades ?(yes/no):").lower()  
if desire_to_update== "yes":
    update_student()
    
else:
    print("There is no desire to update existing grades")
    

    



print("Grade Max and Min")
print("The highest grade in maths is",max(maths),"%")
print("The lowest grade in maths is",min(maths),"%")
print("The highest grade in english is",max(english),"%")
print("The lowest grade in english is",min(english),"%")
print("The highest grade in science is",max(science),"%")
print("The lowest grade in science is",min(science),"%")

print("Subject Summary") 
view_subject=input("Do you want to view the results for a specific subject?(yes/no):").lower()
if view_subject=="yes":
    subject_choice=input("Choose one out of the following(Maths,English,Science):")
    if subject_choice=="Maths":

        print("Maths Grades:",Maths)
    elif subject_choice=="English":
        print("English Grades:",English)
    elif subject_choice=="Science":
        print("Science Grades:",Science)
    else:
        print("Invalid subject name")
else:
    print("You did not choose a specific subject")
  

print("Student search")
desire_to_search=input("Do you want to search for a specific student via name?(yes/no):").lower()
if desire_to_search == "yes":

    name= input("Enter student name:") # while loop to enter name until one is in dictionary?
    
    if name in studentss:#check if name exists in dictionary
        grades=studentss.get(name) # just retrieved values under key /specific name
        average = sum(grades.values())/len(grades)
        print(name,"'s Grades:",grades,"Average",round(average,2),"%")
    else:
        print("student not found")
       
else:
    print("Not searching")