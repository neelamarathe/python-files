import pickle
class student:
    def __init__(self, rno = 0, name = " "):
        self.rollNo = rno
        self.name = name 
        self.marks1, self.marks2 = 0.0,0.0
    def readMarks(self):
        print("Enter 2 subject marks")
        self.marks1 = float(input("Enter first subject marks: "))
        self.marks2 = float(input("Enter second subject marks: "))
    def display(self):
        print("student details are")
        print("roll number: ", self.rollNo)
        print("name: ", self.name)
        print("marks in two subjects: ",self.marks1," and ", self.marks2)

stud1 = student(15, "Abhay")
stud2 = student(15, "Ameya")
stud1.readMarks();
stud2.readMarks();

file1=open("student.det","wb")
pickle.dump(stud1,file1)
pickle.dump(stud2,file1)
file1.close();
file1=open("student.det","rb")
stud1 = student()
try:
    while True:
        stud1 = pickle.load(file1)
        stud1.display();
except EOFError:
    file1.close();
