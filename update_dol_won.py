import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# API 키 설정
API_KEY = os.getenv("DOLLARWON_API_KEY")
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

# README 파일 경로
README_PATH = "README.md"

def get_exchange_rate():
    """Exchangerate API를 호출하여 달러-원 환율 정보를 가져옴"""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        if "conversion_rates" in data and "KRW" in data["conversion_rates"]:
            krw_rate = data["conversion_rates"]["KRW"]  # USD to KRW 환율
            return f"미국 달러(USD) 환율: {krw_rate} 원"
    return "환율 정보를 가져오는 데 실패했습니다."

def update_readme():
    """README.md 파일을 업데이트"""
    exchange_info = get_exchange_rate()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""


# USD-KRW Exchange Rate Status(달러-원 환율)

* IMF 금융위기 환율(달러) 최고 피크 1$ - 2000원
* 2008년 금융위기 환율(달러) 최고 피크 1$ - 1600원
* 코로나 쇼크 환율(달러) 최고 피크 1$ - 1300원



과연... 지금은??!!


## 현재 달러-원 환율
> {exchange_info}

⏳ 업데이트 시간: {now} (UTC)

---
"""


    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()