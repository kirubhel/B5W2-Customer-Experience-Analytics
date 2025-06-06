# B5W2: Customer Experience Analytics for Fintech Apps

This project is part of the 10 Academy's B5W2 challenge, focused on analyzing user feedback on Ethiopian banking apps through customer reviews on the Google Play Store.

## 🔍 Objective

Omega Consultancy aims to help banks like CBE, BOA, and Dashen improve their mobile apps by:
- Scraping real customer reviews
- Analyzing sentiment and user themes
- Identifying satisfaction drivers and pain points
- Recommending improvements

## 📦 Data Sources

- **Google Play Store reviews** for:
  - Commercial Bank of Ethiopia (CBE)
  - Bank of Abyssinia (BOA)
  - Dashen Bank

## 📊 Methodology

### Step 1: Web Scraping
- Used `google-play-scraper` to extract:
  - Review text
  - Rating (1–5)
  - Review date
  - App name

### Step 2: Preprocessing
- Removed duplicates and nulls
- Normalized dates to `YYYY-MM-DD`
- Saved as `bank_reviews_clean.csv` with columns:
  - `review`, `rating`, `date`, `bank`, `source`

### Step 3: Early Analysis *(ongoing)*
- Performed basic sentiment scoring using `TextBlob`
- Grouped by bank and rating
- Keyword previews show recurring issues like login problems, app crashes, and UI lag

## 📁 Repo Structure

├── data/
│   └── bank_reviews_clean.csv
├── notebooks/
│   └── scraping.ipynb
├── scripts/
│   ├── scrape_reviews.py
│   └── clean_reviews.py
├── requirements.txt
├── .gitignore
├── README.md


## 🔧 Tools & Libraries

- Python, Pandas, Numpy
- `google-play-scraper`
- `TextBlob`, `nltk`
- Matplotlib, Seaborn

## 🧠 Next Steps

- Apply `DistilBERT` or `VADER` for deeper sentiment classification
- Perform thematic clustering using TF-IDF + spaCy
- Visualize insights and build stakeholder-friendly plots
- Store data in Oracle DB

## 👥 Team
Lead Analyst: Kirubel Gizaw  
Platform: 10 Academy - Tenx