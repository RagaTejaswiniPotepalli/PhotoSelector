import os.path
import shutil
from os import path
from shutil import copyfile
PicNames = []
SourceD = input("enter the source file path")
while True:
    PicName = input("Enter your value: ")
    if PicName == "0":
        break
    else:
        PicNames.append(PicName)

DestinationD = "C:\\Users\\mails\\OneDrive\\Pictures\\Selected Photos\\Photos Candid - Wedding"
for Pic in PicNames:
    finalName = SourceD + "\\" + "_89A" + Pic + ".JPG"
    if (path.exists(finalName)):
        shutil.copy(finalName, DestinationD)
    else:
        print("_89A" + Pic + ".JPG" + "does not exist")





