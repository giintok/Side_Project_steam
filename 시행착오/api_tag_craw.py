# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:39:30 2024

@author: goldg
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# app_ids.csv 파일에서 app_id 불러오기
appids = pd.read_csv('app_ids.csv')['AppID']

# 결과를 저장할 리스트 생성
results = []

# 각 app_id에 대해 반복
for appid in appids[1500:]:
    # 게임 페이지 URL 생성
    url = f'https://store.steampowered.com/app/{appid}/'

    # GET 요청을 보내고 응답 받기
    response = requests.get(url)

    # 딜레이 추가
    time.sleep(3)

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # popular_tags 클래스를 가진 div 태그 찾기
    popular_tags_div = soup.find('div', class_='glance_tags popular_tags')

    # popular_tags_div 안에 있는 모든 a 태그를 찾아서 텍스트 추출
    tags = [tag.text.strip() for tag in popular_tags_div.find_all('a', class_='app_tag')]

    # 결과를 딕셔너리로 저장
    result = {'app_id': appid, 'tags': tags}
    results.append(result)

    # 결과 출력
    print(result)

# 결과를 데이터프레임으로 변환
df = pd.DataFrame(results)

# 결과를 파일로 저장
df.to_csv('game_tags_2500.csv', index=False)
