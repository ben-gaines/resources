# migrate_foia_sba_loans.py

import os
import sqlite3
import pandas as pd

# ------------------------------------------------- #
# Up-front notes
# ------------------------------------------------- #

'''
https://data.sba.gov/dataset/7-a-504-foia/resource/
c71ba6cf-b4e0-4e60-98f0-48aeaf4c6460
'''

# ------------------------------------ #
# Delete the DB if it exists
# ------------------------------------ #

if os.path.exists("foia_sba_loans.db"):
    os.remove("foia_sba_loans.db")

# ------------------------------------ #
# Make the db
# ------------------------------------ #

db = sqlite3.connect('foia_sba_loans.db')
cursor = db.cursor()
cursor.close()
db.close()

# define list of urls
foia_csv_url_list = [
    'https://data.sba.gov/dataset/0ff8e8e9-b967-4f4e-987c-6ac78c575087/resource/e8023bd1-7d8e-4bd2-8346-47cb6b367beb/download/foia-504-fy2010-present-asof-220331.csv',
]

# ------------------------------------ #
# Make eidl table function
# ------------------------------------ #

def create_foia_sba_loans_table(csv_link_list:list):
    
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

        conn = sqlite3.connect('foia_sba_loans.db', check_same_thread=False)
        df.to_sql(name='foia_sba_loans', con=conn, if_exists='append', index=False)  

# ------------------------------------ #
# Run the ppp migration function
# ------------------------------------ #

create_foia_sba_loans_table(foia_csv_url_list)

print(' ')
print('--------------------------------------')
print('foia sba loan migration complete')
print('--------------------------------------')