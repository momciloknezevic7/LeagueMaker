#!/bin/bash
# Potentially necessary before run this script: chmod +x filename.sh

# Directory for storing .csv file 
[ ! -d DataInput ] && mkdir -p DataInput

# Directory where program will store fixtures file 
[ ! -d Fixtures ] && mkdir -p Fixtures

# Directory where user will store fixtures file after putting result in it 
[ ! -d Results ] && mkdir -p Results
[ ! -d 'Fixtures/ReadOut Fixtures' ] && mkdir -p 'Fixtures/ReadOut Fixtures'
[ ! -d 'Fixtures/Unread Fixtures' ] && mkdir -p 'Fixtures/Unread Fixtures'