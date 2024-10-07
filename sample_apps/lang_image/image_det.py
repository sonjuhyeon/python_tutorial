from pydantic.v1 import BaseModel, Field
import base64
from langchain.chains import TransformChain
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import os
from PIL import Image
import io
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

class ImageInformation(BaseModel):
  car: bool = Field(
    ...,
    example=True,
    description="Set to True if image contains a trash; otherwise, return False.",
  )
  color: str = Field(
    ...,
    example="red",
    description="The classifications of the trash. Possible values are: 'can', 'bottle', 'paper', 'plastic', or 'none' if no trash is detected.",
  )


inputs = {
  "image_path": "./images/bottle.jpeg"
}


def compress_image(image_path, max_size=(500, 500)):
  # 이미지를 압축하여 크기를 줄임
  image = Image.open(image_path)
  image.thumbnail(max_size)
  byte_array = io.BytesIO()
  image.save(byte_array, format="JPEG")
  return byte_array.getvalue()


def encode_image(image_path):
  compressed_image = compress_image(image_path)
  return base64.b64encode(compressed_image).decode("utf-8")


def load_image(inputs):
  image_path = inputs["image_path"]
  image_base64 = encode_image(image_path)
  return {"image": image_base64}


load_image_chain = TransformChain(
  input_variables=["image_path"], output_variables=["image"], transform=load_image
)


# def split_input(text, max_length=1000):
#   # 입력 텍스트를 주어진 길이로 분할
#   return [text[i:i+max_length] for i in range(0, len(text), max_length)]


def image_model(inputs):
  model: ChatOpenAI = ChatOpenAI(
    temperature=0.5,
    model="gpt-4o-2024-05-13",
    max_tokens=512,  # 출력 토큰 수 제한
  )
 
  # # 긴 프롬프트를 분할하여 처리
  # prompt = inputs["prompt"]
  # text_chunks = split_input(prompt, 1000)
  # responses = []


  # 모델에 JSON 형식으로 응답을 요구하는 명확한 프롬프트
  prompt = f"""Analyze the following image and return a JSON with the following format:
              {{
                  "trash": boolean,
                  "classifications": string
              }}.
              Only use the following values for "classifications": "can", "bottle", "paper", or "plastic".
              Here is the image in base64 format: {inputs['image']}.
              """
 
  msg = model.invoke(
    [
      HumanMessage(
          content=prompt
      )
    ]
  )
  return msg.content
 
  # # 응답 결과 결합
  # final_response = " ".join(responses)
  # return final_response


parser = JsonOutputParser(pydantic_object=ImageInformation)


def get_image_information(image_path: str) -> dict:
  vision_prompt = """이미지가 쓰레기 인지 아닌지를 알려주세요.
  다음의 예시에 따라 인식 결과를 반환해 주세요.
  # Example 1
  classifications: can, bottle
  trash: True
  # Example 2
  classifications: none
  trash: False
  # Example 3 - There is a trash but none of the valid classifications
  classifications: none
  trash: True
  """
 
  vision_chain = load_image_chain | image_model | parser
  try:
    return vision_chain.invoke(
      {"image_path": f"{image_path}", "prompt": vision_prompt}
    )
  except OutputParserException as e:
    print(f"Parser error: {str(e)}")
    return {
      "car": False,
      "color": "none",
    }
  except Exception as e:
    print(f"General error: {str(e)}")
    return {
      "car": False,
      "color": "none",
    }


if __name__ == "__main__":
  red_car = get_image_information("./images/bottle.jpeg")
  print("Red car:")
  print(red_car)