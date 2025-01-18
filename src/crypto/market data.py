import requests
import pandas as pd
from datetime import datetime, timedelta

class CryptoDataFetcher:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://api.coingecko.com/api/v3"
    
    def get_price_history(self, symbol, days=30):
        """Fetch historical price data for a cryptocurrency"""
        endpoint = f"/coins/{symbol}/market_chart"
        params = {
            'vs_currency': 'usd',
            'days': days,
            'interval': 'daily'
        }
        
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        data = response.json()
        
        df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('date', inplace=True)
        df.drop('timestamp', axis=1, inplace=True)
        
        return df
    
    def get_current_price(self, symbol):
        """Get current price for a cryptocurrency"""
        endpoint = f"/simple/price"
        params = {
            'ids': symbol,
            'vs_currencies': 'usd'
        }
        
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        data = response.json()
        
        return data[symbol]['usd']