import threading
import requests
import os
import random
from queue import Queue

# Configuration
BASE_URL = "http://www.floatrates.com/daily/{currency}.xml"
CURRENCY_LIST = ['usd', 'eur', 'gbp', 'jpy', 'cad', 'aud', 'nzd', 'chf', 'cny', 'inr']  # Add up to 52 currencies
DATA_DIR = "currency_data"
NUM_WORKERS = 3

# Thread-safe queue
task_queue = Queue()

def download_and_save_xml(currency_code):
    try:
        response = requests.get(BASE_URL.format(currency=currency_code), timeout=10)
        response.raise_for_status()
        
        # Create output directory
        dir_path = os.path.join(DATA_DIR, currency_code.upper())
        os.makedirs(dir_path, exist_ok=True)
        
        # Save XML as-is
        file_path = os.path.join(dir_path, "latest.xml")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Saved XML for {currency_code.upper()} at {file_path}")
        
    except Exception as e:
        print(f"[ERROR] Failed for {currency_code.upper()}: {e}")

def worker():
    while not task_queue.empty():
        currency = task_queue.get()
        print(f"Thread {threading.current_thread().name} processing {currency}")
        download_and_save_xml(currency)
        task_queue.task_done()

def main():
    currency = random.choice(CURRENCY_LIST)
    print(f"Selected currency: {currency.upper()}")
    task_queue.put(currency)

    threads = []
    for _ in range(NUM_WORKERS):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    task_queue.join()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()