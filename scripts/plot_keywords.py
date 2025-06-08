import matplotlib.pyplot as plt
import os
from collections import defaultdict

# Load theme_keywords_summary.txt
with open("outputs/theme_keywords_summary.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Parse into dictionary: data[bank_sentiment] = {keyword: count}
data = defaultdict(dict)
current_key = None

for line in lines:
    line = line.strip()
    if line.startswith("🔎 Top keywords for"):
        current_key = line.split(":")[0].split("for ")[1]
    elif current_key and line:
        try:
            keyword, count = line.split(":")
            data[current_key][keyword.strip()] = int(count.strip())
        except ValueError:
            continue

# Plot top 10 keywords for each group
os.makedirs("outputs/keyword_charts", exist_ok=True)

for key, keywords in data.items():
    sorted_kws = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:10]
    labels, counts = zip(*sorted_kws)

    plt.figure(figsize=(8, 5))
    plt.barh(labels[::-1], counts[::-1])
    plt.title(f"Top Keywords: {key}")
    plt.xlabel("Count")
    plt.tight_layout()
    safe_key = key.replace(" ", "_").replace(":", "").replace("/", "_")
    plt.savefig(f"outputs/keyword_charts/{safe_key}.png")
    plt.close()

print("✅ Keyword plots saved to: outputs/keyword_charts/")
