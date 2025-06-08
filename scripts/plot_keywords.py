import matplotlib.pyplot as plt
import os
from collections import defaultdict

# Load theme_keywords_summary.txt
with open("outputs/theme_keywords_summary.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Parse into dictionary
data = defaultdict(dict)
current_key = None

for line in lines:
    line = line.strip()
    
    # Match both "Top keywords for" and "🔎 Top keywords for"
    if "Top keywords for" in line:
        parts = line.split("for ")[-1].split(":")[0].strip()
        current_key = parts
        print(f"🧠 Detected: {current_key}")
        
    elif current_key and ":" in line:
        try:
            keyword, count = line.split(":")
            data[current_key][keyword.strip()] = int(count.strip())
        except ValueError:
            print(f"⚠️ Couldn’t parse line: {line}")
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
