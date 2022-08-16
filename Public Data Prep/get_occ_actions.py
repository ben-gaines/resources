# get_occ_actions.py

# ------------------------------------ #
# Notes and resources for occ scraping
# ------------------------------------ #

# occ robots.txt
# https://occ.gov/robots.txt
# Only Applebot is disallowed from crawling.
# Always check the robots.txt file for
# updates before runnign this script to 
# be sure their terms haven't changed

# ------------------------------------ #
# Imports
# ------------------------------------ #

from bs4 import BeautifulSoup
import requests
from bs4.element import Comment
import sqlite3
import pandas as pd
import requests
import os
import json
import time
import re

def create_occ_db():

    # ------------------------------------ #
    # Delete the DB if it exists
    # ------------------------------------ #

    if os.path.exists("db_occ.db"):
        os.remove("db_occ.db")

    # ------------------------------------ #
    # Make the db
    # ------------------------------------ #

    db = sqlite3.connect('db_occ.db')
    cursor = db.cursor()
    cursor.close()
    db.close()

    # ------------------------------------ #
    # Make and insert the dataframe
    # ------------------------------------ #

    # make the list of all character combos for the url
    list_0 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    char_list = []
    for char_0 in list_0:
        for char_1 in list_1:
            char_set = char_0+char_1
            char_list.append(char_set)

    # query each character set and continue while pagination is true
    for char_set in char_list:

        try:

            # ------------------------------------ #
            # Make the DataFrame
            # ------------------------------------ #

            # scrape the site
            url = f'https://apps.occ.gov/EASearch/?Search={char_set}&Category=&ItemsPerPage=1000&Sort=&AutoCompleteSelection='
            df_list = pd.read_html(url)
            df = df_list[0]
            df.columns = df.columns.droplevel(0)

            # rename the column titles to remove spaces and camelcase
            column_titles = [
                'institution_bank_name',
                'charter_number',
                'company',
                'individual',
                'city_and_state',
                'type',
                'amount',
                'date_start',
                'start_doc',
                'date_close',
                'close_doc',
                'docket_number'
            ]
            df.columns = column_titles

            # print check
            print(char_set)
            print(' ')
            print(df.head())
            print(' ')
        
            # ------------------------------------ #
            # Insert data to db 
            # ------------------------------------ #

            conn = sqlite3.connect('db_occ.db', check_same_thread=False)
            df.to_sql(name='occ', con=conn, if_exists='append', index=False)

        except:

            print(f'No data for: {char_set}')
            continue

    # ------------------------------------ #
    # Make the virtual table
    # ------------------------------------ #

    headers = ''
    for title in column_titles:
        headers += title
        headers += ','

    conn.execute(f'''
    CREATE VIRTUAL TABLE v_occ
    USING FTS5 (
            {headers[:-1]}
        )
    ;
    '''
    )

    conn.execute(f'''
    INSERT INTO v_occ (
            {headers[:-1]}
        )

    SELECT DISTINCT {headers[:-1]}
     FROM occ
     ;
     '''
    )

    conn.commit()

    conn.execute('''DROP TABLE occ;''')

    conn.execute('''VACUUM;''')

    # ------------------------------------ #
    # Close the database
    # ------------------------------------ #

    conn.close()

    # ------------------------------------ #
    # print statement
    # ------------------------------------ #

    print(' ')
    print(len(df))
    print(' ')
    print('--------------------------------------------')
    print('--------------------------------------------')
    print(' OCC Actions Database Build Complete  ')
    print('--------------------------------------------')
    print('--------------------------------------------')

# ------------------------------------ #
# Execute the function
# ------------------------------------ #

create_occ_db()