# get_finra_barred_brokers.py

import sqlite3
import pandas as pd
import os

def create_finra_db():

    # define list of finra urls
    finra_url_list = [
        'https://www.finra.org/rules-guidance/oversight-Oversight%20&%20Enforcement/individuals-barred-finra',
        'https://www.finra.org/rules-guidance/oversight-Oversight%20&%20Enforcement/individuals-barred-finra/b',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/c',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/d',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/e',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/f',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/g',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/h',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/i',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/j',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/k',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/l',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/m',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/n',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/o',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/p',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/q',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/r',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/s',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/t',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/u',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/v',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/w',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/x',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/y',
        'https://www.finra.org/rules-guidance/oversight-enforcement/individuals-barred-finra/z',
    ]

    # ------------------------------------ #
    # Delete the DB if it exists
    # ------------------------------------ #

    if os.path.exists("db_finra.db"):
        os.remove("db_finra.db")

    # ------------------------------------ #
    # Make the db
    # ------------------------------------ #

    db = sqlite3.connect('db_finra.db')
    cursor = db.cursor()
    cursor.close()
    db.close()

    # ------------------------------------ #
    # Make the dataframe
    # ------------------------------------ #

    for finra_url in finra_url_list:
        df_in_list = pd.read_html(finra_url)
        df = df_in_list[0]

        # rename the column titles to remove spaces and camelcase
        column_titles = []
        for title in df.columns:
            column_titles.append(title.replace(' ','_').replace('-','_').replace(',','').replace('.','').replace('/','_').replace('(','').replace(')','').lower())
        df.columns = column_titles

        # make a formatted string of the column headers for later use
        headers = ''
        for title in column_titles:
            headers += title
            headers += ','  

        # ------------------------------------ #
        # Insert data to db 
        # ------------------------------------ #

        conn = sqlite3.connect('db_finra.db', check_same_thread=False)
        df.to_sql(name='finra', con=conn, if_exists='append', index=False)

    # ------------------------------------ #
    # Make the virtual table
    # ------------------------------------ #

    conn.execute(f'''
    CREATE VIRTUAL TABLE v_finra
    USING FTS5 (
            {headers[:-1]}
        )
    ;
    '''
    )

    conn.execute(f'''
    INSERT INTO v_finra (
            {headers[:-1]}
        )

    SELECT DISTINCT {headers[:-1]}
     FROM finra
     ;
     '''
    )

    conn.commit()

    conn.execute('''DROP TABLE finra;''')

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
    print(' FINRA Database Build Complete  ')
    print('--------------------------------------------')
    print('--------------------------------------------')

# create_finra_db()








