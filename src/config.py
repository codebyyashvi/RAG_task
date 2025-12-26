import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL")
INDEX_NAME = os.getenv("INDEX_NAME")
