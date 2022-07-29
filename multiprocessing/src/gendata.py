##########################################################
#                   Generator data
# gendata - has the functions to generate the fake data.
# The functions - make data return a dataframe pandas
# with data.:
#
# Author: @andvsilva - 2022-07-15
##########################################################

import random
import pandas as pd
import snoop
import feather
import time
import gc
import sys
import feather
import os

from faker import Faker
from varname import nameof
from icecream import ic

# faker object
fake = Faker()

number_of_clients = int(sys.argv[1])
jobNumber = int(sys.argv[2])

os.system(f'touch jobRunning{jobNumber}')
print(f"Starting job #{jobNumber}...")

#@snoop
def make_database():
    # client - transaction
    client_name = fake.name()
    id = random.randint(1000, 10000)
    value = random.random()*100
    date = fake.date_between(start_date='-90d', end_date='today') # 3 months ago!
    date_register = fake.date_between(start_date='-3y', end_date='today')

    name_cols = []
    name_cols.append(nameof(id))
    name_cols.append(nameof(client_name))
    name_cols.append(nameof(date))
    name_cols.append(nameof(date_register))
    name_cols.append(nameof(value))

    # fake database
    database = {f'id': id, 
                f'client_name': client_name,
                f'date': date,
                f'date_register': date_register,
                f'value': value
                }

    ## transaction
    # data - sell
    #print(f'id ....................: {id}')
    #print(f'client name............: {client_name}')
    #print(f'date...................: {date}')
    #print(f'date register..........: {date_register}')
    #print(f'value..................: {value}')

    return name_cols, database

#@snoop
def generate_fakedata(nrows):    

    irow = 1
    name_cols, database = make_database()
    df = pd.DataFrame(columns=name_cols)

    while(irow <= nrows):
        name_cols, database = make_database()
        df_database = pd.DataFrame([database])
        df = pd.concat([df, df_database], ignore_index=True)
        irow += 1

    return df
