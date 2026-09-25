class Student:
    
    #studentss={}
    
    def __init__(self,name):
        self.name=name
        
        self.grades={}  # holds grades to a subject
        
        
        
    def get_grades(self,subject):
        while True:   # intentionally made to run forever no exit condition
            try: #skips to except when entering anything that is not a number
                grade=float(input(f"Enter {subject} grade:"))
                if  grade >= 0 and grade <= 100: #checks if marks are between 0 and 100 and stops loop if it is so
                   return(grade)
                else:
                    print("invalid grade. Enter a grade between 0 and 100!")
            except ValueError:
                print("Please enter a number!")
        
        
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
    
    def remove_student(self,student):
        
            self.students.remove(student)
            print(f"{student.name} removed successfully")
            
            return
    
    def search_student(self,name):
        
        for student in self.students:  #check if name exists in dictionary
            
        
        
             
                if student.name.lower()== name.lower():
                
                   student.print_details()
                   return student
        print("Student not found.")   
                
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
g.search_student("Bob")  # if i add a name not in the students list it will say student not found
g.remove_student(g.students[1]) #removes name in index 1
