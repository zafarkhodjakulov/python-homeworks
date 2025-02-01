import os
import pandas as pd
import requests
from pdf2image import convert_from_path

BOT_TOKEN = "7706754128:AAEPY6NwAE-oueYeYyz_sUcf6NM_Yd9eGow"
CHANNEL_ID = "@getsbooks"
POPPLER_PATH = r"C:\\poppler\\Library\\bin"  
CSV_FILE = 'book_stats.csv'

def send_telegram(method, data, files=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    response = requests.post(url, data=data, files=files)
    return response.json()

def download_file(file_id):
    file_info = send_telegram("getFile", {"file_id": file_id})
    if "result" not in file_info:
        return None
    file_path = file_info['result']['file_path']
    file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
    response = requests.get(file_url)
    
    if response.status_code == 200:
        filename = file_path.split("/")[-1]
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    return None

def extract_pdf_first_page(pdf_path):
    images = convert_from_path(pdf_path, first_page=1, last_page=1, poppler_path=POPPLER_PATH)
    if images:
        img_path = pdf_path.replace(".pdf", ".jpg")
        images[0].save(img_path, "JPEG")
        return img_path
    return None

def log_book_status(book_name, status):
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=["book_name", "status"])
    new_data = pd.DataFrame([{"book_name": book_name, "status": status}])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def get_successful_book_count():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        return len(df[df["status"] == "Success"])
    return 0

def send_book_to_channel(file_path, file_name):
    img_path = extract_pdf_first_page(file_path)
    if not img_path:
        log_book_status(file_name, "Failed")
        return None

    with open(img_path, "rb") as img:
        response_img = send_telegram("sendPhoto", {
            "chat_id": CHANNEL_ID
        }, {"photo": img})

    if "result" not in response_img:
        log_book_status(file_name, "Failed")
        return None
    reply_to_message_id = response_img["result"]["message_id"]

    with open(file_path, "rb") as book:
        response_reply = send_telegram("sendDocument", {
            "chat_id": CHANNEL_ID,
            "reply_to_message_id": reply_to_message_id
        }, {"document": book})

    if "result" in response_reply:
        log_book_status(file_name, "Success")
    else:
        log_book_status(file_name, "Failed")

def process_telegram_update(update):
    if "message" in update and "chat" in update["message"]:
        chat_id = update["message"]["chat"]["id"]

        if "document" in update["message"]:
            file_id = update["message"]["document"]["file_id"]
            file_name = update["message"]["document"]["file_name"]
            
            file_path = download_file(file_id)
            if file_path:
                send_book_to_channel(file_path, file_name)
            else:
                log_book_status(file_name, "Failed")

        elif "text" in update["message"] and update["message"]["text"] == "/stats":
            count = get_successful_book_count()
            send_telegram("sendMessage", {
                "chat_id": chat_id,
                "text": f"📊 Muvaffaqiyatli jo'natilgan kitoblar soni: {count}"
            })

def main():
    offset = 0
    while True:
        updates = send_telegram("getUpdates", {"offset": offset})
        if "result" in updates:
            for update in updates["result"]:
                process_telegram_update(update)
                offset = update["update_id"] + 1

if __name__ == "__main__":
    main()