import json

import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, ticker_name):
        self.ticker = ticker_name.upper()
        self.raw_data = []
        self.df = None

    def load_json_data(self, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            self.df = pd.DataFrame(data)

            column_map = {
                'date': 'Date',
                'open': 'Open',
                'high': 'High',
                'low': 'Low',
                'close': 'Close',
                'volume': 'Volume'
            }
            self.df.rename(columns=column_map, inplace=True)

            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df.sort_values('Date', inplace=True)
            self.df.reset_index(drop=True, inplace=True)
            self.df.set_index('Date', inplace=True)

            number_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            for col in number_columns:
                if col in self.df.columns:
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
            return self.df
        except Exception as e:
            print(f"Error loading JSON data: {e}")
            return None

    def receive_row(self, date, open_price, high_price, low_price, close_price, volume):
        """Receives data from ANTLR listener."""
        self.raw_data.append({
            "Date": date,
            "Open": float(open_price),
            "High": float(high_price),
            "Low": float(low_price),
            "Close": float(close_price),
            "Volume": int(volume)
        })

    def finalize_data(self):
        """Prepares the table for financial analysis."""
        self.df = pd.DataFrame(self.raw_data)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.sort_values('Date', inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        self.df.set_index('Date', inplace=True)
        return self.df
    
    def add_moving_averages(self, short_window=20, long_window=50):
        """STORY 2: Trend Analysis with Moving Averages"""
        if self.df is not None:
            self.df['SMA20'] = self.df['Close'].rolling(window=short_window).mean()
            self.df['SMA50'] = self.df['Close'].rolling(window=long_window).mean()
        return self.df
    
    def add_signals(self):
        """STORY 2: Indentifies Golden and Death Crosses based on SMA20 and SMA50"""
        if self.df is not None:
            if 'SMA20' not in self.df.columns or 'SMA50' not in self.df.columns:
                self.add_moving_averages()

            self.df['Signal'] = 0
            self.df.loc[self.df['SMA20'] > self.df['SMA50'], 'Signal'] = 1
            self.df.loc['Crossover'] = self.df['Signal'].diff()

        return self.df
    
    def add_returns(self):
        """STORY 1 & 3: Calculates daily percentage changes"""
        if self.df is not None:
            self.df['Daily Return'] = self.df['Close'].pct_change() * 100
        return self.df
    
    def add_volatility(self, window=20):
        """STORY 3: Risk Assesment (Rolling Standard Deviation of Returns)"""
        if self.df is not None:
            if 'Daily Return' not in self.df.columns:
                self.add_returns()
            self.df['Volatility'] = self.df['Daily Return'].rolling(window=window).std()
        return self.df
    
    def add_normalization(self):
        """STORY 4: Normalizes the 'Close' price to a base value of 100 at the start of the dataset"""
        if self.df is not None:
            first_price = self.df['Close'].iloc[0]
            self.df['Normalized Close'] = (self.df['Close'] / first_price) * 100
        return self.df
    
    def process_all(self):
        if self.df is not None:
            self.add_moving_averages()
            self.add_signals()
            self.add_returns()
            self.add_volatility()
            self.add_normalization()
        return self.df
    