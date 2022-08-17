# migratre_eidl_loans.py

import os
import sqlite3
import pandas as pd

# ------------------------------------------------- #
# Up-front notes
# ------------------------------------------------- #

'''
The eidl data has to be downloaded as a zip file from the 
below link and placed into the repo first. Once this is 
done running, delete the csv files to save space.

https://data.sba.gov/dataset/d158e867-cf27-49dd-b6c8-fa8df098e394/
resource/28563b11-99a1-40a2-aa80-c446a181e231/download/
april-2021-delivery-of-eidl-data-through-november-2020.zip

(Note: the link is broken into three lines here)
'''

# ------------------------------------ #
# Delete the DB if it exists
# ------------------------------------ #

if os.path.exists("eidl_loans.db"):
    os.remove("eidl_loans.db")

# ------------------------------------ #
# Make the db
# ------------------------------------ #

db = sqlite3.connect('eidl_loans.db')
cursor = db.cursor()
cursor.close()
db.close()

# define list of urls
eidl_csv_url_list = [
    'DATAACT_EIDL_LOANS_20200401-20200609.csv',
    'DATAACT_EIDL_LOANS_20200610-20200625.csv',
    'DATAACT_EIDL_LOANS_20200626-20200723.csv',
    'DATAACT_EIDL_LOANS_20200724-20201115.csv',
    'DATAACT_EIDL_LOANS_DMCS2.0.csv'
]

# ------------------------------------ #
# Make eidl table function
# ------------------------------------ #

def create_eidl_loans_table(csv_link_list:list):
    
    for link in csv_link_list:

        # ------------------------------------ #
        # Prep the dataframe
        # ------------------------------------ #

        # print check (optional)
        print(link)

        # create a dataframe to read in the csv 
        df = pd.read_csv(link, error_bad_lines=False)
        df = df.astype(str)
        
        # rename the column titles to remove spaces and camelcase
        column_titles = []
        for title in df.columns:
            column_titles.append(title.replace(' ','_').replace('-','_').replace(',','').replace('.','').replace('/','_').replace('(','').replace(')','').lower())
        df.columns = column_titles

        # ------------------------------------ #
        # Insert data to db 
        # ------------------------------------ #

        conn = sqlite3.connect('eidl_loans.db', check_same_thread=False)
        df.to_sql(name='eidl_loans', con=conn, if_exists='append', index=False)  

# ------------------------------------ #
# Run the ppp migration function
# ------------------------------------ #

create_eidl_loans_table(eidl_csv_url_list)

print(' ')
print('--------------------------------------')
print('eidl loan migration complete')
print('--------------------------------------')