import pandas as pd

def clean_reviews():
    df = pd.read_csv("data/raw_reviews.csv")
    
    df.drop_duplicates(subset="review", inplace=True)
    df.dropna(subset=["review", "rating", "date"], inplace=True)
    df["date"] = pd.to_datetime(df["date"]).dt.date

    df.to_csv("data/bank_reviews_clean.csv", index=False)
    print("Cleaned data saved to data/bank_reviews_clean.csv")

if __name__ == "__main__":
    clean_reviews()