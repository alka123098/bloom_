from mod import SerialObject
import time
import concurrent.futures
import asyncio
arduino = SerialObject("COM3")

time.sleep(3)




def sendData(matrix):
    
    #print(matrix)           
    arduino.sendData(matrix)    