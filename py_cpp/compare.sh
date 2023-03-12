#!/bin/bash

# This script bash will run the programs in C++
# and python to do the comparison to
# check the performance of each program.

#compile C++
g++ -o time.exec time.cpp
timecpp=$(./time.exec)
echo "$timecpp"
timecppexec=${timecpp:10:8}
cppexec_time=$(bc -l <<<"${timecppexec}")
#echo $cppexec_time

timepy=`python time.py`
echo $timepy
timepyexec=${timepy:14:8}
pyexec_time=$(bc -l <<<"${timepyexec}")
#echo $pyexec_time

# calculate the performance
performance_perc=$((pyexec_time / cppexec_time))

echo "Comparing the performance of python and C++..."
echo "We have that C++ is more fast than python: $performance_perc times!"

echo "All done :)"