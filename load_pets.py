#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Ten - DBs and SQL"""

import sqlite3 as lite
import sys

persons = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
)

pets = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)

try:
    con = lite.connect('pets.db')

    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS Persons;
        DROP TABLE IF EXISTS Pets;
        DROP TABLE IF EXISTS Ownership;
        CREATE TABLE Persons(Id INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Age INT);
        CREATE TABLE Pets(Id INTEGER PRIMARY KEY, Name TEXT, Breed TEXT, Age INT, Value INT);
        CREATE TABLE Ownership(OwnerID INTEGER, PetID INTEGER);
        """)

    cur.executemany('INSERT into Persons VALUES (?,?,?,?)', persons)
    cur.executemany('INSERT into Pets VALUES (?,?,?,?,?)', pets)
    cur.executemany('INSERT into Ownership VALUES (?,?)', person_pet)

    con.commit()

except lite.Error, e:

    if con:
        con.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
