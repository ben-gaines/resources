# get_ofac_sanctions.py

import sqlite3
import pandas as pd
import os

def create_ofac_sanctions_db():

    # ------------------------------------ #
    # Delete the DB if it exists
    # ------------------------------------ #

    if os.path.exists("db_ofac_sanctions.db"):
        os.remove("db_ofac_sanctions.db")    

    # ------------------------------------ #
    # Make the db
    # ------------------------------------ #

    db = sqlite3.connect('db_ofac_sanctions.db')
    cursor = db.cursor()
    cursor.close()
    db.close()

    # ------------------------------------ #
    # Make the dataframe
    # ------------------------------------ #

    # Create a Dataframe to Read in the CSV 
    primary_names_df = pd.read_csv('https://www.treasury.gov/ofac/downloads/consolidated/cons_prim.csv',header = None)
    alt_names_df = pd.read_csv('https://www.treasury.gov/ofac/downloads/alt.csv',header = None)
    address_df = pd.read_csv('https://www.treasury.gov/ofac/downloads/add.csv',header = None)
    comments_df = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn_comments.csv',header = None)
    ofac_df = pd.concat([
        primary_names_df,
        alt_names_df,
        address_df,
        comments_df,
    ])

    # TODO: Even though we are using FTS, add the actual column names in here

    ofac_df.columns = [
        'col_0',
        'col_1',
        'col_2',
        'col_3',
        'col_4',
        'col_5',
        'col_6',
        'col_7',
        'col_8',
        'col_9',
        'col_10',
        'col_11',
    ]
    
    # ------------------------------------ #
    # Insert data to db 
    # ------------------------------------ #

    conn = sqlite3.connect('db_ofac_sanctions.db', check_same_thread=False)
    ofac_df.to_sql(name='ofac_sanctions', con=conn, if_exists='append', index=False)

    # ------------------------------------ #
    # Make the virtual table
    # ------------------------------------ #

    conn.execute('''
    CREATE VIRTUAL TABLE v_ofac_sanctions
    USING FTS5 (col_0,
        col_1,
        col_2,
        col_3,
        col_4,
        col_5,
        col_6,
        col_7,
        col_8,
        col_9,
        col_10,
        col_11)
    ;
    '''
    )

    conn.execute('''
    INSERT INTO v_ofac_sanctions(col_0,
        col_1,
        col_2,
        col_3,
        col_4,
        col_5,
        col_6,
        col_7,
        col_8,
        col_9,
        col_10,
        col_11)

    SELECT col_0,
        col_1,
        col_2,
        col_3,
        col_4,
        col_5,
        col_6,
        col_7,
        col_8,
        col_9,
        col_10,
        col_11
    FROM ofac_sanctions
    ;
    '''
    )

    conn.commit()

    conn.execute('''DROP TABLE ofac_sanctions;''')

    conn.execute('''VACUUM;''')

    # ------------------------------------ #
    # Close the database
    # ------------------------------------ #

    conn.close()

    # ------------------------------------ #
    # print statement
    # ------------------------------------ #

    print(' ')
    print(len(ofac_df))
    print(' ')
    print('--------------------------------------------')
    print('--------------------------------------------')
    print(' OFAC Sanctions List Database Build Complete  ')
    print('--------------------------------------------')
    print('--------------------------------------------')

# ------------------------------------ #
# Execute the function
# ------------------------------------ #

create_ofac_sanctions_db()