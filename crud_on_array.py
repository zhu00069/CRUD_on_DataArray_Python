"""
Description: the purpose of assignmemt3 is to import csv file and read csv file,
             save the first 10 records to array data structure,
             provide user options to achieve CRUD on data.
Created on 2019-02-19
Last modified on 2019-03-02
@author:Bo Zhu, student Number：040684747
"""

#import csv
import csv

def displayName():
    """display author name"""
    print ("\nAuthor: Bo Zhu\n")

def readDataFromCsv():
    """read data from scv file and read 10 records"""

    #exception handling try except to catch if file is missing or not available.
    try:
        #define an empty array
        dataArr = []
        #if file exsits, open & read file
        with open('data.csv') as file:
            reader =csv.reader(file)
            #variable line_count
            line_count = 0
            #for loop
            for row in reader:
                #print header
                if line_count == 0 :
                    print(row)
                #ignore print header, print nothing
                elif line_count ==1 :
                    print("")
                #append data, save in array
                elif line_count < 12:
                    dataArr.append(row)
                else:
                    break;
                line_count += 1
        #close file
        file.close()
    except IOError:
        #print IOErro msg
        print("Something went wrong when open the file")
    return dataArr


def readUserInputForAddEdit():
    """parse user's input data for each column"""

    #variable columm
    columm = {}
    #user input info save into ceach columns
    columm["Species"] = input("Species : ")
    columm["Year"] = input("Year : ")
    columm["Julian Day of Year"] = input("Julian Day of Year : ")
    columm["Plant Identification Number"] = input("Plant Identification Number : ")
    columm["Number of Buds"] = input("Number of Buds :")
    columm["Number of Flowers"] = input("Number of Flowers : ")
    columm["Number of Flowers that have Reached Maturity"] = input("Number of Flowers that have Reached Maturity : ")
    columm["Observer Initials"] = input("Observer Initials : ")
    columm["Observer Comments"] = input("Observer Comments : ")
    #variable newRecord to hold input columns' values
    newRecord = [columm["Species"], columm["Year"], columm["Julian Day of Year"],
              columm["Plant Identification Number"], columm["Number of Buds"], columm["Number of Flowers"],
              columm["Number of Flowers that have Reached Maturity"], columm["Observer Initials"],
              columm["Observer Comments"]]
    return newRecord

def add(myArray):
    '''define function add() to insert data to data structure'''

    #variable newRow, was assigned user input
    newRecord = readUserInputForAddEdit()
    #append new value after array
    myArray.append(newRecord)
    #print array
    printCurrentArray(myArray)
    print("\nadd succefully!")
    return myArray


def printCurrentArray(myArray):
    '''printCurrentArray function, to print array'''
    #variable line_counter
    line_counter = 0
    #for loop, print each line
    for i in range(0, len(myArray)):
            line_counter += 1
            print(line_counter,myArray[i])
    return myArray

def edit(myArray):
    '''defince function edit() to update a record in array'''

    #varible index, to store user input number
    index = int(input("\nPlease enter line number you want to edit: "))
    print ("\nPlease edit your selected record !\n")
    #print selected record
    print(myArray[index-1])
    #variable tmpRow, to store user input data
    tmpRow = readUserInputForAddEdit()
    #replace the select record with user input data
    myArray[index-1] = tmpRow
    #display array
    printCurrentArray(myArray)
    print("\nedit successfully!")
    return myArray



def delete(myArray):
    '''defince function delete() to delete a data in data structure'''
    #variable index, to store user input number
    printCurrentArray(myArray)
    index = int(input("\nPlease enter line number you want to delete: "))

    #delete record from array
    del myArray[index-1]
    #print updated array
    printCurrentArray(myArray)
    print("\ndelete successfully!")
    return myArray


def main():
    '''main funtion'''

    #variable dataArray
    dataArray = []
    print("\nStart to read data...")
    dataArray=readDataFromCsv()
    displayName()

    # privide select options for user
    print("Please enter your options (1-6):")
    print("1: reload 10 records")
    print("2: display all records")
    print("3: add a record")
    print("4: edit a record")
    print("5: delete a record")
    print("6: exit")

    #variable option
    option = 0
    #while loop these options, break loop when option = 6
    while (option < 6):

        # user option input
        option = int(input("Please enter your option: "))

        if option == 1:
            dataArray = readDataFromCsv()
            printCurrentArray(dataArray)
            displayName()
        elif option == 2:
            printCurrentArray(dataArray)
            displayName()
        elif option == 3:
            dataArray = add(dataArray)
            displayName()
        elif option == 4:
            dataArray=edit(dataArray)
            displayName()
        elif option == 5:
            dataArray= delete(dataArray)
            displayName()
        elif option == 6:
            break
        else:
            print("Invalid input!")

if __name__ == '__main__':
    main()


