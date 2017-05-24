studentList = []
f=open('IUA.txt','w')
column = ['StudentId\t','StudentName\t','A1\t','A2\t','FinalExam\t','WeightedTotal\t','WeightedTotalwithBonus']
f.writelines(column)
f.close()
def inputValues():

    while True:
        print ("-----------------------------------------------------------------------------------------")         #print header
        print ("The Innovation University of Australia (IUA) Grade System ")
        print ("-----------------------------------------------------------------------------------------")

        print ("Please enter all marks out of 100")                                 #print message
        studentID = input("Please enter the student ID: ")
        studentName = input("Please enter the student name: ")
        assign1 = int(input("Please enter the marks for Assignment 1: "))           #input marks for assignment1
        assign2 = int(input("Please enter the marks for Assignment 2 : "))           #input marks for assignment2
        finalExam = int(input("Please enter the marks for Final Exam: "))         #input marks for final exam

        print ("Thank You!")   
                                                             #print thank you
        student = [studentID, studentName, assign1, assign2, finalExam]
        total_weight, total_weight_bonus = calculate(student)
        student.append(total_weight)
        student.append(total_weight_bonus)
        #studentList.append(student)
        f=open('IUA.txt','a')
        row=[str(value).center(len(column))+"\t" for value,column in zip(student,column)]
        row[0] = "\n"+row[0]
        f.writelines(row)
        f.close()
        ans = input("Do you want to enter marks for another student (Y/N)?")

        if ans != 'Y':
            return

def calculate(student):
    weight1 = int(student[2]) * 0.2                                                     #calculate weight for assignment1
    weight2 = int(student[3]) * 0.3                                                     #calculate weight for assignment2
    assignWeight = weight1 + weight2                                            #calculate total weight for assignments

    print ("Weighted mark for Assignment 1: ", weight1)                         #print weight of assignment1
    print ("Weighted mark for Assignment 2: ", weight2)                         #print weight of assignment2
    print ("Weighted mark for Assignment 1: ", assignWeight)                    #print total weight for assignments

    finalWeight = int(student[4]) * 0.5                                               #calculate weight for final exam
    totalWeight = assignWeight + finalWeight                                    #calculate total weight
            
    print ("Weighted mark for the Final Exam is: ", finalWeight)                #print weight of final exam
    print ("Total weighted mark for the subject: ", totalWeight)                #print total weight

    if totalWeight < 50:                                                        #check totalWeight and assign bonus
        bonus = 0 
    elif totalWeight < 70:
        bonus = (totalWeight-50) * 0.1
    elif totalWeight < 90:
        bonus = 2 + (totalWeight-70) * 0.15
    else:
        bonus = 5 + (totalWeight-90) * 0.2

    print ("Bonus mark: ", bonus)                                               #print bonus
    total = totalWeight + bonus                                                 #calculate total marks
    print ("Total mark with bonus: ", total) 
                                   #print total marks
    return  totalWeight, total

def searchStudent():

    while True:
        print ("-----------------------------------------------------------------------------------------")         #print header
        print ("The Innovation University of Australia (IUA) Grade System ")
        print ("-----------------------------------------------------------------------------------------")
        ID = input("Please enter the student ID to search: ")

        with open('IUA.txt', 'r') as f:
            studentList = [line.split('\t') for line in f.readlines()]

        flag = 0
        for student in studentList:
            if student[0].strip() == str(ID):
                print ("".join(column))
                print ("___"*30)
                print ("".join(student))
                flag = 1
                break

        if flag == 0:
            print ("Student Not Found")

        ans = input("Do you want to search for another student (Y/N)?")

        if ans != 'Y':
            return


while True:
    print ("================================================ ")
    print ("Welcome to the AGoS System of IUA")
    print ("Please select an option from the following.")
    print ("<A>dd details of a student")
    print ("<S>earch details of a student.")
    print ("<Q>uit")
    print ("================================================ ")
    option = input("Enter the option:")
    if option == 'A':
            inputValues()
    elif option == 'S':
            searchStudent()
    elif option == 'Q':
            break;
    else:
            print ("Incorrect option!! Please try again")

