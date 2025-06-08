import pandas as pd
import oracledb

# Config (replace with your actual credentials)
user = "your_user"
password = "your_password"
dsn = "localhost/orclpdb1"  # adjust for your Oracle instance

# Connect
conn = oracledb.connect(user=user, password=password, dsn=dsn)
cur = conn.cursor()

# Create or fetch bank IDs
banks = ["CBE", "BOA", "Dashen"]
bank_ids = {}

for bank in banks:
    cur.execute("SELECT id FROM banks WHERE name = :1", [bank])
    result = cur.fetchone()
    if result:
        bank_ids[bank] = result[0]
    else:
        cur.execute("INSERT INTO banks (name) VALUES (:1) RETURNING id INTO :2", [bank, cur.var(int)])
        bank_ids[bank] = cur.getimplicitresults()[0][0]

# Load CSV
df = pd.read_csv("outputs/reviews_with_sentiment.csv")

inserted = 0
for _, row in df.iterrows():
    try:
        cur.execute("""
            INSERT INTO reviews (review_text, rating, review_date, bank_id, sentiment, source)
            VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6)
        """, [row['review'], row['rating'], row['date'], bank_ids[row['bank']], row['sentiment'], row['source']])
        inserted += 1
    except Exception as e:
        print(f"⚠️ Skipped a row due to error: {e}")

conn.commit()
print(f"✅ Successfully inserted {inserted} rows.")
