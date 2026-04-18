import json
import sys
import os
import pandas as pd
from src.DataProcessor import DataProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <json_file_path> [output_dir]")
        return
    
    json_file_path = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) >= 3 else "outputs"

    filename = os.path.basename(json_file_path)
    ticker_name = filename.split('_')[0]
    
    processor = DataProcessor(ticker_name)
    
    print(f"--- Starting Semantic Analysis for {ticker_name} ---")

    if processor.load_json_data(json_file_path) is not None:
        print(f"Calculating financial stories...")
        processed_df = processor.process_all()
        
        os.makedirs(out_dir, exist_ok=True)
        output_csv = f"{out_dir}/{ticker_name}_analysis_report.csv"
        processed_df.to_csv(output_csv)
        
        print(f"Success! Analysis report saved to: {output_csv}")
        print("-" * 40)
    else:
        print(f"Error: Could not process {json_file_path}")

if __name__ == "__main__":
    main()