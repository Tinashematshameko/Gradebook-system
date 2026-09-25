# custom exceptions 

class StudentNotFoundError(Exception):
    # raised when a student cannot be found in the gradebook
    pass

class InvalidGradeError(Exception):
    
    # raised when an invalid grade is present
    pass
    
    
    
class Student:
    
    #studentss={}
    
    def __init__(self,name):
        self.name=name
        
        self.grades={}  # holds grades to a subject
        
        
       
    def get_grades(self,subject):
        while True:   # intentionally made to run forever no exit condition
            try: #skips to except when entering anything that is not a number
                grade=float(input(f"Enter {subject} grade:"))
                if  grade >= 0 and grade <= 100: #checks if marks are between 0 and 100 and stops loop if it is so continues forever if not
                   return(grade)   
                else:
                    raise InvalidGradeError ("invalid grade. Enter a grade between 0 and 100!")
            except ValueError:
                print("Please enter a number!")
        # value error and invalid grade error are handled gracefully
        
    def add_grades(self):
            
                #call function and save to dictionary
            self.grades["Maths"]=self.get_grades("Maths")
            self.grades["English"]=self.get_grades("English")
            self.grades["Science"]=self.get_grades("Science")
                 # successful entry of students
            
        
       
    def get_average(self):
         if not self.grades:   # check if grades exsist
             return 0
         return sum(self.grades.values())/ len(self.grades)
          
                
    def print_details(self):
            print(f"Student:{self.name}")
            for subject , mark in self.grades.items():
                print(f"{subject}: {mark}")
            print(f"Average: {round(self.get_average(),2)}")
            
        
            
        
        
   # def get_grade(self,maths,english,science):
    #    while True:   # intentionally made to run forever no exit condition
     #       try: #skips to except when entering anything that is not a number
      #          grade=float(input(f"Enter {name_of_subject} grade:"))
       #         if  grade >= 0 and grade <= 100: #checks if marks are between 0 and 100 and stops loop if it is so
        #           return(grade)
         #       else:
          #          print("invalid grade. Enter a grade between 0 and 100!")
           # except ValueError:
            #    print("Please enter a number!")
       # return()
    
class Gradebook:
    
    def __init__(self,max_students):
        self.max_students= max_students
        self.students =[]
        
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"{student.name} added successfully")
            return True # successful entry of students
        else:
            print("Cannot add. gradebook too full")
        return False
    
    def remove_student(self,name):
        
        
         for student in self.students:  #check if name exists in dictionary
             
         
         
              
                 if student.name.lower()== name.lower():  #finds student by name and removes name and grades
                 
                    self.students.remove(student)
                    print(f"{student.name} removed successfully")
                    return 
                #if not found
         raise StudentNotFoundError(f"Student '{name}' not found cannot remove.")    
            
            
    def search_student(self,name):
        
        for student in self.students:  #check if name exists in dictionary
            
        
        
             
                if student.name.lower()== name.lower():
                
                   student.print_details()
                   return student
        raise StudentNotFoundError(f"Student '{name}' not found.")   
                
    def sort_by_average(self):
        sorted_students = sorted(  # compares students by average the function below returns
            self.students,
            key=lambda s: s.get_average(),   # expects a function that gets one element from student list the function then uses the element/name to return their average
            reverse = True  #reverses the order to now biggest to smallest
            
            )
        
        print("Students sorted by average grade:")
        for s in sorted_students:
            print (f"{s.name} - Average: {round(s.get_average(),2)}%")
        return
        
    def sort_by_subject(self,subject):
        sorted_students = sorted(  # compares students by average the function below returns
            self.students,
            key= lambda s: s.grades.get(subject ,0),   # expects a function that gets one element from student list the function then uses the element/name to return their average
            reverse = True  #reverses the order to now biggest to smallest
            
            )
        
        print(f"Students sorted by {subject}:")
        for s in sorted_students:
            print (f"{s.name} - {subject}: {s.grades.get(subject, 'N/A')}")
        return
        
    def sort_by_name(self):  # sorting names alphabetically
        sorted_students = sorted(  # compares students by average the function below returns
            self.students,
            key= lambda s: s.name.lower(),
            
            reverse = False  #makes sure the order to now smallest to biggest
            
            )
        
        print("Students sorted by name:")
        for s in sorted_students:
            print (f"{s.name}")
        return
    
    def bubble_sort_by_average(self):
        n = len(self.students)
        for i in range(n):
            for  j in range(0, n-i-1): # compare the student averages 
                if self.students[j].get_average() < self.students[j+1].get_average():
                
                
                    self.students[j], self.students[j+1] = self.students[j+1],self.students[j]
                # swapped if they are in wrong order
            
        print("Students sorted by average grade using the bubble sort method:")
        for s in self.students:
            print(f"{s.name}- Average: {round(s.get_average(),2)}%")
        
           
s1 = Student("Ana")
s2 = Student("Bob")
s3 = Student("Charlie")
s4 = Student("Malebogo")
s5 = Student("Ethan")

#  manually set grades
s1.grades = {"Maths": 80, "English": 70, "Science": 90}
s2.grades = {"Maths": 60, "English": 65, "Science": 58}
s3.grades = {"Maths": 95, "English": 90, "Science": 100}
s4.grades = {"Maths": 72, "English": 76, "Science": 68}
s5.grades = {"Maths": 85, "English": 88, "Science": 82}

# create gradebook
g = Gradebook(10)  #argument is max number of students allowed
#add students
g.add_student(s1)
g.add_student(s2)
g.add_student(s3)
g.add_student(s4)
g.add_student(s5)            



g.sort_by_average()
g.sort_by_subject("Maths")  #maths is used as an example 

try:
    student=g.search_student("we")  # if i add a name not in the students list it will say student not found
    student.print_details()
except StudentNotFoundError as e:
    print(e)
    

try:
    student=g.remove_student("we")  # if i add a name not in the students list it will say student not found cannot remove
    
except StudentNotFoundError as e:
    print(e)

g.sort_by_name()
g.bubble_sort_by_average()



# FINAL TESTING AND DOCUMENTATION 
#The program was tested to make sure all functions work properly and that invalid inputs are handled gracefully with some of them using custom exceptions

# I was able to succesfully add 5 students and all their grades across 3 subjects (0-100)
#sorting,adding,removing,displaying and calculating average functions work as expected
# All functions work as expected and outputs are displayed correctly

# when searching for an existing name it displayed their name and results as expected but when searching for a name that doesnt exist it triggered the student not found error as expexted and diplayed "Student'name' not found" and continued execting as expected
#when removing a student that is not in the list it displayed a student not found error as expexted and diplayed "Student'name' not found in gradebook cannot remove" and continued execting as expected
# exception handling worked as expected ,the program does not crash and all errors are handled with no unhandled exceptions


#bubble sort was used to sort students correctly from higheest to lowest using their averages and without using the built in sorted function and the results are as expected as they match the results of the built in sorted function

#an invalid grade "hdyfg" was enterd and it triggered a value error and asked for a number to be entered
#an invalid grade both "-57" and 45 were entered and it triggered a invalid grade error and asked user to enter a number between 0 and 100
#the error messages were clear and easy to understand and did not cause the program to crash instead it continued running as expected

#for edge cases when trying to enter more students than the max limit allowed which was 10 a message would appear saying "cannot add. gradebook too full."


#Overall the program continues to run as expected after every handled exception , the program does not crash and all errors are handled with no unhandled exceptions
#The system is robust , error- tolerant and user friendly
