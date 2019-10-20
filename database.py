# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:20:26 2019

@author: DSC
"""

import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('TestDB.db')  
c = conn.cursor()
read_clients = pd.read_csv(r'da.csv')
read_clients.to_sql('data', conn, if_exists='append', index = False)
c.execute("SELECT * FROM data WHERE type='wet'")
#c.execute('SELECT * FROM data')
#names = [description[0] for description in c.description]
#info = '''wiki-calculuswithmrjames.wikispaces.com'''
#
#
#c.execute("UPDATE data SET downloads=downloads+1 WHERE identifier='wiki-calculuswithmrjames.wikispaces.com'")
#c.execute("SELECT * FROM data WHERE identifier='"+info+"'")
a = c.fetchall()
print(a)
c.execute("SELECT * FROM data WHERE type='dry'")
a = c.fetchall()
print(a)
#c.fetchall()
#c.execute('SELECT * FROM data WHERE TITLE=3')
#c.execute('SELECT * FROM data WHERE downloads=7')