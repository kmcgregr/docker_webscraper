import os
import sys
import requests
import csv
from bs4 import BeautifulSoup

def read_stock_file():
 stock_data_file = open('my_stocks.csv','r')
 return stock_data_file.readlines()
 
def get_stock_price():
    stock_tickers = read_stock_file()
    for stock in stock_tickers:
        try:
            print("Stock",stock)
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
            url = "https://ca.finance.yahoo.com/quote/%s?p=%s"%(stock,stock)
            page = requests.get(url,headers=headers)
            print("response.ok : {} , response.status_code : {}".format(page.ok , page.status_code))
            print("Preview of response.text : ", page.text[:500])
            soup = BeautifulSoup(page.content, 'html.parser')
            price = soup.find("fin-streamer", {"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)","value":True})['value']

            with open('stock_prices.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([price])
        except Exception as error:
            print("An error occured",error.args[0])
            sys.exit()

get_stock_price()
