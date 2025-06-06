import pandas as pd
from textblob import TextBlob
from pathlib import Path

# Load cleaned reviews
df_path = Path("data/raw_reviews.csv")
df = pd.read_csv(df_path)

# Function to classify sentiment
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

# Apply sentiment analysis
df["sentiment"] = df["review"].fillna("").apply(get_sentiment)

# Save sentiment-labeled output
output_path = Path("outputs/reviews_with_sentiment.csv")
df.to_csv(output_path, index=False)

print(f"Sentiment analysis complete. Saved to: {output_path}")
print(df["sentiment"].value_counts())
