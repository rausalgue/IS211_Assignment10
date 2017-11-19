#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Ten - DBs and SQL"""

import sqlite3 as lite
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--userId", help="Player Type",default=None)
args = parser.parse_args()

con = lite.connect('pets.db')

cur = con.cursor()

def getClientData(id):
    cur.execute('SELECT * from Persons where Id = ?', id)
    row = cur.fetchone()
    #print row
    #print row[1], row[2], ',', row[3], 'years old.'
    firstName = row[1]
    lastName = row[2]
    age = row[3]

    print firstName,lastName,',',age,'years old'

    cur.execute('SELECT * from Ownership where OwnerID = ?', id)

    rows = cur.fetchall()

    for row in rows:
        #print row[0]
        #print row[1]

        petID = row[1]
        #print petID
        cur.execute('SELECT * from Pets where Id = ?', str(petID))
        pet = cur.fetchone()
        petName = pet[1]
        petBreed = pet[2]
        petAge = pet[3]
        petExists = pet[4]

        if int(petExists) > 0:
            type = 'owns'
            func = 'is'
        else:
            type = 'owned'
            func = 'was'

        print firstName,lastName,type,petName,', a',petBreed,", that",func,petAge,'years old'


def main():
    print 'Welcome to Petco Database'

    userId = 0

    while int(userId) != -1:

        userId = args.userId if args.userId else raw_input("Please enter Client ID: ")

        #print 'UserID',userId

        if int(userId) > 0 and int(userId) < 5:
            print 'You have entered Client ID - ',userId
            getClientData(userId)
        else:
            print 'The Client ID supplied is not valid'

if __name__ == '__main__':
    main()
