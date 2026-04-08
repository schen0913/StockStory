import json
import pandas as pd
from DataProcessor import DataProcessor

def main():

    ticker = "NVDA"
    processor = DataProcessor(ticker)

    json_file = "records.json"
    
    print(f"--- Python Analyisis Stage ---")
    print(f"Loading data from: {json_file}")

    data = processor.load_json_data(json_file)
    if data is not None:

        print("Proccesing moving averages, returns, and volatiliyu...")
        processed_df = processor.process_all()

        print("\n--- DATA PREVIEW ---")
        print(processed_df.tail())

        processed_df.to_csv(f"{ticker}_analyzed.csv")
        print(f"\nFinal analysis saved to {ticker}_analyzed.csv")
    else:
        print("Error: Could not load JSON. Ensure 'records.json' exists and is properly formatted.")

if __name__ == "__main__":
    main()