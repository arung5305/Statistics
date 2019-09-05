#To read from csv file and put images into respective folders
#Written for lesion diagnosis classification problem  May 11 2018(base, updated June 2018)
#Author ArunG
import csv
import os
import shutil
'''
csv_file = "C:\\Users\\arun\\Documents\\DL\\Data\\AusDIAB_BL_CERA\\file.csv"
with open(csv_file) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	c=0
	for row in readCSV:
		c = c+1
		print(row[0])
		shutil.copy(row[0], "C:\\Users\\arun\\Documents\\DL\\Data\\GLAUCOMA\\Datasets\\300-400\\last\\"+row[0])
	print(c)
'''
csv_file = "C:\\Users\\arun\\Documents\\DL\\Data\\UkBioBank_Data\\csv\\MI_Fundus_Above4y.csv"
src_folder_global = "C:\\Users\\arun\\Documents\\DL\\Data\\UkBioBank_Data\\UKBIOBANK_FUNDUS\\March22_all\\"
with open(csv_file) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	c=0
	e=0
	for row in readCSV:
		c = c+1
		file_path = os.path.join(src_folder_global,row[0])
		if(os.path.exists(file_path)):
			e=e+1
			print(row[0])
			shutil.copy(file_path, "C:\\Users\\arun\\Documents\\DL\\Data\\UkBioBank_Data\\UKBIOBANK_FUNDUS\\MI\\above_4y\\")
	print("out of "+str(c)+" items in the list, "+str(e)+" existing items copied")
