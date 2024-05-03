'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import re

class Student:
    
    def __init__(self, FIO, bilnum, rating):
        
        self.FIO = FIO
        self.bilnum = bilnum
        self.rating = rating
    
    def printinf(self):
        
        print(f"('{self.FIO}'", str(self.bilnum), str(self.rating) + ")", sep = ", ") 
        
    def change_rating(self, change):
        
        self.rating = self.rating + change
        
class Starosta(Student):
    
    journal = {}
    
    def __init__(self, stud):
        
        Student.__init__(self, stud.FIO, stud.bilnum, stud.rating)
        self.N = 0
        self.journal[self.N] = {self.FIO : {self.bilnum : self.rating}}
        
    
    def addstudent(self, stud):
        self.journal[self.N + 1] = {stud.FIO : {stud.bilnum : stud.rating}}

    def removestudent(self, stud):
        self.journal.pop(stud.FIO)
 
    def showclass(self):
        for key in self.journal:
            print(key, self.journal[key], sep=" : ")
 

FIO = ""

while FIO == "" or not(all(chr.isalpha() or chr.isspace() for chr in FIO)):
    FIO = input()

bilnum = 0
while len(str(bilnum)) != 9:
    bilnum = int(input())
    

rating = int(input())


std1 = Student(FIO, bilnum, rating)

FIO = ""

while FIO == "" or not(all(chr.isalpha() or chr.isspace() for chr in FIO)):
    FIO = input()

bilnum = 0
while len(str(bilnum)) != 9:
    bilnum = int(input())
    

rating = int(input())

std2 = Student(FIO, bilnum, rating)

change = int(input())

std1.printinf()
std1.change_rating(change)
std1.printinf()
std2.printinf()

star = Starosta(std1)
star.printinf()
star.showclass()

