import pandas as pd
import random
import re
import os
from konlpy.tag import Okt

#리뷰데이터 리뷰수 상위 200개 게임 10개씩 짤라서 토큰화 작업한 코드
basic_path = os.path.dirname(__file__)
basic_file_path = os.path.join(basic_path, 'data')

# 게임 파일 경로
file_path = os.path.join(basic_file_path, 'reviews_final.csv')
df = pd.read_csv(file_path)

# 상위 200개 게임 선택
review_counts_per_game = df['game_id'].value_counts()
top_200_games = review_counts_per_game.nlargest(200)

# 자연어 처리 함수 정의
def preprocess_korean(review):
    # 한글, 숫자만 남기고 제거
    review = re.sub(r'[^가-힣0-9\s]', '', review)
    # 형태소 분석을 위한 Okt 초기화
    okt = Okt()
    # 토큰화
    tokens = okt.morphs(review)
    return tokens

# 상위 게임을 처리하는 함수
def process_top_game(game_id):
    game_reviews = df[df['game_id'] == game_id]['review'].tolist()
    sampled_reviews = random.sample(game_reviews, min(100, len(game_reviews)))
    game_tokens = []
    for review in sampled_reviews:
        processed_review = preprocess_korean(review)
        game_tokens.append(" ".join(processed_review))
    # 토큰화된 리뷰를 파일로 저장
    with open(f"tokenized_reviews_game_{game_id}.txt", "a", encoding="utf-8") as f:
        for token in game_tokens:
            f.write(token + "\n")

# 상위 10개 게임 처리
for game_id in top_200_games.index[180:200]:
    process_top_game(game_id)
