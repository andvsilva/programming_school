import sys
import os

# print datetime in the terminal
os.system('date')

# get arguments from input file.
jobNumber = int(sys.argv[1])
number_range = int(sys.argv[2])

# print on the terminal window
os.system(f'touch jobRunning{jobNumber}')
print(f"Starting job #{jobNumber}...")

def solve(number_range):
    square = 0
    for number in range(1,number_range):
        square += number**2
        
solve(number_range)

os.system('date')
print(f"All Done. :)")
    
os.system(f'rm jobRunning{jobNumber}')