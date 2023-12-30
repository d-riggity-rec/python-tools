'''
This a sample project to demonstrate usage of MySQL connector in Python.
This project illustrates a script that can parse through a file directory and mulitple files to extract
data, manipulate it, and push it into a MySQL database.
The data in this project contains purely fictitious data, likeness is taken from the Naruto anime
series for fun and learning purposes.
'''

import sys
sys.path.append('c:/scripts/python')

import os.path
import pandas as pd
import dm_mods as dm   # <-------- disregard squiggly here, tis import works because of the sys path append
import random
import calendar
import mysql.connector

################################################
'''
MYSQL Set-up 
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="90844996",   # <-- use this to access a database when making the conneection
  database="naruto_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE 2021reports(id INT AUTO_INCREMENT PRIMARY KEY, date INT, team INT, mission_rank VARCHAR(255), enemy VARCHAR(255), grade VARCHAR(255), bonus VARCHAR(255))")
# mycursor.execute("DESCRIBE 2020reports")
# mydb.commit()

# for x in mycursor:
#     print(x)

#################################################

#################################################
'''
Naruto Directory Stuff
'''

hr_201912 = 'C:/scripts/naruto_trends/hidden_leaf/hokage_report_2019/hiddenLeaf201912.csv'
h_reports_2019 = 'C:/scripts/naruto_trends/hidden_leaf/hokage_report_2019/'
h_reports_2020 = 'C:/scripts/naruto_trends/hidden_leaf/hokage_report_2020/'
h_reports_2021 = 'C:/scripts/naruto_trends/hidden_leaf/hokage_report_2021/'
sensei_fle = 'C:/scripts/naruto_trends/teams/senseis.csv'
team_mems = 'C:/scripts/naruto_trends/teams/ninja_teams.csv'
#################################################

################################################
'''
Dataframe & Database Workout
'''

hdrs = ["Team","Mission Rank","Enemy","Perf Grade","Extra Bonus"]

hl_dict = {
   "Date":[],
   "Team":[],
   "Mission Rank":[],
   "Enemy":[],
   "Perf Grade": [],
   "Extra Bonus":[]
}

hl_df = pd.DataFrame(hl_dict)

# print(hl_df)


for yr_mo in os.listdir(h_reports_2021):
    yr_mo_fle = h_reports_2021 + yr_mo
    df = dm.cleanCSV(yr_mo_fle)
    dt_str = yr_mo[10:16]
    df['Date'] = dt_str
    # print(dt_str)
    frames = [hl_df,df]
    # hl_df = pd.concat(frames).reset_index(drop=True) # this is how WEEee doOOOoooo it.. 
    hl_df = pd.concat(frames,ignore_index=True)  # this is how ul does it !

# print(hl_df)

hl_len = len(hl_df)
# print(hl_len)
# all_dt = hl_df["Date"]
# last_dt = hl_df["Date"][9]
# print(all_dt)

# print(last_dt)

colcnt = 1
for idx in range(hl_len):
    dt = hl_df["Date"][idx]
    # tm = str(int(hl_df['Team'][idx]))
    tm = int(hl_df['Team'][idx])
    mr = hl_df['Mission Rank'][idx]
    en = hl_df['Enemy'][idx]
    pg = hl_df['Perf Grade'][idx]
    eb = hl_df['Extra Bonus'][idx]
    dat_arr = [dt,tm,mr,en,pg,eb]
    # dat_arr = dat_arr.join(',')
    # print(dat_arr)
    # print(dt,tm,mr,en,pg,eb,"data type:",type(pg))
    sql = "INSERT INTO 2021reports VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = [(colcnt,dt,tm,mr,en,pg,eb)]
    mycursor.executemany(sql,val)
    colcnt = colcnt + 1
    print(dt,tm,mr,en,pg,eb)
    # print(dt)
mydb.commit()

# print(mydb)
#######################################################