import os
text_file = open("/home/mab/Desktop/testedname.txt", "r")
list1 = text_file.readlines()

path = "/media/usbdrive3/AREDS_2010-untar/jpg_dng/Fundus/Field_2"
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

for i in list1:
    print(i)