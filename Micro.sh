#!/bin/bash
# micro.sh
INPUT=$1
OUTPUT=$2

# Java — parse CSV -> JSON
java -cp ".:antlr-4.13.1-complete.jar" stockstory.Main "$INPUT" records.json

# Python — JSON -> HTML charts
python3 charts.py records.json "$OUTPUT"