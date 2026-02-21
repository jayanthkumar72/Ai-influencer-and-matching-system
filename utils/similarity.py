import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(df, brand_category=None, target_country=None):

    # Create brand match feature
    if brand_category:
        df['brand_match'] = df['supported_brand_category'].apply(
            lambda x: 1 if x.lower() == brand_category.lower() else 0
        )
    else:
        df['brand_match'] = 0

    # Create country match feature
    if target_country:
        df['country_match'] = df['country'].apply(
            lambda x: 1 if x.lower() == target_country.lower() else 0
        )
    else:
        df['country_match'] = 0

    # Select feature columns for vector comparison
    feature_columns = [
        'engagement_rate',
        'followers',
        'historical_success_score',
        'authenticity_score',
        'brand_match',
        'country_match'
    ]

    influencer_matrix = df[feature_columns].values

    # Create ideal brand vector (target profile)
    # Ideal influencer should have:
    # High engagement, followers, success, authenticity, and match conditions

    brand_vector = np.array([1, 1, 1, 1, 1, 1])

    # Calculate cosine similarity
    similarities = cosine_similarity(
        influencer_matrix,
        brand_vector.reshape(1, -1)
    )

    df['similarity_score'] = similarities

    return df.sort_values(by='similarity_score', ascending=False)