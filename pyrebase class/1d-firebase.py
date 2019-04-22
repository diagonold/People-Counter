# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:49:11 2019

@author: ryan_sacatani
Firebase realtime database 
    suitable for application
    grabbing data and editing data on the cloud
    minimum authentication if we add a security measure
    
We will first go through the functions available on firebase 
Then we will apply these functions in a class that will make our firebase code, usable on our app
"""
#%%
"""
Initializing the SDK(software developement kit)
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# fetch the service account key JSON file contents
cred = credentials.Certificate('peopleCounter-adminSDK.json')
# initialize the app with a service account, granting admin priveleges
firebase_admin.initialize_app(cred)

print("hello")

ref = db.reference('/')

#set()
# using set method, we create database with this. The structure of the file will be the same as the said database
ref.set({
        'boxes': 
            {
                'box001': {
                    'color': 'red',
                    'width': 1,
                    'height': 3,
                    'length': 2
                },
                'box002': {
                    'color': 'green',
                    'width': 1,
                    'height': 2,
                    'length': 3
                },
                'box003': {
                    'color': 'yellow',
                    'width': 3,
                    'height': 2,
                    'length': 1
                }
            }
        })

#



