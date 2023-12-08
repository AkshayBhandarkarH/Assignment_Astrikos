"""4. The below API print the price of Bitcoin in USD and GBP 
https://api.coindesk.com/v1/bpi/currentprice.json
• Collect data from this API for 1 day at 5 minutes interval. I.e you will have at least 
288 unique data points. Consecutive data points should not have same value.
• Find the highest and lowest price of bitcoin from the collected data, without using minimum 
or maximum functions"""
import requests
import time

api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_bitcoin_prices():
    prices = []
    for _ in range(288):  # 1 day at 5-minute intervals
        response = requests.get(api_url)
        data = response.json()
        
        # Extracting Bitcoin prices in USD and GBP
        usd_price = data["bpi"]["USD"]["rate_float"]
        gbp_price = data["bpi"]["GBP"]["rate_float"]
        
        prices.append((time.time(), usd_price, gbp_price))
        time.sleep(300)
    
    return prices

def find_highest_lowest(prices):
    highest_price = float("-inf")
    lowest_price = float("inf")
    
    for timestamp, usd_price, gbp_price in prices:
        if usd_price > highest_price:
            highest_price = usd_price
        
        if usd_price < lowest_price:
            lowest_price = usd_price
    
    return highest_price, lowest_price

bitcoin_prices = get_bitcoin_prices()
highest_price, lowest_price = find_highest_lowest(bitcoin_prices)

print("Highest Bitcoin Price (USD):", highest_price)
print("Lowest Bitcoin Price (USD):", lowest_price)
