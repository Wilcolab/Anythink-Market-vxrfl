#!/bin/bash

# Check if the file argument is provided
if [ $# -eq 0 ]; then
    echo "Please provide a filename as an argument"
    exit 1
fi

# Check if the file exists
if [ ! -f $1 ]; then
    echo "File not found"
    exit 1
fi

# Extract the first and last names
awk -F',' 'tolower($4) ~ /amazon\.com/ {print $3, $2}' $1 > amazon_names.txt

echo "The first and last names of individuals whose email addresses contain 'amazon.com' or 'Amazon.com' are saved in amazon_names.txt"
