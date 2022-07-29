#################################################
#                Toolkit  
# Funtions to execute tasks.

# Author: @andvsilva 2022-07-15
# Usage: add a function with a simple description
##################################################


import random
import pandas as pd
import gc
import os

os.system('date')

# Pandas has a high consume of memory RAM usage
# release memory RAM
def release_memory(df):   
    del df
    gc.collect() 
    df = pd.DataFrame() # point to NULL
    print('memory RAM released.')
