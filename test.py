import pandas as pd
from utils.preprocessing import preprocess_data
from utils.scoring import calculate_match_score

df = pd.read_excel("data/influencer_dataset_300_records.xlsx")

df = preprocess_data(df)

ranked_df = calculate_match_score(
    df,
    brand_category="travel",
    target_country="Spain"
)

print(ranked_df[['channel_name','match_score']].head(10))