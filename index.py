import requests
import pandas as pd
from datetime import datetime
import time

# Coingecko API endpoint
url = "https://api.coingecko.com/api/v3/simple/price"

# Top 10 Cryptos
cryptos = ["bitcoin", "ethereum", "ripple", "cardano", "solana", "polkadot", "binancecoin", "dogecoin", "avalanche-2", "terra-luna"]

#Data collection
data_list = []

for i in range(2):
    params = {
        "ids": ",".join(cryptos),
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    print("API Response:", response.text)  
    data = response.json()
    data_list.append(data)
    # Wait for 10 minutes between requests(will price change significantly? try with other times and see)
    time.sleep(600)  

# Extract relevant data
records = []

for data in data_list:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #(check to see if another time format will be better)
    for crypto in cryptos:
        record = {
            "Timestamp": timestamp,
            "Crypto": crypto,
            "Price": data[crypto]["usd"]
        }
        records.append(record)

# Create a DataFrame
df = pd.DataFrame(records)

# Calculate the difference in price between the second and first requests
df["Diff_Price"] = df.groupby("Crypto")["Price"].diff() #(How to handle decimal changes. will that be necessary)

# Save the DataFrame as new  CSV file
df.to_csv("done_crypto_prices_10.csv", index=False)


