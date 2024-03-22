# Side_Project_steam
사이드 프로젝트 스팀 게임 추천 서비스

A. 프로젝트 주제:
   - Steam 게임 태그를 기반으로 한 추천 시스템

B. 프로젝트 소개:
   - 이 프로젝트는 Steam 플랫폼의 게임 데이터를 활용하여 사용자 성향 맞춤 추천 시스템을 개발합니다.
   - 목표는 사용자의 게임 방식과 선호하는 취향을 분석하여 개인 맞춤 게임 추천 서비스를 제공하는 것입니다.

C. 기술 스택 또는 사용된 언어:
   - Python 3.9, Pandas, Matplotlib, Seaborn, Scikit-learn, BeautifulSoup, streamlit
   - TF-IDF : 각 게임의 태그를 TF-IDF로 벡터화하여 각 게임의 태그의 고유한 조합으로 표현을 한 다음, 이를 기반으로 사용자가 선택한 태그와 게임 간의 유사도를 계산하여 게임을 추천하는 방식을 사용하였습니다.

D. TF-IDF를 사용한 이유
   - cosine similarity : 코사인 유사도를 이용하여 각각의 게임 설명, 장르, 태그를 이용한 추천서비스를 만들었지만, 태그 선택수를 3개로 한정 짓다 보니 정확도가 너무 떨어지는 문제가 발생
   - konlpy - OKT : 리뷰를 이용해서 자연어 처리, 태그를 원핫인코딩 하여 상위 200개의 게임의 리뷰를 긍정 분석한다음 그와 관련된 태그를 학습시켜서 빅 데이터에 적용할려고 하였으나, 리뷰수가 너무많아 잔연어 처리시 램 문제가 발생 샘플링, 단어 제한, 리뷰수 제한을 하니 정확도가 떨어지는 문제가 발생

E. 사용 방법

  streamlit 주소 : https://sideprojectsteam-qwpsczrvdwuf2ouxyhkzmq.streamlit.app/
  
F. 팀원 소개 및 깃 주소
  - 김기인 : https://github.com/giintok
  - 서정무 : https://github.com/ExploreSeo
  - 손혜림 : https://github.com/hyerimson
  - 최서진 : https://github.com/seoJin145

G. 참고 자료 및 출처
  - 케글 데이터 : https://www.kaggle.com/datasets/fronkongames/steam-games-dataset 2024-01-18일자
  - <사용자 평점 기반 게임 추천 시스템>, Journal of the Korea Industrial Information Systems Research, 김종현, 조현정,김병만, 2018.09.19
  - <PC 게임 리뷰의 감성분석>, 2020 한국정보기술학회 종합학술대회, 박준렬, 김은지, 이재용, 유형진, 권순형, 김동년, 강태원
  - 크롤링 관련 https://www.youtube.com/watch?v=wwhJ32al364
  - Steam 공식 사이트 인기순위 https://store.steampowered.com/search/?filter=topsellers&os=win
  - 기획안 : https://docs.google.com/document/d/1q-01BLLLuYxJgBAzpztd2Yd9P1QmTote/edit

H. 라이센스
