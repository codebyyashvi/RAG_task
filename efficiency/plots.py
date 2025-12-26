import matplotlib.pyplot as plt

top_k = [1, 3, 5]
latency = [42, 55, 71]
f1_scores = [0.62, 0.81, 0.79]

plt.figure()
plt.plot(top_k, latency)
plt.xlabel("Top-K")
plt.ylabel("Latency (ms)")
plt.title("Latency vs Top-K")
plt.show()

plt.figure()
plt.plot(top_k, f1_scores)
plt.xlabel("Top-K")
plt.ylabel("F1 Score")
plt.title("F1 Score vs Top-K")
plt.show()
