#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
Setup Redmine server access.
"""
# To disable Insecure Request Warnings, in case of requests={'verify': False} is used
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
Launches a basic GUI to get user inputs.
"""
# Dialog boxes to get the test parameters
import easygui

# API_key = easygui.enterbox("KEY ? (copy/paste from My Account")
API_key = "445795a91e0c88948dc333817d8e59492fc0a4bc"

"""
Redmine access to Redmine servers : please update the "key" parameter with your private access API key.
"""
# 1a. = Connect to the dummy site bitnami (OCJ)
# 1b. = Connect to the xifu-redmine site
from redminelib import Redmine
# 1a. redmine = Redmine('http://127.0.0.1/redmine', key = 'e3191b442153f5e28c3ba7ec3c8e7a5d9583c038', requests={'verify': False})
redmine = Redmine('https://xifu-redmine.irap.omp.eu', key = API_key, requests={'verify': False})

# Get the issues
issues = redmine.issue.all(sort='category:desc', include=['relations', 'attachments'])
issues = redmine.issue.all(sort='category:desc', include=['relations', 'attachments'])

print(issues)
issue = issues.get(98)
issue = redmine.issue.get(98, include=['children', 'journals', 'watchers', 'attachments'])
print("issue=", issue)

print("journals", issue.journals[0])
print("attachments", issue.attachments[0])

for jour in (issue.journals):
    print(jour)

for wat in (issue.watchers):
    print(wat)

for attach in (issue.attachments):
    print(attach)

issues = redmine.issue.all()
#issue = redmine.issue.get(98)

#issues = redmine.issue.all()

# 2. Get a valid path on disk
import os.path
issuepath = os.path.normpath("D:/S.O.F.T.S/ATHENA/TEMP")

issues.export('pdf', savepath=issuepath, filename='issue1.pdf')
issues.export('csv', savepath=issuepath, filename='issues.csv')


print("issuepath = ", issuepath)


print("Issues exported...")
