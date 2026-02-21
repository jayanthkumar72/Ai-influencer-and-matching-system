def calculate_match_score(df, brand_category=None, target_country=None):

    # Brand Match Feature
    if brand_category:
        df['brand_match'] = df['supported_brand_category'].apply(
            lambda x: 1 if x.lower() == brand_category.lower() else 0
        )
    else:
        df['brand_match'] = 0

    # Country Match Feature
    if target_country:
        df['country_match'] = df['country'].apply(
            lambda x: 1 if x.lower() == target_country.lower() else 0
        )
    else:
        df['country_match'] = 0

    # Weighted Match Score
    df['match_score'] = (
        0.30 * df['engagement_rate'] +
        0.25 * df['followers'] +
        0.20 * df['historical_success_score'] +
        0.15 * df['authenticity_score'] +
        0.05 * df['brand_match'] +
        0.05 * df['country_match']
    )

    return df.sort_values(by='match_score', ascending=False)