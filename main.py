#!/usr/bin/env python

"""
Imports
"""
import sys
import argparse
import requests
import json

#-----------
# Functions
#-----------

def isConnected():
    try:
        r = requests.get('http://localhost:4400/rest/2.0/application/info')
        print r.json()['buildNumber']
        return True
    except ValueError:
        return False

def getAssetTypes():
    try:
        r = requests.get('http://localhost:4400/rest/2.0/assetTypes', auth=('Admin', 'admin'))
        print r.json()['total']
        return True
    except ValueError:
        return False

def createUser():

    headers = {'Content-Type' : 'application/json'}
    payload = {"userName": "elliot","firstName": "Elliot","lastName": "Dines","emailAddress": "email@email.com","gender": "MALE"}
    payload = json.dumps(payload)
    r = requests.post('http://localhost:4400/rest/2.0/users',headers=headers, data=payload, auth=('Admin','admin'))
    print r.json()        
    return True

#-----------
# Main
#-----------

print isConnected()

print getAssetTypes()

print createUser()
