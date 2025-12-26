from elasticsearch import Elasticsearch
import time

es = Elasticsearch("http://localhost:9200")
INDEX_NAME = "tech_docs"


def semantic_search(query):
    start = time.time()

    response = es.search(
        index=INDEX_NAME,
        size=5,
        query={
            "multi_match": {
                "query": query,
                "fields": ["title", "content"]
            }
        }
    )

    latency = (time.time() - start) * 1000
    print(f"\nQuery: {query}")
    print(f"Latency: {latency:.2f} ms")

    for hit in response["hits"]["hits"]:
        src = hit["_source"]
        print("-", src["title"], "| Category:", src["category"])


semantic_search("Zero Trust security model")
semantic_search("API authentication")


def filtered_search(query, category):
    response = es.search(
        index=INDEX_NAME,
        query={
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["title", "content"]
                    }
                },
                "filter": {
                    "term": {"category.keyword": category}
                }
            }
        }
    )

    print(f"\nFiltered Query: {query} | Category: {category}")
    for hit in response["hits"]["hits"]:
        print("-", hit["_source"]["title"])


filtered_search("security", "Security")


def tag_search(tag):
    response = es.search(
        index=INDEX_NAME,
        query={
            "term": {
                "tags.keyword": tag
            }
        }
    )

    print(f"\nTag Search: {tag}")
    for hit in response["hits"]["hits"]:
        print("-", hit["_source"]["title"])


tag_search("security")
