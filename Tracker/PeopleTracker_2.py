# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:08:40 2019

@author: dingx
"""

import cv2
import numpy as np
import time
from pythymiodw import *
from time import sleep
import datetime




class CentroidTracker(object):
    def __init__(self, maxFrames = 300, Dist = 2000, seats = 10):
        self.new = [] #list to help us check whether newcentroids are  added to the oldCentroid
        self.Centroids = {}
        self.lostCentroids = {}
        self.maxFrames = maxFrames
        self.objectID = 0
        self.Dist = Dist
        
        self.availability = seats
        self.centroidPrevPosition = {}
        self.currentTime = 0
        self.previousTime = time.time()
        
        
    def register(self,centroid):
        #takes in a tuple of centroid that should be detected
        self.Centroids[self.objectID] = centroid
        self.lostCentroids[self.objectID] = 0 # here we initialize the number of frames for each objectID that has been lost
        self.centroidPrevPosition[self.objectID] = centroid
        self.objectID +=1 # increases the name of the object every time it increases
        
    def deregister(self, centroidID):
        #takes in a object ID that should no longer be included
        del self.Centroids[centroidID] #deletes from the lost centroid and the old centroid list permanently
        del self.lostCentroids[centroidID]
        del self.centroidPrevPosition[centroidID]
        
    def calcDistance(self, newCentroid , oldCentroid):
        #calculates euclidean distance between 
        return ((newCentroid[0]-oldCentroid[0])**2 + (newCentroid[1]-oldCentroid[1])**2)**0.5
    
#    def speed(self, centroidID):# calculates the speed of a centroid within the next frame
#        self.currentTime = time.time()
#        timePassed = self.currenTime - self.previousTime
#        self.previousTime = self.currentTime
#        xDistance =  self.oldCentroids[centroidID] - self.centroidPrevPosition[centroidID]
#        return float(xDistance/ timePassed)
    
    def update(self, newCentroids):
        
        #inputs: list of list, where each inner list is a centroid with values(cx, cy, x, y, w, h)
        #checks if the new centroids are similar to the close one,
        #if yes update the oldcentroid dictionary with the new values of the centroid
        #output: returns oldcentroid list, which is the list of object in format(cx,cy, x, y,w,h) that should be drawn on the frame
        
        #special case, registering nth for no frame
        if newCentroids == [(-1,-1)]:
            if len(self.Centroids) != 0:
                for objectID, frames in self.lostCentroids.items():
                    self.lostCentroids[objectID] += 1
                    #print('added 1 frame')
                    
                    if frames >= self.maxFrames:
                        self.deregister(objectID)
                    return self.Centroids
            else:
                return self.Centroids
        #case0 , the oldCentroid is zero:
        #Checking for error in case first centroid is (0,0)
        if len(self.Centroids) == 0:
            for newCentroid in newCentroids:
                self.register(newCentroid)
                print('REGISTERED',newCentroid)
                
                
        #case1:new centroid is close to old centroids or not
        self.framescounter = 0      #Current ObjectID of detected frame
        self.currentobject = 0      #Current ObjectID of detected object
        for newCentroid in newCentroids:
            for objectID, Centroid in list(self.Centroids.items()):
                #print('NEW',newCentroid,Centroid)
                dist1 = self.calcDistance(newCentroid , Centroid)
                #print('DISTANCE',dist1)
                if dist1 < self.Dist:
                    self.currentobject = objectID
                    #we should find the objectID with the closest distance then we use 
                    #that object and we update its value
                    self.Centroids[objectID] = newCentroid          #newcentroid now replaces the value for the objectID in Centroids dic
                    self.centroidPrevPosition[objectID] = Centroid  #oldcentroid added into the prevcentroid dic
                    self.framescounter = objectID
                    self.lostCentroids[objectID] = 0                #reset the frames lost
                    
                    if self.centroidPrevPosition[objectID][1] >= boundary1[1] and self.Centroids[objectID][1] < boundary1[1]:
                        self.availability += 1
                    elif self.Centroids[objectID][1] >= boundary1[1] and self.centroidPrevPosition[objectID][1] < boundary1[1]:
                        self.availability -= 1
     
                    #currentTime = datetime.datetime.now()
                    #currentMinute = currentTime.minute
                    break
                    # add value of n to a newC list
                    # this will be used to check whether the centroid in the oldCentroids still exist 
                
                else:
                    #if they are not close then new object name should be added
                    self.register(newCentroid)
                    
        #case2: the detected object ID != other objectID
        #add frames to other non-detected objectIDS
        for objectID, frames in self.lostCentroids.items():
            if self.framescounter != objectID:
                self.lostCentroids[objectID] += 1
            
            if frames >= self.maxFrames:
                self.deregister(objectID)
                
            #for newCentroid in newCentroids:
            #case 3: they were lost but now found in the newCentroids 
#            #        update the values of the lost centroid in the oldCentroids class
#                dist2 = self.calcDistance(self.oldCentroids[objectID],newCentroid)
#                if dist2 < self.thresholDist:
#                    self.oldCentroids[objectID] = newCentroid
            
        return self.Centroids

class Point:
    def __init__(self, point1=(0,200), point2=(790,200)):
        self.point1 = point1
        self.point2 = point2
    
    def __call__(self):
        return self.point1, self.point2

#%%INSTANTIATE YOUR GLOBAL VARIABLES FIRST
#head_cascade = cv2.CascadeClassifier('HS.xml')
cap = cv2.VideoCapture(0)
#head_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
ct = CentroidTracker()
boundary = Point()
area_of_detection = 20000
subtractor = cv2.createBackgroundSubtractorMOG2(history = 80 , varThreshold = 15 ,detectShadows = False)
#%%
counter = 0
while cap.isOpened():
    _,frame = cap.read()   #Read every frame
    mask = subtractor.apply(frame)
    kernel = np.ones((3,3), np.uint8)
	
    mask = cv2.erode(mask, kernel, iterations = 1)
    mask = cv2.dilate( mask, kernel, iterations = 3)
    contours, _ =  cv2.findContours( mask ,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #heads = head_cascade.detectMultiScale(gray)
    newCentroid = 0
    #Start line boundary
    boundary1, boundary2 = boundary()
    boundary2 = (790,200)
    cv2.line(frame, boundary1, boundary2, (0,0,255), 2)
    cv2.putText(frame, "Entry Line", (350,250), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), lineType=cv2.LINE_AA)
    #print(heads)
    if contours ==():
        newCentroid = [(-1,-1)]
        ct.update(newCentroid)
    for contour in contours:
        #print(contour)
        #print(head)
        x,y,w,h = cv2.boundingRect(contour)
        if w*h > area_of_detection:
            cx = (x+w)/2
            cy = (y+h)/2
            newCentroid = [(cx,cy)]
            ct.update(newCentroid)
            counter += 1
            label = 'objectID ' + str(ct.currentobject)
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255),2)
            cv2.putText(frame, label, (int(cx),int(cy)), font, 3, (0,255,0), 2, lineType=cv2.LINE_AA)
            #roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        elif w*h < 20000:
            newCentroid = [(-1,-1)]
            ct.update(newCentroid)
        #print('detected',counter)
        #print('points',ct.Centroids)
        #print('prev',ct.centroidPrevPosition)
        #print('lost',ct.lostCentroids)
    
    availability = 'Availabile seats: '+str(ct.availability)
    cv2.putText(frame, availability, (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2, lineType=cv2.LINE_AA)        
    cv2.imshow('frame',frame)
 
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()

