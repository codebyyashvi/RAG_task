from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
INDEX_NAME = "tech_docs"

mapping = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "1s"
    },
    "mappings": {
        "properties": {
            "doc_id": {"type": "keyword"},
            "title": {"type": "text"},
            "content": {"type": "text"},
            "category": {"type": "keyword"},
            "tags": {"type": "keyword"},
            "created_at": {
                "type": "date",
                "format": "yyyy-MM-dd"
            }
        }
    }
}

# Re-create index safely
if es.indices.exists(index=INDEX_NAME):
    es.indices.delete(index=INDEX_NAME)

es.indices.create(index=INDEX_NAME, body=mapping)
print("Index created successfully!")
