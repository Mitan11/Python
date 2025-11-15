class Student:
    # name = ""
    # roll_no = 0

    #problematic code with class variables showaing same data for all objects
    # marks = []

    #solution using instance variables 
    #using constructor to initialize instance variables
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = []

    def getData(self):
        self.name = input("Enter student name: ")
        self.roll_no = int(input("Enter roll number: "))
        self.marks = []
        for i in range(3):
            mark = float(input(f"Enter mark for subject {i+1}: "))
            self.marks.append(mark)

    def showData(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print("Marks:", self.marks)


s1 = Student()
s1.getData()

s2 = Student()
s2.getData()

s1.showData()
s2.showData()