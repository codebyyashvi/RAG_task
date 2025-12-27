from evaluation import evaluate_retrieval
import os
import json

configs = [1, 3, 5]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_PATH = os.path.join(BASE_DIR, "data", "eval_queries.json")
OUT_PATH = os.path.join(BASE_DIR, "data", "experiment_results.json")

final_results = []

for k in configs:
    results = evaluate_retrieval(EVAL_PATH, top_k=k)
    avg_latency = sum(r["latency_ms"] for r in results) / len(results)
    avg_f1 = sum(r["f1"] for r in results) / len(results)

    final_results.append({
        "top_k": k,
        "avg_latency_ms": avg_latency,
        "avg_f1": avg_f1
    })

    print(f"\nTop-K = {k}")
    print(f"Avg Latency: {avg_latency:.2f} ms")
    print(f"Avg F1 Score: {avg_f1:.2f}")

with open(OUT_PATH, "w") as f:
    json.dump(final_results, f, indent=2)
