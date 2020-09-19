#####################################################################################
#             Python program to convert CSV to JSON for Django's model              #
#                       support Thai language & Unicode                             #
#####################################################################################
# Program name : Csv2Json
# version : 1.1
# Developer : Krabeeputh Kaekwam
# e-mail : krabeeputh@gmail.com
# Date : 19 Sept. 2020
# license : Free of charge for personal and commercial use
#          "The Knowledge should be shared such a gift from god :)"
#
# Background : I am living in non-English language country, We are speak, read and 
# write in Thai language. I am just starting to learn Python and Django and faced a 
# problem when working with Thai language, generated wrong charactors and unreadable!!.
# After read from many websites, Finally I found a few resources to get close the
# solution. Then I revised the code to support my working after tested it works fine
# with Thai charactor which be Unicode. I hope this program will help Thai people
# and other people who are using non-English too :)
#
# my references : 
# https://realpython.com/python-csv/
# https://docs.python.org/3/library/csv.html
# https://thepythonguru.com/python-how-to-read-and-write-csv-files/
# https://www.geeksforgeeks.org/convert-text-file-to-json-in-python/
# https://github.com/jcamier/csv-json-django/blob/master/convert_csv_to_json.py
# https://bigdata.go.th/big-data-101/unicode-and-big-data-text-processing-part-2/

import json, csv
from pathlib import Path
  
class Csv2Json:

    # init method or constructor
    def __init__(self, file_in, file_out, model, fields=[], pk_col=0):
        self.file_in = file_in
        self.file_out = file_out
        self.model = model
        self.fields = fields
        self.pk = pk_col

    # Case 1 : the CSV file doesn't have ID for primary key
    def auto_pk(self):
        # Open CSV file as a text file with Python’s built-in open() function, which  
        # returns a file object. Default open mode is "r". So, no need to specify.
        # If csvfile is a file object, it should be opened with newline=''.
        # IMPORTANT : The CSV files MUST save as UTF8 to support Thai & Unicode,
        # then open it with encoding="utf8"
        with open(self.file_in, newline='', encoding="utf8") as file:
            # Use Python's built-in csv library to read CSV format from microsoft Excel
            # Each row read from the csv file is returned as a list of strings.
            # By default, delimiter=',', quotechar='"', doublequote=True
            csv_reader = csv.reader(file)
            x = 0 # count variable for PK (id) creation 
            # creating json file to support Thai language & Unicode
            json_file = open(self.file_out, "w", encoding="utf8") 
            output = [] # resultant list
            for line in csv_reader:
                x += 1 # PK index start from 1                       
                i = 0 # loop variable 
                dict1 = {} # intermediate dictionary 
                dict2 = {} # fields dictionary
                while i<len(self.fields):
                    # creating dictionary for each field
                    dict2[self.fields[i]] = line[i]
                    i += 1
                dict1 = { # add the record of each field to the intermediate dict.
                    "model": self.model,
                    "pk": x,
                    "fields": dict2 
                }
                output.append(dict1) # appending dict and sub-dict to the list
            # Default Json will save character in ASCII code only. For Thai
            # character have to use "ensure_ascii=False" to avoid the converting 
            # character in ASCII code before save file. That makes unreadable!!
            json.dump(output, json_file, indent = 4, ensure_ascii=False)        
            json_file.close()

    # Case 2 : the CSV file already have ID for primary key
    def define_pk(self):
        # Open CSV file as a text file with Python’s built-in open() function, which  
        # returns a file object. Default open mode is "r". So, no need to specify.
        # If csvfile is a file object, it should be opened with newline=''.
        # IMPORTANT : The CSV files MUST save as UTF8 to support Thai & Unicode,
        # then open it with encoding="utf8"
        with open(self.file_in, newline='', encoding="utf8") as file:
            # Use Python's built-in csv library to read CSV format from microsoft Excel
            # Each row read from the csv file is returned as a list of strings.
            # By default, delimiter=',', quotechar='"', doublequote=True
            csv_reader = csv.reader(file)
            # creating json file to support Thai language & Unicode
            json_file = open(self.file_out, "w", encoding="utf8")
            output = [] # resultant list
            for line in csv_reader:                  
                i = 0 # loop variable 
                dict1 = {} # intermediate dictionary 
                dict2 = {} # fields dictionary
                while i<len(self.fields):
                    if self.pk == i :
                        pk = line[i]
                    else :                        
                        dict2[self.fields[i]] = line[i] # creating dictionary for each field
                    i += 1
                dict1 = { # add the record of each field to the intermediate dict.
                    "model": self.model,
                    "pk": pk,
                    "fields": dict2
                }
                output.append(dict1) # appending dict and sub-dict to the list
            # Default Json will save character in ASCII code only. For Thai
            # character have to use "ensure_ascii=False" to avoid the converting 
            # character in ASCII code before save file. That makes unreadable!!
            json.dump(output, json_file, indent = 4, ensure_ascii=False)
            json_file.close()