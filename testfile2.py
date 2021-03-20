myfile = open("D:\poem1.txt","r")
#str = myfile.read()
#size = len(str)
str = " "
while(str):
    str = myfile.readline()
    print(str)
    entr = input("")
#print("Size occupied by the file is ",size)
myfile.close()