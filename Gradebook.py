# Name= PULKIT KOHLI
# Roll No. = 2501420007
# Intro = Lecturers often need a fast and accurate way to compute statistics on student marks. Instead of manually calculating averages or assigning grades, this mini project helps automate the entire process via a Python-based GradeBook Analyzer CLI. The system will read marks from input or a CSV file, perform key statistical analysis, assign grades, and generate summaries in a user-friendly format.


while True:
    marks = float(input("Enter your marks : "))

    if marks == -1:
        print("Exit")
        break
   
    if marks<100 and marks>90:
        print("grade=A+")
    elif marks<90 and marks>80:
        print("grade=A")
    elif marks<80 and marks>70:
        print("grade=B+")
    elif marks<70 and marks>60:
        print("grade=B")
    elif marks<60 and marks>50:
        print("grade=c+")
    elif marks<50 and marks>40:
        print("C")
    elif marks<40 and marks>33:
        print("D+")
    else:
        print("FAIL !")
    print() 