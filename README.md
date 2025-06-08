# B5W2: Customer Experience Analytics for Fintech Apps

## 🚀 Overview
This project analyzes customer reviews for mobile banking apps from three Ethiopian banks—CBE, BOA, and Dashen—using sentiment analysis and keyword extraction. It aims to uncover pain points and recommend UX improvements.

## 🧪 Objective
Help Omega Consultancy deliver data-driven insights to improve app features, stability, and support channels for banks.

---

## 🗂️ Repository Structure

├── scripts/
│ ├── scrape_reviews.py
│ ├── analyze_sentiment.py
│ ├── load_to_oracle.py
│ ├── plot_sentiment_distribution.py
│ └── plot_keywords.py
├── data/
│ └── raw_reviews.csv
├── outputs/
│ ├── reviews_with_sentiment.csv
│ ├── sentiment_distribution_by_bank.png
│ └── keyword_charts/
├── requirements.txt
├── README.md
└── report.md


---

## ✅ Tasks

### Task 1: Scraping
- Scraped 400+ reviews each for CBE, BOA, and Dashen using `google-play-scraper`.

### Task 2: Sentiment & Themes
- Analyzed sentiment using rule-based classification (`TextBlob/nltk`)
- Extracted top keywords by sentiment

### Task 3: Oracle DB
- Created tables `banks` and `reviews`
- Inserted 1200+ rows after cleaning & formatting

### Task 4: Visualization & Reporting
- Plotted sentiment distributions & top keywords
- Created final business report with actionable recommendations

---

## 📊 Key Outputs
- `outputs/reviews_with_sentiment.csv`: Cleaned dataset with sentiment
- `outputs/sentiment_distribution_by_bank.png`: Sentiment bar plot
- `outputs/keyword_charts/`: Bank-wise keyword plots
- `report.md`: Final summarized report

---

## 💡 Recommendations
- **CBE**: Improve transaction speed, optimize UI
- **BOA**: Fix crashes and loading bugs urgently
- **Dashen**: Leverage strengths; fix few reliability issues

---

## 🛠 Tech Stack
- Python, Pandas, NLTK, Matplotlib, Seaborn
- Oracle XE (local database)
- Git for version control

---

## 👥 Team
Facilitators: Mahlet, Kerod, Rediet, Rehmet  
Analyst: Kirubel Gizaw

---

## 📎 Submission
- Final report: `report.md`
- GitHub: [github.com/kirubhel/B5W2-Customer-Experience-Analytics](https://github.com/kirubhel/B5W2-Customer-Experience-Analytics)

