import csv
import sys
import pprint
from docxtpl import DocxTemplate

# Function to convert a csv file to a list of dictionaries.  Takes in one variable called "variables_file"

def csv_dict_list(variables_file):
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    reader = csv.DictReader(open(variables_file, 'rb'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list


# Calls the csv_dict_list function, passing the named csv


def generate_word_document():
    context_for_word_docx = csv_dict_list(sys.argv[1])
    pprint.pprint(context_for_word_docx)
    for index, context in enumerate(context_for_word_docx):
    	doc = DocxTemplate(sys.argv[2])
        doc.render(context)
        doc.save(str(index)+"generated_doc.docx")


# Generates the documents
generate_word_document()
