#Python Code to Generate QRcodes

#Import the necessary libraries
#use pip install pyqrcode 
#use pip install qrtools , pip install pypng
#You Need to pip install zbar and pillow as well
#use above commands to obtain the necessary dependencies

import pyqrcode
from pyqrcode import QRCode
from qrtools.qrtools import QR
import os 
from random import randrange

def GenerateQRCode() : 	
	#Generating A random Number to uniquely name our QRCode output file! 
	random_ = randrange(0x000000,0xfffffff)
	filename_ = "QRCode"+str(random_)

	#Text/String to Encode 
	data = input("Encode ->")
	if (data == "") : #no text provided
		print ("Please Enter the text you want to encode ! ")
		GenerateQRCode() #Restaring GenerateQRCODE Function
	#Generating the QRCode Object
	#You can Further Explore the 'create' method for more parameters (Error, Version, etc) 
	DataQRObject = pyqrcode.create(data)

	#Generate an SVG Vector Image out of the QRCode Object We created
	DataQRObject.png(filename_+".png", scale = 8)
	if (DataQRObject) : 
		print("Your QRCode Was Successfully Generated ! ")
		start()
	else : 
		print("There was some kind of error ! Try Again ...")
		start()
	#Execute a System Command to open the Generated QRCode File
	os.system("open " + str(filename_)+".png")
	cycle = input("Generate another ? (y/n)")
	if (cycle == 'y') : GenerateQRCode()
	elif (cycle == 'n') : start()
	
def ReadQRCode():
	#Ask the User to provide the Path to the required file
	PATH = input("QRCODE File PATH : ")
	if (PATH) : 
		#Creating the qrtools.QR object
		qrobj = qrtools.QR()
		
		qrobj.decode(filename=str(PATH))  #Decoding our file
		DecodedQRCodeObject = qrobj.data #Getting the text Output 
		print("Your QRCode Contents : " + str(DecodedQRCodeObject)) #Printing Results
		start() #Restarting the Program
	else : 
		print("Please Provide A PATH !")
		ReadQRCode()
	
	
#Define the Start Function ; this will be our mini menu 	
def start():
	Start = input("Generate or Read QR Code ? (g/r) -> ")
	if (Start == 'g'): GenerateQRCode() #Call the Generate QRCODE Function
	elif (Start == 'r') : ReadQRCode()	#Call the Read QRCODE Function
	else : 
		print("Please Enter a valid Argument !")
		start()
	
start()	