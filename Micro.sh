#!/bin/bash
# Micro.sh — StockStory end-to-end pipeline
# Usage: bash Micro.sh inputs/AAPL.csv [output_dir]

INPUT=$1
OUTDIR=${2:-outputs}

if [ -z "$INPUT" ]; then
    echo "Usage: bash Micro.sh <path-to-csv> [output_dir]"
    exit 1
fi

if [ ! -f "$INPUT" ]; then
    echo "Error: File '$INPUT' not found."
    exit 1
fi

FILENAME=$(basename "$INPUT")
TICKER="${FILENAME%%.*}"
TICKER=$(echo "$TICKER" | tr '[:lower:]' '[:upper:]')
JSON_PATH="${OUTDIR}/${TICKER}_records.json"

mkdir -p "$OUTDIR"

echo "----------------------------------------"
echo " StockStory Pipeline"
echo " Ticker  : $TICKER"
echo " Input   : $INPUT"
echo " Output  : $OUTDIR"
echo " JSON    : $JSON_PATH"
echo "----------------------------------------"

# Step 1: Compile only if .class files are missing
echo "[1/3] Checking Java parser..."
if [ ! -f "src/parser/Main.class" ] || [ ! -f "src/parser/StockStoryListener.class" ]; then
    echo "      Compiling..."
    javac -cp "antlr-4.13.1-complete.jar" \
        src/parser/StockLexer.java \
        src/parser/StockParser.java \
        src/parser/StockListener.java \
        src/parser/StockBaseListener.java \
        -d src/parser
    if [ $? -ne 0 ]; then
        echo "Error: Java compilation failed (pass 1)."
        exit 1
    fi
    javac -cp "antlr-4.13.1-complete.jar:src/parser" \
        src/parser/StockRecord.java \
        src/parser/StockStoryListener.java \
        src/Main.java \
        -d src/parser
    if [ $? -ne 0 ]; then
        echo "Error: Java compilation failed (pass 2)."
        exit 1
    fi
    echo "      Done."
else
    echo "      Already compiled, skipping."
fi

# Step 2: Run Java parser (CSV -> JSON)
echo "[2/3] Parsing CSV with Java/ANTLR..."
java -cp "antlr-4.13.1-complete.jar:src/parser" Main "$INPUT" "$JSON_PATH"
if [ $? -ne 0 ] || [ ! -f "$JSON_PATH" ]; then
    echo "Error: Java parser failed or produced no output."
    exit 1
fi
echo "      Done. JSON saved to $JSON_PATH"

# Step 3: Run Python analysis (JSON -> CSV report)
echo "[3/3] Running Python analysis..."
python main.py "$JSON_PATH" "$OUTDIR"
if [ $? -ne 0 ]; then
    echo "Error: Python analysis failed."
    exit 1
fi
echo "      Done. Report saved to ${OUTDIR}/${TICKER}_analysis_report.csv"

echo "----------------------------------------"
echo " Pipeline complete! Files saved to: $OUTDIR"
echo "----------------------------------------"