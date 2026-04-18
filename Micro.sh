#!/bin/bash
# Micro.sh — StockStory end-to-end pipeline
# Usage: bash Micro.sh inputs/AAPL.csv

INPUT=$1

# Validate input
if [ -z "$INPUT" ]; then
    echo "Usage: bash Micro.sh <path-to-csv>"
    echo "Example: bash Micro.sh inputs/AAPL.csv"
    exit 1
fi

if [ ! -f "$INPUT" ]; then
    echo "Error: File '$INPUT' not found."
    exit 1
fi

# Extract ticker name from filename (e.g. inputs/AAPL.csv -> AAPL)
FILENAME=$(basename "$INPUT")
TICKER="${FILENAME%%.*}"
TICKER=$(echo "$TICKER" | tr '[:lower:]' '[:upper:]')

JSON_PATH="outputs/${TICKER}_records.json"

echo "----------------------------------------"
echo " StockStory Pipeline"
echo " Ticker  : $TICKER"
echo " Input   : $INPUT"
echo " JSON    : $JSON_PATH"
echo "----------------------------------------"

# Step 1: Compile Java (if not already compiled)
echo "[1/3] Compiling Java parser..."
javac -cp "antlr-4.13.1-complete.jar" src/Main.java src/parser/*.java -d src/parser
if [ $? -ne 0 ]; then
    echo "Error: Java compilation failed."
    exit 1
fi
echo "      Done."

# Step 2: Run Java parser (CSV -> JSON)
echo "[2/3] Parsing CSV with Java/ANTLR..."
mkdir -p outputs
java -cp "antlr-4.13.1-complete.jar:src/parser" Main "$INPUT" "$JSON_PATH"
if [ $? -ne 0 ] || [ ! -f "$JSON_PATH" ]; then
    echo "Error: Java parser failed or produced no output."
    exit 1
fi
echo "      Done. JSON saved to $JSON_PATH"

# Step 3: Run Python analysis (JSON -> CSV report)
echo "[3/3] Running Python analysis..."
python main.py "$JSON_PATH"
if [ $? -ne 0 ]; then
    echo "Error: Python analysis failed."
    exit 1
fi
echo "      Done. Report saved to outputs/${TICKER}_analysis_report.csv"

echo "----------------------------------------"
echo " Pipeline complete!"
echo "----------------------------------------"