import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(df):

    # Handle missing country values
    df['country'] = df['country'].fillna("Unknown")

    # Ensure numeric columns are correct type
    numeric_cols = [
        'followers',
        'engagement_rate',
        'avg_likes',
        'historical_success_score',
        'authenticity_score'
    ]

    df[numeric_cols] = df[numeric_cols].astype(float)

    # Scale numeric features (0–1)
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df