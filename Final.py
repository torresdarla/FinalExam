#Programmed by Darla Torres
#August 10, 2017

import Short
import os

#This function goes through the directory and creates a list of the relevant files that will be searched through
#It then takes that list, opens each file, and searches the file for the term and prints the line

def searchDir(term):
    searchList=[]
    files = os.listdir(".")
    for file in files:
        if ".txt" in file:
            searchList.append(file)
    for file in searchList:
        find = open(file, 'r')
        for line in find:
            if term in line:
                print "%s : %s" %(file,line)


#Here is the main function that runs the entrie program
def main():
    word = Short.userString("Enter a search term:")
    searchDir(word)
    

main()


