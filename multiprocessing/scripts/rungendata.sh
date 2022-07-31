#!/bin/zsh

# Script to run multiple jobs in parallel

# arguments: number of jobs and number of eventos per job.
jobnumbers=$1
nevents=$2

# get datetime that start the run.
begin=$(date +"%s")

# loop in jobs.
for JobNumber in {1..$jobnumbers}; do

    # A good trick that we can change the number of jobs running 
    # 'on the fly', so, you don't need to stop the running.
    nprocesses=$(< NumberOfJobsRunning.txt)

    # Please, check the number of jobs running
    while [ $(ls -l | grep jobRunning | wc -l) -ge $nprocesses ]; 
    do
        nprocesses=$(< NumberOfJobsRunning.txt)
        sleep 3s; # so, wait until one job finish!
    done

    # number of processes running...
    echo "Number of processes to keep alive: $nprocesses"

    # run python code
    python ../src/createfakedata.py $nevents $JobNumber &
    sleep 1s # time to finish the job before the next one. 

done

# waiting until ALL the jobs are finished.
while [ $(ls -l | grep jobRunning | wc -l) -gt 0 ]; 
do
    sleep 3s; # so, wait until one job finish!
    echo "waiting until the last process finished..."
done

echo "merging files..."
# merge files csv to one file feather.
python ../src/merge_files.py

termin=$(date +"%s")
difftimelps=$(($termin-$begin))

echo "$(($difftimelps / 60)) minutes and $(($difftimelps % 60)) seconds elapsed for Script Execution."
echo "All Done!"
