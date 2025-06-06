from tqdm import tqdm
import pandas as pd
from google_play_scraper import reviews, Sort

BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

def scrape_bank_reviews(app_name, app_id, n_reviews=400):
    try:
        print(f"🔍 Scraping {app_name} ({app_id})...")
        result, _ = reviews(
            app_id,
            lang="en",
            country="us",
            sort=Sort.NEWEST,
            count=n_reviews
        )
        if not result:
            print(f"⚠️ No reviews returned for {app_name}.")
            return pd.DataFrame()  # Empty
        df = pd.DataFrame(result)
        df["bank"] = app_name
        df["source"] = "Google Play"
        df = df[["content", "score", "at", "bank", "source"]]
        return df
    except Exception as e:
        print(f"❌ Error scraping {app_name}: {e}")
        return pd.DataFrame()

def main():
    all_reviews = []
    for bank, app_id in tqdm(BANK_APPS.items(), desc="Scraping Progress"):
        df = scrape_bank_reviews(bank, app_id)
        if not df.empty:
            all_reviews.append(df)
    if all_reviews:
        final_df = pd.concat(all_reviews, ignore_index=True)
        final_df.columns = ["review", "rating", "date", "bank", "source"]
        final_df.to_csv("data/raw_reviews.csv", index=False)
        print("✅ Saved scraped reviews to data/raw_reviews.csv")
    else:
        print("🚫 No reviews scraped. Check network or app IDs.")

if __name__ == "__main__":
    main()