import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# API 키 설정
API_KEY = os.getenv("DOLLARWON_API_KEY")
SEARCHDATE = datetime.now().strftime("%Y%m%d")  # YYYYMMDD 형식
URL = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate={SEARCHDATE}&data=AP01"

# README 파일 경로
README_PATH = "README.md"

def get_exchange_rate():
    """한국 수출입은행 API를 호출하여 달러-원 환율 정보를 가져옴"""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item["cur_unit"] == "USD":  # 미국 달러 정보 필터링
                usd_rate = item["deal_bas_r"]  # 매매 기준율
                return f"미국 달러(USD) 환율: {usd_rate} 원"
    return "환율 정보를 가져오는 데 실패했습니다."

def update_readme():
    """README.md 파일을 업데이트"""
    exchange_info = get_exchange_rate()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""

# USD-KRW Exchange Rate Status

IMF 금융위기 환율(달러) 최고 피크 1$ - 2000원
2008년 금융위기 환율(달러) 최고 피크 1$ - 1600원
코로나 쇼크 환율(달러) 최고 피크 1$ - 1300원
과연... 지금은??!!

## 현재 달러-원 환율
> {exchange_info}

⏳ 업데이트 시간: {now} (UTC)

(이 리포지토리는 한국 수출입은행 API를 사용하여 달러-원 환율 정보를 자동으로 업데이트합니다.)
---
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()


