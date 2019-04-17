""""
Description: unit test for Assignment4 Final Project - final.py
Created on 2019-03-20
Last modified on 2019-04-11
@author:Bo Zhu, student Number：040684747
"""
# import unit test framework
import unittest
from unittest import TestCase
# import package, classes, and function
from FinalProject_1.final import readDataFromCsv
from FinalProject_1.final import readHeaderFromCsv
from FinalProject_1.final import DataFormatAdvance
from FinalProject_1.final import displayName

class Testing(TestCase):
    """
    This is a unit test verifying that the sorted records(by column 2)
    matches the expected sort order.
    """
    def setUp(self):
        """
        Set up before unit test.

        :return: None
        """
        # variable dataFormat, empty array
        self.dataFormat = []
        # instantiate objects to be used in unit test
        self.dataFormat = readDataFromCsv()
        # insert header to the beginning of dataArray
        self.dataFormat.insert(0,readHeaderFromCsv())
        # instance object from subclass DataFormatAdvance
        self.dataFormatAdvance = DataFormatAdvance()
        # set 10 records data format
        self.dataFormatAdvance.setMyData(self.dataFormat)
        # set sort by column = 2
        self.dataFormatAdvance.setSortColumn(2)
        # set sort by column name
        self.dataFormatAdvance.setColumnName()


    def test_descending_sort(self):
        """
        This is test on descending sort by column 2, Julian Day of year
        :return: None
        """
        # display author name
        displayName()

        # format data
        self.dataFormatAdvance.formatData()
        # set descending order
        self.dataFormatAdvance.setSortOrder("descending")
        # sort data
        result1 = self.dataFormatAdvance.sortingData()

        # display author name
        displayName()
        # variable temKey to store column name. This is a dictionary key
        tmpKey = "Julian Day of Year"
        # assert true if records of columns 2 are the same as correct order
        self.assertEqual(result1[0][tmpKey], str(196))
        self.assertEqual(result1[1][tmpKey], str(193))
        self.assertEqual(result1[2][tmpKey], str(190))
        self.assertEqual(result1[3][tmpKey], str(188))
        self.assertEqual(result1[4][tmpKey], str(184))
        self.assertEqual(result1[5][tmpKey], str(181))
        self.assertEqual(result1[6][tmpKey], str(178))
        self.assertEqual(result1[7][tmpKey], str(175))
        self.assertEqual(result1[8][tmpKey], str(172))
        self.assertEqual(result1[9][tmpKey], str(169))

    def test_read_first_line_after_desc_sorting(self):
        """
        This is test for comparing if the first line record after desc sorting match with the actrual record
        :return: None
        """
        # display author name
        displayName()

        # format data
        self.dataFormatAdvance.formatData()
        # set descending order
        self.dataFormatAdvance.setSortOrder("descending")
        # sort data
        result1 = self.dataFormatAdvance.sortingData()

        # display author name
        displayName()
        #variables to hold each columnn's value
        tmpKey_column1 = "Species"
        tmpKey_column2 = "Year"
        tmpKey_column3 = "Julian Day of Year"
        tmpKey_column4 = "Plant Identification Number"
        tmpKey_column5 = "Number of Buds"
        tmpKey_column6 = "Number of Flowers"
        tmpKey_column7 = "Number of Flowers that have Reached Maturity"
        tmpKey_column8 = "Observer Initials"
        tmpKey_column9 = "Observer Comments"

        #compare the first record of match with actural record by each column
        self.assertEqual(result1[0][tmpKey_column1], str('Dryas integrifolia'))
        self.assertEqual(result1[0][tmpKey_column2], str(2016))
        self.assertEqual(result1[0][tmpKey_column3], str(196))
        self.assertEqual(result1[0][tmpKey_column4], str(1))
        self.assertEqual(result1[0][tmpKey_column5], str(0))
        self.assertEqual(result1[0][tmpKey_column6], str(0))
        self.assertEqual(result1[0][tmpKey_column7], str(31))
        self.assertEqual(result1[0][tmpKey_column8], str('LP'))
        self.assertEqual(result1[0][tmpKey_column9], str(''))

if __name__ == '__main__':
    # execute unittest.main()
    unittest.main()