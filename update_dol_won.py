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
    """Exchangerate API를 호출하여 달러-원 및 루블-원 환율 정보를 가져옴"""
    response = requests.get(URL)
    data = response.json()
    if data.get("result") == "success":  # API 응답 상태 확인
        krw_rate = data["conversion_rates"].get("KRW", "N/A")  # USD to KRW 환율
        rub_rate = data["conversion_rates"].get("RUB", "N/A")  # USD to RUB 환율
        return f"-미국 달러(USD) 환율: {krw_rate} 원 \n-러시아 루블(RUB) 환율: {rub_rate} 루블"
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


---
(저는 노어과라 러시아도 관심이 많답니다.)

---

⏳ 업데이트 시간: {now} (UTC)
---
자동 업데이트 봇에 의해 관리됩니다.
---
"""


    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()