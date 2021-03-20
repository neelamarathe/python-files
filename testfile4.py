myfile = open("D:\poem3.txt","a+")
choice = input("Do you want to enter line in a notepad file?  \n Press Y for yes - ")

while((choice == 'Y')|(choice =='y')):
    content = input("Enter a line for notepad file : \n")
    myfile.write(content)
    choice = input("Do you want to enter line in a notepad file?  \n Press Y for yes - ")
    myfile.write('\n\n')
myfile.close();

readfile = open("D:\poem3.txt","r")
str = readfile.read()
print(str)
#print("Size occupied by the file is ",size)