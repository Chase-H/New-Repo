import PyPDF2
import shutil
import csv
import os
import re

original_directory = '/mnt/c/Users/chase.hudson/Documents/GitHub/New_Repo/pdfs/original'
result_directory = '/mnt/c/Users/chase.hudson/Documents/GitHub/New_Repo/pdfs/result'
logfile = "log.csv"

rename_data = [['Original_File', 'Renamed_File']]
for subdir, dirs, files in os.walk(original_directory):
    for file in files:
        filepath = os.path.join(original_directory, file)
        with open(filepath, 'rb') as pdfFileObj:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj).getPage(0).extractText()
            result = re.search(r'\d{9}', str(pdfReader))
        if result:
            new_filepath = os.path.join(original_directory, result.group(0) + '-' + file)
            rename_data.append([filepath, new_filepath])
            os.rename(filepath, new_filepath)
        else:
            rename_data.append([filepath, 'Claim Number Not Found'])

with open(logfile, "w") as csv_file:
    writer = csv.writer(csv_file)
    for line in rename_data:
        writer.writerow(line)
