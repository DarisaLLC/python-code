#!/bin/bash

# start a background process
ping www.google.ca &> /dev/null &

# write its PID to file
PID_FILE=example.pid
echo $! > $PID_FILE
