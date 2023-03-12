#!/bin/zsh

begin=$(date +"%s")
for JobNumber in {0..10}; do

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
<<<<<<< HEAD:generatorFake_data/rungendata.sh
    python generator_data.py 10000 $JobNumber &
=======
    python generator_data.py 100 $JobNumber &
>>>>>>> ceb67e458ae1a5a30345865e7b0ec1f673326958:generatorFake_data/scripts/rungendata.sh
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

termin=$(date +"%s")
difftimelps=$(($termin-$begin))

echo "$(($difftimelps / 60)) minutes and $(($difftimelps % 60)) seconds elapsed for Script Execution."
echo "All Done!"