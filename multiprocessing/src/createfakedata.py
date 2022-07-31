import pandas as pd
import sys
import time
import os

import gendata
import toolkit

# print datetime in the terminal
os.system('date')

# Get start time.
start_time = time.time()

# time - multithreading.
start = time.perf_counter()

# get arguments from input file.
number_of_clients = int(sys.argv[1])
jobNumber = int(sys.argv[2])

# print on the terminal window
os.system(f'touch ../scripts/jobRunning{jobNumber}')
print(f"Starting job #{jobNumber}...")

print("----------------------------- DATABASE ----------------------------") 
df = gendata.generate_fakedata(nrows=number_of_clients)

# display the database
print(df)

df.to_csv(f'../dataset/fakeDatabase_{jobNumber}.csv')

toolkit.release_memory(df)

# time of execution in minutes
time_exec_min = round( (time.time() - start_time)/60, 4)

print(f'time of execution: {time_exec_min} minutes')
os.system('date')
print(f"All Done. :)")

warning_message = "please, remove the file jobRunning"
os.system(f"echo {warning_message}{jobNumber}...")
os.system(f'rm ../scripts/jobRunning{jobNumber}')