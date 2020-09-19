from pathlib import Path
from csv2json import Csv2Json
  
#-----------------------------------------------------------------------------------
#                               CONFIGURATION PART
# Please Config all variables below to match your resources
# NOTE :The text/CSV file has to saved in UTF-8 to support UNICODE
#-----------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

text_file_name = BASE_DIR/'countries.csv' # the CSV file to be converted 
json_file_name = BASE_DIR/'countries.json' # the JSON output file
app_name = "member" # change this to your Django app name
model_name = "Country" # the name of you Django model
fields =[ # Change your fields in this list
    'iso_3166_1_numeric', 
    'iso_3166_1_a2',
    'iso_3166_1_a3',
    'country_general_name',
    'country_general_name_th',
    'country_formal_name', 
    'country_formal_name_th', 
    'capital_city',
    'capital_city_th',
    'continent',
    'languages'
]
model = app_name + '.' + model_name

#-----------------------------------------------------------------------------------
#                      How to use the Csv2Json class? 
# just follow 2 steps as below
#-----------------------------------------------------------------------------------
# 1. define object, if your csv file already have ID for primary key 
#    please specify the column (the 1st column is default, start with 0)

a = Csv2Json(text_file_name, json_file_name, model, fields)

# 2. call class method to excute in 2 conditions
# if your csv file doesn't have ID, just call method : auto_pk()
# if your csv file already have ID for primary key, call method : define_pk()

a.auto_pk() 
#a.define_pk()