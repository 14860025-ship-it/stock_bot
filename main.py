import requests
import os

def test_telegram():
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    # 這裡會印出檢查資訊 (會遮蔽部分字元保護隱私)
    print(f"--- 檢查開始 ---")
    print(f"Token 前五碼: {token[:5] if token else '沒抓到'}")
    print(f"Chat ID: {chat_id if chat_id else '沒抓到'}")
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': '🔥 測試連線中！如果你看到這則訊息，代表成功了！'}
    
    try:
        response = requests.post(url, data=payload)
        print(f"Telegram 回傳狀態碼: {response.status_code}")
        print(f"Telegram 回傳內容: {response.text}")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    test_telegram()
