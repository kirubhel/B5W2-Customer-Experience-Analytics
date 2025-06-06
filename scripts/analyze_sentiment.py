import pandas as pd
from textblob import TextBlob
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

# ----------------------------
# Step 1: Load and Validate CSV
# ----------------------------
df_path = Path("data/raw_reviews.csv")  # Adjust if needed

if not df_path.exists():
    raise FileNotFoundError(f"❌ File not found: {df_path}")

df = pd.read_csv(df_path)

if df.empty:
    raise ValueError("❌ CSV file is empty. Rerun scraping first.")

# ----------------------------
# Step 2: Sentiment Analysis
# ----------------------------

def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["review"].fillna("").apply(get_sentiment)

# Save with sentiment
output_file = Path("outputs/reviews_with_sentiment.csv")
output_file.parent.mkdir(exist_ok=True)
df.to_csv(output_file, index=False)
print(f"✅ Sentiment analysis complete. Saved to: {output_file}")
print(df["sentiment"].value_counts())

# ----------------------------
# Step 3: Thematic Keyword Extraction
# ----------------------------

# Download stopwords if not already downloaded
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def tokenize_and_clean(text):
    text = str(text).lower()
    words = text.split()
    cleaned = [
        word.strip(string.punctuation)
        for word in words
        if word.isalpha() and word not in stop_words and len(word) > 2
    ]
    return cleaned

grouped_keywords = {}

for bank in df["bank"].unique():
    for sentiment in ["positive", "neutral", "negative"]:
        key = f"{bank}_{sentiment}"
        reviews_subset = df[(df["bank"] == bank) & (df["sentiment"] == sentiment)]["review"].dropna()

        all_words = []
        for review in reviews_subset:
            all_words.extend(tokenize_and_clean(review))

        word_counts = Counter(all_words).most_common(15)
        grouped_keywords[key] = word_counts

# Print keywords to console
for group, keywords in grouped_keywords.items():
    print(f"\n🔎 Top keywords for {group}:")
    for word, count in keywords:
        print(f"  {word}: {count}")

# Save to file
keywords_output = Path("outputs/theme_keywords_summary.txt")
with open(keywords_output, "w") as f:
    for group, keywords in grouped_keywords.items():
        f.write(f"\nTop keywords for {group}:\n")
        for word, count in keywords:
            f.write(f"{word}: {count}\n")

print(f"\n✅ Thematic keywords saved to: {keywords_output}")
