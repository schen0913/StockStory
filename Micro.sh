#!/bin/bash
# Micro.sh — StockStory end-to-end pipeline (Mac/Linux/Windows Git Bash)
# Usage: bash Micro.sh inputs/AAPL.csv [output_dir]

INPUT=$1
OUTDIR=${2:-outputs}

if [ -z "$INPUT" ]; then
    echo "Usage: bash Micro.sh <path-to-csv> [output_dir]"
    echo "Example: bash Micro.sh inputs/AAPL.csv"
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

# Detect OS and set classpath separator
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    SEP=";"
else
    SEP=":"
fi

echo "----------------------------------------"
echo " StockStory Pipeline"
echo " Ticker  : $TICKER"
echo " Input   : $INPUT"
echo " Output  : $OUTDIR"
echo " JSON    : $JSON_PATH"
echo "----------------------------------------"

# Step 1: Generate ANTLR parser from grammar
echo "[1/3] Generating parser from grammar..."
rm -f src/parser/StockLexer.java src/parser/StockParser.java \
      src/parser/StockListener.java src/parser/StockBaseListener.java \
      src/parser/*.class
cp Stock.g4 src/parser/Stock.g4
cd src/parser
java -cp "../../antlr-4.13.1-complete.jar" org.antlr.v4.Tool Stock.g4
cd ../..
if [ $? -ne 0 ]; then
    echo "Error: ANTLR grammar generation failed."
    exit 1
fi
echo "      Done."

# Step 2: Compile all Java
echo "[2/3] Compiling Java..."
javac -cp "antlr-4.13.1-complete.jar${SEP}src/parser" \
    src/parser/StockLexer.java \
    src/parser/StockParser.java \
    src/parser/StockListener.java \
    src/parser/StockBaseListener.java \
    src/parser/StockRecord.java \
    src/parser/StockStoryListener.java \
    src/Main.java \
    -d src/parser
if [ $? -ne 0 ]; then
    echo "Error: Java compilation failed."
    exit 1
fi
echo "      Done."

# Step 3: Run Java parser (CSV -> JSON)
echo "[3/5] Parsing CSV with Java/ANTLR..."
java -cp "antlr-4.13.1-complete.jar${SEP}src/parser" Main "$INPUT" "$JSON_PATH"
if [ $? -ne 0 ] || [ ! -f "$JSON_PATH" ]; then
    echo "Error: Java parser failed or produced no output."
    exit 1
fi
echo "      Done. JSON saved to $JSON_PATH"

# Step 4: Run Python analysis (JSON -> CSV report)
echo "[4/5] Running Python analysis..."
python main.py "$JSON_PATH" "$OUTDIR"
if [ $? -ne 0 ]; then
    echo "Error: Python analysis failed."
    exit 1
fi
echo "      Done. Report saved to ${OUTDIR}/${TICKER}_analysis_report.csv"

echo "----------------------------------------"
echo " Pipeline complete! Files saved to: $OUTDIR"
echo "----------------------------------------"