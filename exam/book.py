import requests
import fitz 
from pdf2image import convert_from_path
from ebooklib import epub
from PIL import Image

BOT_TOKEN = "7700842374:AAGAovjEHzG7iRCM87Fo0TrPCT1lyJFOR7E"
CHANNEL_ID = "@getsbooks"

def send_telegram_message(method, data, files=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    response = requests.post(url, data=data, files=files)
    return response.json()

def download_file(file_id):
    file_info = send_telegram_message("getFile", {"file_id": file_id})
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
    images = convert_from_path(pdf_path, first_page=1, last_page=1)
    if images:
        img_path = pdf_path.replace(".pdf", ".jpg")
        images[0].save(img_path, "JPEG")
        return img_path
    return None

def extract_epub_first_page(epub_path):
    book = epub.read_epub(epub_path)
    for item in book.items:
        if item.get_type() == 9: 
            img_data = item.get_content()
            img_path = epub_path.replace(".epub", ".jpg")
            with open(img_path, "wb") as f:
                f.write(img_data)
            return img_path
    return None

def extract_djvu_first_page(djvu_path):
    doc = fitz.open(djvu_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    
    img_path = djvu_path.replace(".djvu", ".jpg")
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save(img_path, "JPEG")
    return img_path

def process_telegram_update(update):
    if "message" in update and "document" in update["message"]:
        file_id = update["message"]["document"]["file_id"]
        file_name = update["message"]["document"]["file_name"].lower()

        file_path = download_file(file_id)
        if not file_path:
            return

        if file_path.endswith(".pdf"):
            img_path = extract_pdf_first_page(file_path)
        elif file_path.endswith(".epub"):
            img_path = extract_epub_first_page(file_path)
        elif file_path.endswith(".djvu"):
            img_path = extract_djvu_first_page(file_path)
        else:
            return

        if img_path:
            with open(img_path, "rb") as img:
                response = send_telegram_message("sendPhoto", {"chat_id": CHANNEL_ID}, {"photo": img})
                if "result" in response:
                    message_id = response["result"]["message_id"]
                    
                    with open(file_path, "rb") as book:
                        send_telegram_message("sendDocument", {"chat_id": CHANNEL_ID, "reply_to_message_id": message_id}, {"document": book})

def main():
    offset = 0
    while True:
        updates = send_telegram_message("getUpdates", {"offset": offset})
        if "result" in updates:
            for update in updates["result"]:
                process_telegram_update(update)
                offset = update["update_id"] + 1

if __name__ == "__main__":
    main()