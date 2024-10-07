# hugging face finbert : https://huggingface.co/ProsusAI/finbert

# FinBERT는 금융 텍스트의 감정을 분석하기 위해 사전 학습된 NLP 모델.
# 이 모델은 대규모 금융 코퍼스를 사용하여 금융 도메인에서 BERT 언어 모델을 추가로 학습시키고, 금융 감정 분류를 위해 미세 조정
# Malo et al. (2014)의 Financial PhraseBank가 미세 조정을 위해 사용되었음.
# 자세한 내용은 논문 FinBERT: Financial Sentiment Analysis with Pre-trained Language Models와 Medium에 게시된 관련 블로그 게시물을 참조.

# 모델은 세 가지 레이블(긍정, 부정, 중립)에 대한 소프트맥스 출력을 제공.
# !pip3 install transformers feedparser requests torch tensorflow tf-keras(설치되면 모델 한 번 학습함)

# 1. Transformers (Hugging Face):
# 설명: Hugging Face에서 제공하는 라이브러리로, 자연어 처리(NLP)를 위한 사전 학습된 모델을 쉽게 사용할 수 있게 해준다.
# BERT, GPT, T5 같은 다양한 Transformer 기반 모델들을 지원하며, 모델의 학습, 추론, 튜닝 등을 간편하게 수행할 수 있다.
# 주요 기능: NLP 모델의 다운로드 및 사용, 학습, 미세 조정(fine-tuning) 등.


# 2. Feedparser:
# 설명: RSS 및 Atom 피드 파싱을 위한 파이썬 라이브러리. 다양한 포맷의 뉴스 피드 또는 블로그 피드를 읽고 분석하는 데 사용.
# 주요 기능: RSS/Atom 피드에서 텍스트, 이미지, 링크 등의 데이터를 추출.


# 4. Torch (PyTorch):
# 설명: Facebook에서 개발한 오픈소스 딥러닝 프레임워크로, 텐서 계산 및 동적 신경망을 빠르고 유연하게 구현할 수 있다. 특히, 연구 및 학습을 위한 도구로 많이 사용되며, GPU 가속을 지원.
# 주요 기능: 텐서 연산, 신경망 구축, 모델 학습 및 추론, GPU 가속.


# 5. TensorFlow:
# 설명: Google에서 개발한 딥러닝 프레임워크로, 머신러닝과 딥러닝 모델을 구축하고 학습시키는 데 사용. 대규모 데이터 처리에 최적화되어 있으며, 다양한 머신러닝 알고리즘을 지원.
# 주요 기능: 텐서 연산, 신경망 구축, 분산 학습, GPU/TPU 가속 지원.


# 6. tf.keras:
# 설명: Keras는 텐서플로우 내에서 제공되는 고수준 API로, 딥러닝 모델을 쉽게 정의하고 학습시킬 수 있게 해준다. TensorFlow와 긴밀하게 통합되어 있으며, 신경망을 간단하게 구축하고 훈련할 수 있는 인터페이스를 제공.
# 주요 기능: 신경망 모델 정의, 학습 루프 제어, 모델 컴파일 및 훈련, 평가 및 예측.


# Use a pipeline as a high-level helper
from transformers import pipeline
import feedparser


ticker = "ORCL" # 오라클 티커
keyword = 'oracle'


pipe = pipeline("text-classification", model="ProsusAI/finbert")

# print(pipe('Stocks rallied and the British pound gained.'))


rss_url = f'https://finance.yahoo.com/rss/headline?s={ticker}'
feed = feedparser.parse(rss_url)

total_score = 0
num_articles = 0

for i, entry in enumerate(feed.entries):
  if keyword.lower() not in entry.description.lower():
    continue

  print(f"Title: {entry.title}")
  print(f"Link: {entry.link}")
  print(f"Published: {entry.published}")
  print(f"Description: {entry.description}")

  sentiment = pipe(entry.description)[0]

  print(f"Sentiment: {sentiment["label"]} ({sentiment["score"]})")
  print("-" * 50)

  if sentiment['label'] == 'positive':
    total_score += sentiment['score']
    num_articles += 1
  elif sentiment['label'] == 'negative':
    total_score -= sentiment['score']
    num_articles += 1

final_score = total_score / num_articles
print(f'Ovarall Sentiment: {"positive" if total_score >= 0.15 else "negative" if total_score <= -0.15 else "neutral"} with score {final_score}')