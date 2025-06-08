import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data with sentiment
df = pd.read_csv("outputs/reviews_with_sentiment.csv")

# Group and count
sentiment_counts = df.groupby(["bank", "sentiment"]).size().reset_index(name="count")

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=sentiment_counts, x="bank", y="count", hue="sentiment")
plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.legend(title="Sentiment")
plt.tight_layout()

# Save plot
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/sentiment_distribution_by_bank.png")
plt.show()
