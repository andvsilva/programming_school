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

os.system('date')

# Pandas has a high consume of memory RAM usage
# release memory RAM
def release_memory(df):   
    del df
    gc.collect() 
    df = pd.DataFrame() # point to NULL
    print('memory RAM released.')

# Get start time 
start_time = time.time()

# time - multithreading
start = time.perf_counter()

# faker object
fake = Faker()

number_of_clients = int(sys.argv[1])

#@snoop
def make_database():
    # client - transaction
    client_name = fake.name()
    id = random.randint(1000, 10000)
    value = random.random()*100
    date = fake.date_between(start_date='-90d', end_date='today') # 3 months ago!
    date_register = fake.date_between(start_date='-3y', end_date='today')

    name_cols = []

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


print("----------------------------- DATABASE ----------------------------") 
df = generate_fakedata(nrows=number_of_clients)
# display the database
print(df)

#print("saving the file format feather...")
# this is important to do before save in feather format.
df = df.reset_index(drop=True) 
df.to_feather('dataset/fakeDatabase.ftr')
release_memory(df)

# time of execution in minutes
time_exec_min = round( (time.time() - start_time)/60, 4)

print(f'time of execution: {time_exec_min} minutes')
os.system('date')
print(f"All Done. :)")