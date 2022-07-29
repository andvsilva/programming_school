import glob
import os
import pandas as pd
import time

# list file
files = [f for f in glob.glob("../dataset/fakeDatabase_*.csv")]

# dataframe
df_merge = pd.DataFrame()

# merge files
for file in files:
    df = pd.read_csv(f'{file}')
    df_merge = pd.concat([df_merge, df], ignore_index=True)

print("saving the file feather format...")
# this is important to do before save in feather format.
df_merge = df_merge.reset_index(drop=True)
df_merge.to_feather('../dataset/fakeDatabase.ftr')
print('files merged successfully.')

# print('removing files csv...')
for file in files:
    os.system(f'rm {file}')