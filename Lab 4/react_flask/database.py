import os
import json


class dataB(object):
    '''
    Useage: [[ NEEDS UPDATING ]]
    python
    from newdb import dataB
    myB = dataB()
    myB.create(key,value)
    myB.read(key)
    myB.update(key,value)
    myB.delete(key)
    myB.showAll()
    myB.Write()
    myB.read_written()
    '''

    # allows naming of database
    def __init__(self):
        self.location = './database.json'
        self.db = {}

    def create(self, value):
        key = str(1) if len(self.db) < 1 else str(
            max([int(i) for i in self.db.keys()])+1)
        self.db[key] = value
        return {key: self.db[key]}

    def read(self, key):
        if key == 'all':
            return self.db
        if key in self.db.keys():
            return {key: self.db[key]}
        else:
            return("not in db"+str(type(key))+str(type(list(self.db.keys())[0])))

    def update(self, id, value):
        if id in self.db.keys():
            self.db[id] = value
            return self.db
        else:
            return("key is in db.keys?:" + str(id in self.db.keys()))

    def delete(self, key):
        if str(key) in self.db.keys():
            del self.db[str(key)]
            return self.db
        else:
            return("key is in db.keys?:" + str(key in self.db.keys()))

    def upload(self):
        with open('database.db', 'w') as json_file:
            json.dump(self.read('all'), json_file)
        return self.db

    def download(self):
        self.db = json.load(open('./database.db', 'r'))
        return self.db