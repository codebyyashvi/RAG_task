import time
import json
import sys 
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")

sys.path.append(SRC_PATH)

from retriever import retrieve_documents

def precision_recall_f1(retrieved_ids, relevant_ids):
    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)

    tp = len(retrieved & relevant)
    fp = len(retrieved - relevant)
    fn = len(relevant - retrieved)

    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0

    return precision, recall, f1


def evaluate_retrieval(eval_file, top_k=3):
    with open(eval_file, "r") as f:
        data = json.load(f)

    results = []

    for item in data:
        start = time.time()
        docs = retrieve_documents(item["query"], top_k)
        latency = (time.time() - start) * 1000

        retrieved_ids = [doc.get("doc_id") for doc in docs]
        precision, recall, f1 = precision_recall_f1(
            retrieved_ids, item["relevant_doc_ids"]
        )

        results.append({
            "query": item["query"],
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "latency_ms": latency
        })

    return results
