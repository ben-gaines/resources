# get_ita_sanctions.py

import sqlite3
import pandas as pd
import requests
import os

def create_ita_db():

    # ------------------------------------ #
    # Delete the DB if it exists
    # ------------------------------------ #

    if os.path.exists("db_ita.db"):
        os.remove("db_ita.db")

    # ------------------------------------ #
    # Make the db
    # ------------------------------------ #

    db = sqlite3.connect('db_ita.db')
    cursor = db.cursor()
    cursor.close()
    db.close()

    # ------------------------------------ #
    # Make the dataframe
    # ------------------------------------ #

    r = requests.get('https://api.trade.gov/static/consolidated_screening_list/consolidated.json')
    data = r.json()
    ita_df = pd.DataFrame(data['results'])
    ita_df = ita_df.astype(str)
    
    # ------------------------------------ #
    # Insert data to db 
    # ------------------------------------ #

    conn = sqlite3.connect('db_ita.db', check_same_thread=False)
    ita_df.to_sql(name='ita', con=conn, if_exists='append', index=False)

    # ------------------------------------ #
    # Make the virtual table
    # ------------------------------------ #

    # TODO: make this dynamic from column headers in the dataframe

    conn.execute('''
    CREATE VIRTUAL TABLE v_ita
    USING FTS5 (
            name,
            alt_names,
            source,
            start_date,
            standard_order,
            source_list_url,
            id,
            addresses,
            end_date,
            federal_register_notice,
            remarks,
            source_information_url,
            type,
            ids,
            entity_number,
            dates_of_birth,
            citizenships,
            nationalities,
            places_of_birth,
            programs,
            title,
            country,
            license_policy,
            license_requirement,
            vessel_type,
            vessel_owner,
            vessel_flag,
            gross_tonnage,
            gross_registered_tonnage,
            call_sign
        )
    ;
    '''
    )

    conn.execute('''
    INSERT INTO v_ita (
            name,
            alt_names,
            source,
            start_date,
            standard_order,
            source_list_url,
            id,
            addresses,
            end_date,
            federal_register_notice,
            remarks,
            source_information_url,
            type,
            ids,
            entity_number,
            dates_of_birth,
            citizenships,
            nationalities,
            places_of_birth,
            programs,
            title,
            country,
            license_policy,
            license_requirement,
            vessel_type,
            vessel_owner,
            vessel_flag,
            gross_tonnage,
            gross_registered_tonnage,
            call_sign
        )

    SELECT  name,
            alt_names,
            source,
            start_date,
            standard_order,
            source_list_url,
            id,
            addresses,
            end_date,
            federal_register_notice,
            remarks,
            source_information_url,
            type,
            ids,
            entity_number,
            dates_of_birth,
            citizenships,
            nationalities,
            places_of_birth,
            programs,
            title,
            country,
            license_policy,
            license_requirement,
            vessel_type,
            vessel_owner,
            vessel_flag,
            gross_tonnage,
            gross_registered_tonnage,
            call_sign
    FROM ita
    ;
    '''
    )

    conn.commit()

    conn.execute('''DROP TABLE ita;''')

    conn.execute('''VACUUM;''')

    # ------------------------------------ #
    # Close the database
    # ------------------------------------ #

    conn.close()

    # ------------------------------------ #
    # print statement
    # ------------------------------------ #

    print(' ')
    print(len(ita_df))
    print(' ')
    print('--------------------------------------------')
    print('--------------------------------------------')
    print(' ITA Database Build Complete  ')
    print('--------------------------------------------')
    print('--------------------------------------------')

# ------------------------------------ #
# Execute the function
# ------------------------------------ #

create_ita_db()