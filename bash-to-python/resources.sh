#!/bin/bash

# start a background process
ping www.google.ca &> /dev/null &

# write its PID to file
PID_FILE=example.pid
echo $! > $PID_FILE

# read pid from first line of example.pid file
# kill that process 
read PID < $PID_FILE
if [ "$PID" ] 
then
  ps $PID
  kill $PID
else
  echo "process $PID not found"
fi

# run an executable
APP="python3 print_stuff.py"
ROOT_DIR=/Users/jguo

TODAY=`date '+%Y%m%d'`
output_dir="results_$TODAY"
mkdir $output_dir
for filename in `ls ${ROOT_DIR}/*.sh | sort -r`
do 
  name=`basename $filename`
  echo $name
  $APP $filename > ""
