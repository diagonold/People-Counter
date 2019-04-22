import pyrebase
import datetime


class FB(object):
    def __init__(self, apiKey="AIzaSyAA1AMe3MWLICtbaNs0YsNPEUgcnI8EOHE" , authDomain ="trial-5-42c84.firebaseapp.com",databaseURL ="https://trial-5-42c84.firebaseio.com" , storageBucket = "trial-5-42c84.appspot.com"):
        self.apiKey = apiKey
        self.authDomain = authDomain
        self.databaseURL = databaseURL
        self.storageBucket = storageBucket
        self.clock = str(datetime.datetime.now())
        self.hour =  int(self.clock[11:13])
        self.min = int(self.clock[14:16])
        self.sec = int(self.clock[17:19])
        self.config = {
      "apiKey": self.apiKey,
      "authDomain": self.authDomain,
      "databaseURL": self.databaseURL,
      "storageBucket": self.storageBucket}


    def update_node(self, nodes , updatedValue):
        path = ""
        for node in nodes:
            if node != nodes[-1]:
                path+= node
                path+= "/"        
        print(path)
        db.child(path).update({nodes[-1]:updatedValue})

    def retrieve_node(self, nodes):
        path = self.create_path(nodes)
        finalValue = db.child(path).get()
        return  finalValue.val()

    def create_path(self, nodes):
        path = ""
        for node in nodes:
            if node != nodes[-1]:
                path += (node + "/")
            else:
                path += node
        return path
        

    def update_hourly(self,nodes,nodeCurrent):
        pathToHistory = createPath(nodes)
        pathToCurrent =  createPath(nodeCurrent)
        
        current = db.child(pathToCurrent).get()
        currentVal =  current.val()
        node = db.child(path).get()
        nodeVal= node.val()
        #case 1: nodeVal is still empty
        #case 2: nodeVal already has 24 values
        if len(nodeVal) == 0:
            nodeVal.append(currentVal)
        elif len(nodeVal) == 24:
            if self.hour == 0 and self.min == 0 and self.sec ==0:
                nodeVal = []
                nodeVal.append(currentVal)
        else:
            if self.min == 0  and self.sec == 0:
                nodeVal.append(currentVal)

        db.child(pathToHistory).update({nodes[-1]:nodeVal})
        return "updated"

        
fb = FB()
firebase = pyrebase.initialize_app(fb.config)
db = firebase.database()
fb.update_node(["LED" ,"Yellow","Room 1"],  123)
print(fb.retrieve_node(["LED" ,"Yellow","Room 1"]))




                            
