#Python Code to Generate QRcodes

#Import the necessary libraries
#use pip install pyqrcode to obtain the necessary dependencies

import pyqrcode
from pyqrcode import QRCode
import os 
from random import randrange


#Generating A random Number to uniquely name our QRCode output file! 
random_ = randrange(0x000000,0xfffffff)
filename_ = "QRCode"+str(random_)

#String to Encode 
data = input("Encode ->")

#Generating the QRCode Object
#You can Further Explore the 'create' method for more parameters (Error, Version, etc) 
DataQRObject = pyqrcode.create(data)

#Generate an SVG Vector Image out of the QRCode Object We created
DataQRObject.svg(filename_+".svg", scale = 8)
if (DataQRObject) : print("Your QRCode Was Successfully Generated ! ")
else : print("There was some kind of error ! Try Again ...")
#Execute a System Command to open the Generated QRCode File
os.system("open " + str(filename_)+".svg")
