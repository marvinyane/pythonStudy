#! /usr/bin/python

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

lists = c.execute("select * from tbl1")

for l in lists:
    print l



