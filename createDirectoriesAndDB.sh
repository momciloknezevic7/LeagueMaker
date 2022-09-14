#!/bin/bash
# Potentially necessary before run this script: chmod +x filename.sh

# Directory for storing .csv file 
[ ! -d DataInput ] && mkdir -p DataInput

# Directory where program will store fixtures file 
[ ! -d Fixtures ] && mkdir -p Fixtures

# Directory where user will store fixtures file after putting result in it 
[ ! -d Results ] && mkdir -p Results
[ ! -d 'Results/ReadOut Fixtures' ] && mkdir -p 'Results/ReadOut Fixtures'
[ ! -d 'Results/Unread Fixtures' ] && mkdir -p 'Results/Unread Fixtures'

# Creating database
python db/db_reset.py 