######################################
# This script is a way to verify
# the performance of python

# Author: @andvsilva 2022-12-12
######################################

import time
import sys

start_time = time.time()
number = 10**7 + 1

sum(range(number))

print(f">>> Python is {round(time.time() - start_time, 6)} in seconds.")
print("Sum is is =", sum(range(number)))
