# Ai-influencer-and-matching-system
AI Influencer Matching System that ranks influencers using engagement rate, reach, authenticity, and campaign success metrics. Built with Flask and Scikit-learn, it supports brand and country-based filtering with weighted scoring and cosine similarity ranking.
# AI Influencer Matching & Recommendation System

## 🚀 Project Overview

AI Influencer Matching System is a Flask-based web application that ranks and recommends influencers based on engagement rate, reach, authenticity, and campaign success metrics.

The system supports brand category and country-based filtering using:

- ✅ Weighted Scoring Model
- ✅ Cosine Similarity (Vector-Based Matching)

This project simulates a real-world AI-driven influencer marketing platform.

---

## 🎯 Key Features

- 🔍 Brand Category Filtering
- 🌍 Country-Based Matching
- 📊 Engagement & Reach-Based Ranking
- 🧠 Historical Campaign Success Scoring
- 🔐 Authenticity Scoring
- 📈 Cosine Similarity Matching (Advanced Option)
- 🌐 Flask Web Interface with Dropdown Inputs
- 🚀 Deployable via Render

---

## 🧠 Matching Logic

### Option A – Weighted Scoring

Match Score is calculated using:

- 30% Engagement Rate  
- 25% Followers  
- 20% Historical Success Score  
- 15% Authenticity Score  
- 5% Brand Match  
- 5% Country Match  

---

### Option B – Cosine Similarity

Influencer features are converted into vectors and compared with an ideal brand profile using cosine similarity to rank top influencers.

---

## 🏗 Project Structure
ai-influencer-matching-system/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── data/
│ └── influencer_dataset_300_records.xlsx
│
├── templates/
│ └── index.html
│
├── utils/
│ ├── preprocessing.py
│ ├── scoring.py
│ ├── similarity.py
│ └── init.py

---

## ⚙️ Tech Stack

- Python
- Flask
- Pandas
- Scikit-learn
- OpenPyXL
- Gunicorn (for deployment)

---

## 📊 Dataset

Custom dataset with 300 influencer records including:

- Influencer ID
- Channel Name
- Category
- Followers
- Engagement Rate
- Avg Likes
- Country
- Supported Brand Category
- Historical Success Score
- Authenticity Score

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/ai-influencer-matching-system.git
cd ai-influencer-matching-system
pip install -r requirements.txt
python app.py

open browser :
    http://127.0.0.1:5000/