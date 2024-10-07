# import base64
# import requests
# from dotenv import load_dotenv
# import os
# from PIL import Image
# import io

# # 환경 변수 로드
# load_dotenv()

# # 파일 확장자 지원을 위한 함수
# def resize_and_encode_image(image_path, size=(300, 300)):
#   try:
#     # 허용되는 확장자 목록
#     allowed_extensions = ['jpg', 'jpeg', 'png']
#     extension = image_path.split('.')[-1].lower()

#     if extension not in allowed_extensions:
#       return None

#     # 이미지 열기 및 리사이즈
#     with Image.open(image_path) as img:
#       img.thumbnail(size)  # 이미지 리사이즈 (비율 유지)
#       buffered = io.BytesIO()
#       img.save(buffered, format=img.format)  # 이미지 저장 (버퍼에)
#       return base64.b64encode(buffered.getvalue()).decode('utf-8')  # base64 인코딩

#   except Exception as e:
#     print(f"Error: {e}")
#     return None

# # 이미지 파일을 base64로 인코딩 (여러 확장자 지원)
# image_path = "./images/cloth1.jpg"  # 이미지 파일 경로
# image_base64 = resize_and_encode_image(image_path)

# # https://platform.openai.com/usage

# # base64 인코딩 실패 시 메시지 출력
# if not image_base64:
#   print({
#     "error": "인식할 수 없는 이미지 0"
#   })
# else:
#     # 헤더 설정
#     headers = {
#       "Content-Type": "application/json",
#       "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
#     }

#     # 프롬프트 수정: JSON 형식으로 응답하도록 요청
#     payload = {
#       "model": "dall-e-3",
#       "messages": [
#         {
#           'role': 'system',
#           'content': 'You are an image classification model. You will classify the input image and return the result in JSON format with the following structure: {"recycle": "true/false", "classify": "bottle/plastic/clothing/paper"}. If the image cannot be classified or recognized, respond with {"error": "인식할 수 없는 이미지 2"}.'
#         },
#         {
#           'role': 'user',
#           'content': 'Classify the waste in the image and respond in JSON format.'
#         },
#         {
#           'role': 'user',
#           'content': f"![image](data:image/jpg;base64,{image_base64})"
#         }
#       ],
#       "max_tokens": 500,
#     }

#     # API 요청
#     try:
#       response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#       response_json = response.json()

#       # API 응답이 제대로 되었는지 확인하고 예외 처리
#       if 'choices' in response_json and len(response_json['choices']) > 0:
#         print(response_json['choices'][0]['message']['content'])
#         print(response_json)
#       else:
#         # 예외 상황 처리: choices를 찾지 못한 경우
#         print({"error": "인식할 수 없는 이미지 2"})
#         print(response_json)

#     except Exception as e:
#       # 예외 상황 처리: API 요청 실패 시
#       print({"error": "API request failed", "details": str(e)})

import base64
import requests
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# 파일 확장자 지원을 위한 함수
def encode_image(image_path):
  try:
    # 허용되는 확장자 목록
    allowed_extensions = ['jpg', 'jpeg', 'png']
    extension = image_path.split('.')[-1].lower()
    
    if extension not in allowed_extensions:
      return None
    
    with open(image_path, 'rb') as f:
      return base64.b64encode(f.read()).decode('utf-8')
  except Exception as e:
    return None

# 이미지 파일을 base64로 인코딩 (여러 확장자 지원)
image_path = "./images/pl2.jpeg"  # 이미지 파일 경로
image_base64 = encode_image(image_path)

# base64 인코딩 실패 시 메시지 출력
if not image_base64:
  print({
    "error": "인식할 수 없는 이미지0"
  })
else:
  # 헤더 설정
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
  }

  # 프롬프트 수정: JSON 형식으로 응답하도록 요청
  payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        'role': 'system',
        'content': 'You are an image classification model. You will classify the input image and return the result in JSON format with the following structure: {"recycle": "true/false", "classify": "bottle/plastic/clothing/paper"}. If the image cannot be classified or recognized, respond with {"error": "인식할 수 없는 이미지 2"}.'
      },
      {
        'role': 'user',
        'content': 'Classify the waste in the image and respond in JSON format.'
      },
      {
        'role': 'user',
        'content': f"![image](data:image/jpg;base64,{image_base64})"
      }
    ],
      "max_tokens": 500,
  }

  # API 요청
  try:
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()
    
    # API 응답이 제대로 되었는지 확인하고 예외 처리
    if 'choices' in response_json and len(response_json['choices']) > 0:
      print(response_json['choices'][0]['message']['content'])
    else:
      # 예외 상황 처리: choices를 찾지 못한 경우
      print({"error": "인식할 수 없는 이미지 1"})
      print(response_json)
  
  except Exception as e:
    # 예외 상황 처리: API 요청 실패 시
    print({"error": "API request failed", "details": str(e)})
