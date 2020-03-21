#!/bin/bash
rm nohup.out
echo "finding FLASK process"
ps -ef | grep -i flask | grep -v grep | awk {'print $2'} | xargs kill
echo "FLASK process killed"
export FLASK_CONFIG=development
export FLASK_ENV=development
export FLASK_APP=run.py
echo "FLASK variables set"
nohup flask run --host=0.0.0.0 --port 5050
echo "FLASK running...."
echo "FLASK PID:- "
ps -ef | grep flask