from flask import Flask, render_template, request
import pandas as pd

from utils.preprocessing import preprocess_data
from utils.scoring import calculate_match_score

app = Flask(__name__)

# Load dataset once
df = pd.read_excel("data/influencer_dataset_300_records.xlsx")
df = preprocess_data(df)

@app.route("/", methods=["GET", "POST"])
def index():

    results = None

    categories = sorted(df['supported_brand_category'].unique())
    countries = sorted(df['country'].unique())

    if request.method == "POST":
        selected_category = request.form.get("category")
        selected_country = request.form.get("country")

        ranked_df = calculate_match_score(
            df.copy(),
            brand_category=selected_category,
            target_country=selected_country
        )

        results = ranked_df[['channel_name', 'match_score']].head(10).to_dict(orient="records")

    return render_template(
        "index.html",
        categories=categories,
        countries=countries,
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)