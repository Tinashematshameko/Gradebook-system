
no_of_students_in_class = int (input("enter the number of students in class:"))

students=[]
maths=[]
english=[]
science=[]
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
        student=(name , maths_grade , english_grade, science_grade)
        students.append(student)
        
        
        
print("Student Summary")
for name, maths_grade, english_grade, science_grade in students:
    average = (maths_grade + english_grade + science_grade)/3
    
    print("Name:", name, "Maths grade=" , maths_grade,"%", "English grade=" , english_grade,"%", "Science grade=" , science_grade,"%" ,"Average =",round( average,2),"%")


print("The highest grade in maths is",max(maths),"%")
print("The lowest grade in maths is",min(maths),"%")
print("The highest grade in english is",max(english),"%")
print("The lowest grade in english is",min(english),"%")
print("The highest grade in science is",max(science),"%")
print("The lowest grade in science is",min(science),"%")

