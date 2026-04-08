import requests
from bs4 import BeautifulSoup
import os

def get_stock_price():
    # 爬取 Yahoo 股市 (以台積電 2330 為例)
    url = "https://tw.stock.yahoo.com/quote/2330.TW"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # 抓取股價與漲跌
    price = soup.find('span', {'class': 'Fz(32px)'}).text
    return f"📈 台積電 (2330) 目前股價：{price}"

def send_telegram_msg(text):
    # 從剛剛設定的 Secrets 讀取資料
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    message = get_stock_price()
    send_telegram_msg(message)
