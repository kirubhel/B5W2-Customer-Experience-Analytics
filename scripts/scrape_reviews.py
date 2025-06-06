from google_play_scraper import Sort, reviews
import pandas as pd

BANK_APPS = {
    "CBE": "com.cbe.mobile.android",
    "BOA": "com.boa.bankapp",
    "Dashen": "com.dashen.bankapp" 
}

def scrape_bank_reviews(app_name, app_id, n_reviews=400):
    print(f"Scraping {app_name}...")
    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=n_reviews
    )

    # 🔍 Debug: Show a sample of what you’re actually getting
    if not result:
        print(f"⚠️ No reviews returned for {app_name}. Check package ID.")
    else:
        print(result[0])  # See keys like 'content', 'score', 'at'

    df = pd.DataFrame(result)
    df["bank"] = app_name
    df["source"] = "Google Play"

    # 🔐 Use .get() in case keys are missing
    return df[["content", "score", "at", "bank", "source"]]
def main():
    all_reviews = []
    for bank, app_id in BANK_APPS.items():
        df = scrape_bank_reviews(bank, app_id)
        all_reviews.append(df)
    
    final_df = pd.concat(all_reviews, ignore_index=True)
    final_df.columns = ["review", "rating", "date", "bank", "source"]
    final_df.to_csv("data/raw_reviews.csv", index=False)
    print("Saved scraped reviews to data/raw_reviews.csv")

if __name__ == "__main__":
    main()