from pathlib import Path 
import os
class filehandling:
    def creatfilee(self):
        x=input("Enter your file name\n")
        if not Path(x).exists():
            with open(x,'w') as fs:
                data=input("Enter your content\n")
                fs.write(data)
        else:
            print("file already exit!\n")
    def readfile(self):
        n=input("Enter your file name\n")
        if  Path(n).exists():
            with open(n,'r') as fs:
                print(fs.read())
        else:
            print("File do nor exit!")
    def updatefile(self):
        n=input("Enter your file name\n")
        if  Path(n).exists():
            with open(n,'a') as fs:
                data=input("Enter the data:- \n")
                fs.write(data)
        else:
            print("File does not exit!")
    def deletefile(self):
        x=input("Enter your file name \n" )
        if  Path(x).exists():
                os.remove(x)
                print("File Deleted Sucessufully")
        else:
            print("File does not exit!")
user=filehandling()
print("press 1 for creating an file")
print("press 2 for reading the file ")
print("press 3 for updating the the file ")
print("press 4 for deleting the file")
check = int(input("tell your response :- "))
if check == 1:
    user.creatfilee()
if check == 2:
    user.readfile()
if check == 3:
    user.updatefile()
if check == 4:
    user.deletefile()