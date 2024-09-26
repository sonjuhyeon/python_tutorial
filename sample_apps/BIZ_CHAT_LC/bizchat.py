import os
import sys
import io
from langchain import hub
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from collections import Counter
from langchain.schema import Document  # Document 클래스 임포트

from dotenv import load_dotenv
load_dotenv()
os.getenv("OPENAI_API_KEY")

loader = DirectoryLoader("./data", glob="*.txt", loader_cls=TextLoader)
documents = loader.load()
print(len(documents))