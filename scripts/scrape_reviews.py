from google_play_scraper import Sort, reviews
import pandas as pd
from tqdm import tqdm

def fetch_reviews(app_id, bank_name, n_reviews=400):
    all_reviews = []
    count = 0
    next_token = None

    while count < n_reviews:
        batch, next_token = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=100,
            continuation_token=next_token
        )

        for review in batch:
            all_reviews.append({
                "review": review["content"],
                "rating": review["score"],
                "date": review["at"].date().isoformat(),
                "bank": bank_name,
                "source": "Google Play"
            })

        count += len(batch)
        if not next_token:
            break

    return pd.DataFrame(all_reviews)

if __name__ == "__main__":
    apps = {
        "CBE": "com.ethiomobile.cbe",
        "BOA": "com.bankofabyssinia.mobilebanking",
        "Dashen": "com.mbanking.dashenbank"
    }

    all_dfs = []

    for bank, app_id in tqdm(apps.items()):
        df = fetch_reviews(app_id, bank)
        all_dfs.append(df)

    final_df = pd.concat(all_dfs, ignore_index=True).drop_duplicates()
    final_df.to_csv("data/cleaned_reviews.csv", index=False)
    print("Saved reviews to data/cleaned_reviews.csv")
