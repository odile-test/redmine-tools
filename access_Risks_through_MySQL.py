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

API_key = "e3191b442153f5e28c3ba7ec3c8e7a5d9583c038" # odile_adm account

# on importe le module mysql
import mysql.connector

# MySQL : 3306
mydb = mysql.connector.connect(
  host="localhost",
  user="guest",
  password="prunier64",
  db="bitnami_redmine"
)

print(mydb)

# Show Tables
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 

# Select from Table Risks
mycursor.execute("SELECT * FROM risks")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Select from Table Projects
mycursor.execute("SELECT * FROM projects")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Select columns from Table Risks
mycursor.execute("SELECT * FROM risks WHERE 1")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Select project_id from Table Risks
mycursor.execute("SELECT * FROM risks where project_id='2'")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# INNER JOIN des tables risks et projects pour trouver à quel projet appartient le risque
mycursor.execute("SELECT projects.name ,risks.description, risks.subject FROM risks INNER JOIN projects ON risks.project_id = projects.id")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# INNER JOIN des tables risk_issues et risks pour trouver toutes les issues liées à un risque
mycursor.execute("SELECT risks.description, risks.subject, issues.subject FROM risk_issues INNER JOIN risks ON risk_id = risks.id INNER JOIN issues ON issue_id = issues.id")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
