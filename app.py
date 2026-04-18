import streamlit as st
import os
import subprocess
import sys

from src.DataProcessor import DataProcessor
from ChartBuilder import ChartBuilder

st.title("StockStory")

uploaded_file = st.file_uploader("Upload .csv file here", type=["csv"])

if uploaded_file:
    os.makedirs("outputs", exist_ok=True)

    input_path = f"outputs/{uploaded_file.name}"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    ticker = uploaded_file.name.split('.')[0].upper()
    json_path = f"outputs/{ticker}_records.json"

    # Build classpath separator based on OS
    sep = ";" if sys.platform == "win32" else ":"
    classpath = f"antlr-4.13.1-complete.jar{sep}src/parser"

    # Run Java parser
    result = subprocess.run([
        "java",
        "-cp", classpath,
        "Main",
        input_path,
        json_path
    ], capture_output=True, text=True)

    # Check if Java parser succeeded
    if result.returncode != 0 or not os.path.exists(json_path):
        st.error("Java parser failed. See details below:")
        st.code(result.stderr)
        st.stop()

    # Process data
    processor = DataProcessor(ticker)
    df = processor.load_json_data(json_path)

    if df is None:
        st.error("Failed to load JSON data. The parser may have produced an empty or invalid file.")
        st.stop()

    df = processor.process_all()

    cb = ChartBuilder()

    st.subheader("Price Action")
    st.plotly_chart(cb.price_action(df))

    st.subheader("Trend")
    st.plotly_chart(cb.trend_chart(df))

    st.subheader("Risk")
    st.plotly_chart(cb.risk_chart(df))

    st.subheader("Relative Performance")
    st.plotly_chart(cb.relative_performance(df))