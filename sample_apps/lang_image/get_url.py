import base64
import requests
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# 이미지를 URL에서 다운로드하여 base64로 인코딩하는 함수
def encode_image_from_url(image_url):
    try:
        # URL에서 이미지를 다운로드
        response = requests.get(image_url)
        if response.status_code == 200:
            # 이미지 데이터를 base64로 인코딩
            return base64.b64encode(response.content).decode('utf-8')
        else:
            print(f"Failed to download image, status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading or encoding image: {e}")
        return None

# GPT API 호출 함수
def call_gpt_with_image(image_base64):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }

    payload = {
        "model": "dall-e-3",
        "messages": [
            {
                'role': 'system',
                'content': 'You are an image classification model. You will classify the input image and return the result in JSON format with the following structure: {"recycle": "true/false", "classify": "bottle/plastic/clothing/paper"}. If the image cannot be classified or recognized, respond with {"error": "인식할 수 없는 이미지 1"}.'
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

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_json = response.json()
        return response_json
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # 이미지 URL
    image_url = "https://img.freepik.com/free-vector/glass-bottles_23-2147506789.jpg"

    # 이미지 다운로드 및 인코딩
    encoded_image = encode_image_from_url(image_url)

    if encoded_image:
        # GPT 모델에 이미지를 전달하고 결과를 받음
        result = call_gpt_with_image(encoded_image)
        print(result)
    else:
        print({"error": "Failed to encode image from URL"})
