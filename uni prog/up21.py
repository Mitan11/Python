# class Customer:
#     name = ''
#     address = ''
#     phone = ''

#     def getData(self):
#         self.name = input("Enter Customer Name: ")
#         self.address = input("Enter Customer Address: ")
#         self.phone = int(input("Enter Customer Phone Number: "))

#     def displayData(self):
#         print("\nCustomer Details:")
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")
#         print(f"Phone Number: {self.phone}")


# c1 = Customer()
# c1.getData()
# c1.displayData()

# print()

# c2 = Customer()
# c2.getData()
# c2.displayData()

class Student:
    student = []
    marks = {}
    subjects = ['DAD' , 'Python' , 'DSA' , 'CSCL']
    def getdata(self):
        self.name = input("Enter Student Name: ")
        self.roll = int(input("Enter Student Roll Number: "))

        for sub in self.subjects:
            self.marks[sub] = int(input(f"Enter marks for {sub} out of 100 : "))            

        self.student.append({"name": self.name, "roll": self.roll, "marks": self.marks})

    def displaydata(self):
        print("\nStudent Details:")
        for stud in self.student:
            print(f"\nName: {stud['name']}")
            print(f"Roll Number: {stud['roll']}")
            print("Marks:")
            for sub, mark in stud['marks'].items():
                print(f"  {sub}: {mark}/100")

    def percentage(self):
        for stud in self.student:
            total_marks = sum(stud['marks'].values())
            percentage = (total_marks / (len(self.subjects) * 100)) * 100
            print(f"\nPercentage of {stud['name']} (Roll No: {stud['roll']}): {percentage:.2f}%")

s1 = Student()
s1.getdata()
s1.displaydata()
s1.percentage()

s2 = Student()
s2.getdata()
s2.displaydata()
s2.percentage()