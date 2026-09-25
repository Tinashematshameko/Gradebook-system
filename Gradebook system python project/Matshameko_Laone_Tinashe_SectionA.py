no_of_students_in_class = int (input("enter the number of students in class:"))
total=0
counter=0
for i in range(no_of_students_in_class):
    counter = counter +1
    name = input("enter name:")
    grade = float(input("enter grade:"))
    while grade < 0 or grade > 100:
        print("invalid grade")
        grade = float(input("enter grade:"))
        
    total = total + grade
    print("name:", name , "grade:", grade ,"%")
average = total/counter

print("total=",total , "overall class average=", round(average,2),"%")


