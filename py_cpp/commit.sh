#!/bin/bash
# script to commit to repo.
echo "${1}"

echo "Add changes in files or directory..."
git add .
echo "committing..."
git commit -m "${1}"
git pull origin master
git push -u origin master
echo "All done! :)"

