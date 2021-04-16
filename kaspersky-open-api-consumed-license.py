#!/usr/bin/env python3
import requests
import base64
import urllib3
import json
import datetime
import sys
licenseid = sys.argv[1]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user64 = base64.b64encode('<username>'.encode('utf-8')).decode("utf-8")
password64 = base64.b64encode('<password>'.encode('utf-8')).decode("utf-8")
auth_headers = {'Authorization': 'KSCBasic user="' + user64 + '", pass="' + password64 + '"', 'Content-Type': 'application/json',}

tokenurl = 'https://<kaspersky-server-address>:13299/api/v1.0/Session.StartSession'
tokenbody = {}
tokenrequest = requests.post(tokenurl, headers=auth_headers, data=tokenbody, verify=False)
token = tokenrequest.json().get('PxgRetVal')
tokenheader = {'X-KSC-Session': token, 'Content-Type': 'application/json',}

licenseurl = 'https://<kaspersky-server-address>:13299/api/v1.0/LicenseKeys.GetKeyData'
licensebody = {"pKeyInfo": {'KLLIC_SERIAL': licenseid}}
licenserequest = requests.post(licenseurl, headers=tokenheader, data=json.dumps(licensebody), verify=False)
licensejson = licenserequest.json()
licenseconsumed = licensejson['PxgRetVal']['KLLIC_NHOSTS_ASCURRENT']
print(licenseconsumed)
