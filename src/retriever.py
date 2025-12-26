from elasticsearch import Elasticsearch
from config import ELASTICSEARCH_URL, INDEX_NAME

es = Elasticsearch(ELASTICSEARCH_URL)

def retrieve_documents(query, top_k=3):
    response = es.search(
        index=INDEX_NAME,
        size=top_k,
        query={
            "multi_match": {
                "query": query,
                "fields": ["title", "content", "tags"]
            }
        }
    )

    documents = []
    for hit in response["hits"]["hits"]:
        src = hit["_source"]
        documents.append({
            "doc_id": src["doc_id"], 
            "title": src["title"],
            "content": src["content"],
            "category": src["category"]
        })

    return documents
