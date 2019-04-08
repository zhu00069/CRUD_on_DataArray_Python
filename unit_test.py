'''
Description: unit test for assignment3, test add function
Created on 2019-03-02
Last modified on 2019-03-02
@author:Bo Zhu, student Number：040684747
'''

#import unit test framework
import unittest

#import, readDataFromCsv, printCurrentArray functions from file crud_on_array.py
from crud_on_array import readDataFromCsv
from crud_on_array import printCurrentArray

class Test(unittest.TestCase):
    """
        The basic class that inherits unittest.TestCase
    """

    def test(self):
        #fist line data information
        line1 = ['Dryas integrifolia', '2016', '169', '1', '12', '0', '0', 'AF, IW', '']

        #read data from csv
        a = readDataFromCsv()
        #get 10 records from array list
        result=printCurrentArray(a)
        #read first line of array
        read_line1= result[0]

        #if read firstline result equal to line1 , return True
        self.assertEqual(read_line1, line1)

        #print Author name
        print("\nAuthor: Bo Zhu")


if __name__ == '__main__':
    #begin the unittest.main()
    unittest.main()
