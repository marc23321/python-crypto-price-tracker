# python-crypto-price-tracker

Tried my hand on this to better understand the Extract, Transform, and Load (ETL) process


I wrote this code to collect real-time price data for a curated selection of the top 10 cryptocurrencies from the CoinGecko API. Let's break down the script's functionality step by step:

API Configuration:

The script defines the API endpoint as "https://api.coingecko.com/api/v3/simple/price."
It specifies the top 10 cryptocurrencies of interest in the cryptos list.
Data Collection:

The script initializes an empty list data_list to store API responses.
It iterates twice through a loop to make two API requests with a 10-minute delay between requests.
For each iteration, it constructs parameters for the API request, including the list of cryptocurrencies and the desired currency ("usd").
It uses the requests.get method to send the API request and stores the JSON response in the data_list.
The script prints the API response for each request.
Data Extraction:

After collecting API responses, the script initializes an empty list records to store relevant data.
It iterates through each API response in data_list and, for each cryptocurrency, extracts the timestamp, cryptocurrency name, and its current price in USD.
The extracted data is structured as dictionaries and appended to the records list.
DataFrame Creation:

Using the Pandas library, the script creates a DataFrame (df) from the list of records.
Price Difference Calculation:

The script calculates the difference in price (Diff_Price) for each cryptocurrency between the second and first API requests using the groupby and diff functions.
Data Export:

Finally, the script saves the DataFrame as a CSV file named "done_crypto_prices_10.csv."