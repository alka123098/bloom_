import useful_functions
import cv2 as cv
import handmodule as htm
import mediapipe as mp
import time
import raindrop_pattern_generator
import arduino_sender
z_axis_values=[]
useful_functions.list_initializator(z_axis_values,20)
time_of_action=[]
useful_functions.list_initializator(time_of_action,20)
cap = cv.VideoCapture(1)
cap.set(3,680)
cap.set(4,480)
detector = htm.HandDetector(detectionCon=0.8,maxHands=1)
variablecount =0
routemap=[[15],[11,14,10],[13,9,5,6,7],[12,8,4,0,1,2,3]]
buttonList=[]
traversal =[]
width=80
height=80
xspan =40
yspan =40
array_var=0
z_max=0
z_min=0

Dict={0:6,1:10,2:13,3:15,4:3,5:7,6:11,7:14,8:1,9:4,10:8,11:12,12:0,13:2,14:5,15:9}


#temX=0
#temY=0
#dummy1=0
variablecount=0

state =0
t =time.time()
time.sleep(1)
t1=time.time()
matrix=[]
i=0
useful_functions.list_initializator(matrix,16)


def runner(t,z_axis_values,time_of_action,array_var,state):
    while True:
        success,img = cap.read()
        #print(success)
        img=cv.flip(img,1)
        hands,img=detector.findHands(img)
        if hands:
            lmList = hands[0]['lmList']
            x,y,z=lmList[8]
            e18=lmList[18]
            e20=lmList[20]
            e19=lmList[19]
            e16=lmList[16]
            e10=lmList[10]
            e12=lmList[12]
            e6=lmList[6]
            e8=lmList[8]
            e2=lmList[2]
            e4=lmList[4]
            
            
            
            
               
                
            if lmList[8][1]<lmList[6][1] and lmList[12][1]<lmList[10][1] and lmList[16][1]<lmList[14][1] and state==0:
                
                if time.time()>time_of_action[array_var-1] + 0.2:
                    z_axis_values[array_var]=abs(lmList[8][2])
                    time_of_action[array_var]=time.time()
                    if array_var<15:
                        array_var+=1
                    else :
                        array_var=0
                    if max(z_axis_values)>10:
                        z_max=max(z_axis_values)
                        z_min=min(z_axis_values)
                if abs(z_max-z_min)>50:
                    print(z_max,z_min)
                    t=time.time()
                    state=1
                    print("success")
                    raindrop_pattern_generator.raindrop()
                    zero_matrix=[]
                    useful_functions.list_initializator(zero_matrix)
                    arduino_sender.sendData(zero_matrix)
                   
                    
                
                   
           
           

               


                
            
        cv.imshow("image",img)
        cv.waitKey(1)
runner(t,z_axis_values,time_of_action,array_var,state)

