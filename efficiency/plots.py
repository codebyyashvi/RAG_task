import json
import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "experiment_results.json")

with open(DATA_PATH, "r") as f:
    data = json.load(f)

top_k = [d["top_k"] for d in data]
latency = [d["avg_latency_ms"] for d in data]
f1_scores = [d["avg_f1"] for d in data]

plt.figure()
plt.plot(top_k, latency, marker="o")
plt.xlabel("Top-K")
plt.ylabel("Latency (ms)")
plt.title("Latency vs Top-K")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(top_k, f1_scores, marker="o")
plt.xlabel("Top-K")
plt.ylabel("F1 Score")
plt.title("F1 Score vs Top-K")
plt.grid(True)
plt.show()
