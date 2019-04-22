# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:31:23 2019

@author: ryan_
"""

import pyrebase

apiKey = "AIzaSyAb28rqWCl_T67ek3RbObnPYLwYS1z5S4Q"
URL = "https://peoplecounter-7f1ec.firebaseio.com"
authDomain = "peoplecounter-7f1ec.firebaseapp.com"
storageBucket = "peoplecounter-7f1ec.appspot.com"

config = {"apiKey": apiKey,"databaseURL": URL, "authDomain":authDomain ,"storageBucket":storageBucket}

firebase = pyrebase.initialize_app(config)



#Possible problem
#1. we keep getting auth domain error

#DATABASE writing

#child()
# use to build path to your data
#initially we need ot build our child nodes first


#Data consideration
#Remember when uploading data into a child, it is in a dictionary format

#push()
# creates a timestamp key on your data, then pushes it to the right child

#set()
#pushes data to child without timestamp key

#update()
#update an existing entry of a child

#remove()
#to remove an existing entry

#DATABASE retrieval

#get()
#this returns data from a path
# this function needs to be called first before use val() or key()
# data needs to be stored in a variable, the data stored is a dictionary

#key()
#gets all the possible key of that child

#val()
#gets all the values of that child

#each()
#returns a list of objects which you can iterate through and call val() and key()

#stream()
# you can listen to any changes of your data with stream() method
# Does this mean we can see any change in that child node?
# Do not fully understand.
# what can i use stream for?

db = firebase.database()

db.child("LED/Yellow").update({"Room 1": 100})
val = db.child("LED/Yellow/Room 1").get()
valc = val.val()
print(valc)
    
