import json
import sys
import os
import pandas as pd
from DataProcessor import DataProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <json_file_path>")
        return
    
    json_file_path = sys.argv[1]

    # This logic handles paths like 'outputs/NVDA_records.json' 
    # and extracts just 'NVDA'
    filename = os.path.basename(json_file_path)
    ticker_name = filename.split('_')[0] 
    
    processor = DataProcessor(ticker_name)
    
    print(f"--- Starting Semantic Analysis for {ticker_name} ---")

    # 1. Load the data
    if processor.load_json_data(json_file_path) is not None:
        
        # 2. Run all the math (MA, Volatility, Crossovers, etc.)
        print(f"Calculating financial stories...")
        processed_df = processor.process_all()
        
        # 3. Save the result into the outputs folder
        # We use the ticker name so we get 'NVDA_analysis_report.csv', etc.
        output_csv = f"outputs/{ticker_name}_analysis_report.csv"
        
        # Ensure the outputs directory exists
        os.makedirs('outputs', exist_ok=True)
        
        processed_df.to_csv(output_csv)
        
        print(f"Success! Analysis report saved to: {output_csv}")
        print("-" * 40)
    else:
        print(f"Error: Could not process {json_file_path}")

if __name__ == "__main__":
    main()