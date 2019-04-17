"""
Description: read csv file, save first 10 records to array data structure,
             provide user options to achieve CRUD operation
             this final project use two advanced language features:
             Inheritance & Data Structure (use dictionary for sorting by column
Created on 2019-03-14
Last modified: 2019-04-11
@author:Bo Zhu, student Number：040684747
"""

#import csv
import csv
class DataFormat():
    """
    This class is super class
    """
    def __init__(self,data = []):
        """
        constructor
        """
        self.data = data

    def setMyData(self, data):
        """
        setter for data
        :param data , data array
        """
        self.data = data

    def getMyData(self):
        """
        getter for data
        :return: data, data array
        """
        return self.data

    def formatData(self):
        """
        this function is used to simple format, append each record and store into array
        :return: an array of records read from csv file
        """
        # define an empty array to store temporary data
        tmpdata = []
        # for loop to append each record, store into array
        for row in self.data:
            for i in range(0, len(row)):
                tmpdata.append(row[i])
        self.data = tmpdata
        print (self.data)


class DataFormatColumn(DataFormat):
    """
    This class is subclass, inherits from super class DataFormat
    """
    def __init__(self, data = [], columnNumber = []):
        """
        invoke _init_ method of super class DataFormat. it will extend super class's attributes data,
        columnNumber is subclass attribute
        """
        super().__init__(self)
        self.data = data
        self.read_column = columnNumber

    def setReadColumn(self,value):
        """
        setter for read columnNumber
        :param value: columnNumber
        """
        self.read_column = value

    def getReadColumn(self):
        """
         getter for read columnNumber
        :return: read_column
        """
        return self.read_column

    def add(self):
        """
        This function is used to add an record
        """
        newRow = readUserInputForAddEdit()
        self.data.append(newRow)
        #printCurrentArray()
        #return myArray

    def displayData(self):
        """
        This function is used to display all data
        :return: data array
        """
        # variable line_counter, set line number for each record
        line_counter = 0;
        # for loop to display data array
        for i in range(0, len(self.data)):
            line_counter += 1;
            print(line_counter, self.data[i])

    def edit(self):
        """
        This function is used to edit an record
        """
        # variable index, to store user input(line number)
        index = int(input("Please enter line number 1-10 that you want to edit: "))
        print("Start to change the following record ! ")
        print(self.data[index-1])
        # varibale temRow to store new record
        tmpRow = readUserInputForAddEdit()
        # update record
        self.data[index-1] = tmpRow
        #printCurrentArray(self)
        #return myArray

    def delete(self):
        """
        This function is used to delete an record
        """
        # variable index to store user input: line number
        index = int(input("Please enter line number 1-10 that you want to delete: "))
        # delete the record
        del self.data[index-1]
        #printCurrentArray(self)
        #return myArray

    def formatData(self):
        """
        This function extends from super class DataFormat, is override method
        """
        tmpRow = []
        for row in self.data:
            if self.read_column <= len(row) :
                tmpRow.append(row[self.read_column])
        for i in tmpRow:
            print (i)

class DataFormatAdvance(DataFormat):
    """
    This class is subclass, it inherits from super class DataFormat
    """

    def __init__(self,data = [], columnNumber = 0, sort_order = "ascending", columnName=""):
        """
        invoke _init_ method of super class DataFormat. it extends super class's
        data, column number, column name and sort_order are subclass's attributes,
        set default value to columnNumber and sort_order
        """
        # call super constructor
        super().__init__(self)
        self.data = data
        self.columnNumber = columnNumber
        self.sort_order = sort_order
        self.columnName = columnName

    def formatData(self):
        """
        This function extends from super class DataFormat, is a override method. It used to change list nested in a list
        to dictionary nested in a list, the key of the dictionary is the column header name read from method
        readFromHeader(), the value of the corresponding key is the column value number from readFromCsv(),
        return a list whose element is a dictionary
        list[dic{},dic{}...]
        """
        # variable tmpList, define an empty array list
        tmpList = []
        # variable tempDic, define an empty dictionary
        tmpDic = {}

        # for loop, used to change structure to list[dic{},dic{}...]
        for r in range(1,len(self.data)):
            for i in range(0,len(self.data[0])):
                tmpDic[self.data[0][i]] = self.data[r][i]
            # append each tmpDic{} into tmpList[]
            tmpList.append(tmpDic)
            tmpDic = {}
        self.data = tmpList
        for row in self.data:
            print (row)

    def getSortOrder(self):
        """
        getter for sort order
        """
        print (self.sort_order)

    def setSortOrder(self,value):
        """
        setter for sort order
        :param value: value of sort type
        """
        self.sort_order = value

    def getSortColumn(self):
        """
        getter for sort column
        """
        print (self.columnNumber)

    def setSortColumn(self, number):
        """
        setter for sort column
        :param number: value of sort column number
        """
        self.columnNumber = number

    def setColumnName(self, name = ""):
        """
        setter for sort column name
        :param name: empty column name
        """
        if name == "":
            self.columnName = self.data[0][self.columnNumber]
        else:
            if name in self.data[0]:
                self.columnName = name
            else :
                print ("Unexisting Column Name")

    def sortingData(self):
        """
        this function is used to process sorting by ascending/descending
        :return:data, sorted data
        """

        def myFunc(e):
            """
            this is nested function, used to set sorting data by column name
            """
            return e[self.columnName]
        print ("\nSet descending sort by column: " + self.columnName + "\n")

        # if else condition: ascending/descending sort order
        if self.sort_order == "ascending":
            # a built-in list.sort() method to do ascending sort by key = columnName (call function myFunc())
            self.data.sort( key = myFunc)
        else :
            # a built-in list.sort() method to do descending sort by key = columnName (call function myFunc())
            self.data.sort( key = myFunc, reverse = True)
        # for loop to print sorted data
        for row in self.data:
            print (row)
        return self.data

def readDataFromCsv():
    """
    This function is used to read data from scv file
    """
    # exception handling try except to catch if file is missing or can not open.
    try:
        # define an empty array
        dataArr = []
        # if file exists, open file
        with open('E:/CP-2019W/CST8333_351ProgrammingLanguageResearch/data.csv') as file:
            # read csv file
            reader =csv.reader(file)
            # variable line_count
            line_count = 0
            # for loop
            for row in reader:
                if line_count == 0 or line_count == 1:
                    # ignore header lines (line1 & line2)
                    pass
                elif line_count < 12:
                    dataArr.append(row)
                else:
                    break;
                line_count += 1
        # close file
        file.close()
    except IOError:
        print("Something went wrong when open the file")
    return dataArr

def readHeaderFromCsv():
    """
    This function is used to read header from scv file
    """
    # exception handling try except to catch if file is missing or can not open.
    try:
        # open file
        with open('E:/CP-2019W/CST8333_351ProgrammingLanguageResearch/data.csv') as file:
            # file is the list that contains the read rows.
            reader =csv.reader(file)
            # variable line_count
            line_count = 0
            # for loop
            for row in reader:
                if line_count == 0:
                    headerArr=row
                else:
                    break;
                line_count += 1
        # close file
        file.close()
    except IOError:
        print("Something went wrong when open the file")
    return headerArr

def printCurrentArray(myArray):
    """"
    This function is used to display the current array
    """
    #variable line_counter
    line_counter = 0
    # for loop, print each line
    for i in range(0, len(myArray)):
        line_counter += 1
        print(line_counter,myArray[i])


def displayName():
    """
    This function is used to display author's name
    :return: None
    """
    print ("\nAuthor: Bo Zhu\n")


def readUserInputForAddEdit():
    """
    This function is used to parse user's input of each column
    :return: newRow
    """
    print("Please input new record data !")
    fieldnames = {}
    # prompt user input for each column
    fieldnames["Species"] = input("Species : ")
    fieldnames["Year"] = input("Year : ")
    fieldnames["Julian Day of Year"] = input("Julian Day of Year : ")
    fieldnames["Plant Identification Number"] = input("Plant Identification Number : ")
    fieldnames["Number of Buds"] = input("Number of Buds :")
    fieldnames["Number of Flowers"] = input("Number of Flowers : ")
    fieldnames["Number of Flowers that have Reached Maturity"] = input("Number of Flowers that have Reached Maturity : ")
    fieldnames["Observer Initials"] = input("Observer Initials : ")
    fieldnames["Observer Comments"] = input("Observer Comments : ")
    # variable newRow to store new record
    newRow = [fieldnames["Species"], fieldnames["Year"], fieldnames["Julian Day of Year"],
              fieldnames["Plant Identification Number"], fieldnames["Number of Buds"], fieldnames["Number of Flowers"],
              fieldnames["Number of Flowers that have Reached Maturity"], fieldnames["Observer Initials"],
              fieldnames["Observer Comments"], '']
    return newRow



def waitUserInput(dataArray, myData):
    """
    This function is used to provide user option
    :param dataArray: 10 records of data
    :param myData: format 10 records of data
    """
    print("1: roload the data")
    print("2: add a record")
    print("3: display all record")
    print("4: edit a record")
    print("5: delete a record")
    print("6: exit")
    # call displayName function to print author name
    displayName()
    # variable option, user option number
    option = 0
    while (option < 6):
        option = int(input("Please enter your option: "))
        # if user select option 1: reload record, read the records from file into array again
        if option == 1:
            dataArray = readDataFromCsv()
            myData = DataFormatColumn(dataArray)
            myData.displayData()
            displayName()
        # if user select option 2: add record, add a record into array
        elif option == 2:
            myData.add()
            dataArray = myData.getMyData()
            printCurrentArray(dataArray)
            print("\nadd successfully!")
            displayName()
        # if user select option 3: display all record, display all records
        elif option == 3:
            myData.displayData()
            #printCurrentArray(dataArray)
            displayName()
        # if user select option 4: edit a record, display specific record then update the record
        elif option == 4:
            myData.edit()
            dataArray = myData.getMyData()
            printCurrentArray(dataArray)
            print("\nedit successfully!")
            displayName()
        # if user select option 5: delete a record, delete the record for user
        elif option == 5:
            myData.delete()
            dataArray = myData.getMyData()
            printCurrentArray(dataArray)
            print("\ndelete successfully!")
            displayName()
        # if user select option 6: exit, exit from the program
        elif option == 6:
            break
        # if user input is invalid, give user an error message!
        else:
            print("Invalid option input!")

def main():

    # variable dataArray to store data which reads from csv
    dataArray = readDataFromCsv()

    # original data format
    myData = DataFormat()
    myData.setMyData(dataArray)
    myData.formatData()

    # for loop is used to loop 10 records to format data with column name
    for i in range (0,9):
        myData1 = DataFormatColumn(dataArray,i)

    # call function waitUserInput() to provide user options
    waitUserInput(dataArray, myData1)
    print("\n")

    # create instance myData2 from subclass DataFormatAdvance
    myData2 = DataFormatAdvance()
    # insert header into beginning of dataArray
    dataArray.insert(0,readHeaderFromCsv())
    # set 10 records data which reads from csv
    myData2.setMyData(dataArray)
    # set sort order based on column = 2
    myData2.setSortColumn(2)
    # set clomun name
    myData2.setColumnName()
    # format data
    myData2.formatData()
    # set descending sort
    myData2.setSortOrder("descending")
    # descending sort
    myData2.sortingData()
    # display author name
    displayName()


if __name__ == '__main__':
    main()
    # start main()