import streamlit as st
import os 
import subprocess

from src.DataProcessor import DataProcessor
from ChartBuilder import ChartBuilder

st.title("StockStory")

uploaded_file = st.file_uploader("Upload .csv file here", type=["csv"])

if uploaded_file:
    os.makedirs("temp", exist_ok=True)

    input_path = f"temp/{uploaded_file.name}"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    ticker = uploaded_file.name.split('.')[0].upper()
    json_path = f"temp/{ticker}_records.json"

    # Run Java parser
    subprocess.run([
        "java",
        "-cp",
        "lib/antlr-4.13.2-complete.jar;src;src/parser",
        "Main",
        input_path,
        json_path
    ])

    # Process data
    processor = DataProcessor(ticker)
    df = processor.load_json_data(json_path)
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