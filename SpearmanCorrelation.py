import json, os, re, sys, time
import numpy
import glob
import csv
import json


#change values here

csv_file = "C:\\Users\\USERNAME\\Desktop\\Correlation.csv"


reader = csv.reader(open(csv_file, "r"), delimiter=",")
x = list(reader)
result = numpy.array(x).astype("float")
#print (result[:,1])

from scipy.stats import spearmanr
x = result[:,0]

x_corr = result[:,1]
corr, p_value = spearmanr(x_corr, x)
print (corr)
