import json
from elasticsearch import Elasticsearch
from tqdm import tqdm
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "data.json")
es = Elasticsearch("http://localhost:9200")
INDEX_NAME = "tech_docs"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    documents = json.load(f)

for doc in tqdm(documents):
    es.index(
        index=INDEX_NAME,
        id=doc["doc_id"],  
        document=doc
    )

print("Data ingestion completed!")
