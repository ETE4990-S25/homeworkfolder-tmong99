import requests
import os


url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"

def download_xml(base, date):
    try:
        base_data = requests.get(url.format(date=date, base=base), timeout=10)
        base_data.raise_for_status()

        # create file
        directory = os.path.join("historical_currency_data", base)
        os.makedirs(directory, exist_ok=True)

        # save xml
        file_path = os.path.join("historical_currency_data", "latest.xml")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(base_data.text)
        
        print(f"xml for {base} saved at {file_path}")

    except Exception as e:
        print(f"[ERROR] Failed for currency {base}: {e}")

    