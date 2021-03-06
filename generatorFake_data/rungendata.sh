#!/bin/zsh

for JobNumber in {0..100}; do

    nprocesses=$(< NumberOfJobsRunning.txt)

    # Please, check the number of jobs running
    while [ $(ls -l | grep jobRunning | wc -l) -ge $nprocesses ]; 
    do

        nprocesses=$(< NumberOfJobsRunning.txt)

        sleep 10s; # so, wait until one job finish!

    done

    # number of processes running
    echo "Number of processes to keep alive: $nprocesses"

    # run python code 
    python generator_data.py 10000 $JobNumber &
    sleep 1s

done

while [ $(ls -l | grep jobRunning | wc -l) -gt 0 ]; 
    do
        sleep 10s; # so, wait until one job finish!
        echo "waiting until the last process finished..."

    done

echo "merging files..."
# merge files csv to one file feather.
python merge_files.py

echo "All Done!"
