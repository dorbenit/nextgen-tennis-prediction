# NextGen Tennis Prediction 🎾

This project aims to identify promising young tennis players based on their performance in ATP Challenger tournaments, and predict whether they are likely to reach a Grand Slam semi-final in the future.

##  Objective
Build a predictive pipeline to analyze early-career performance indicators and assess the potential of players to reach elite levels in men's tennis (Grand Slam semi-finals).

### Why Challenger tournaments?
The ATP Challenger Tour serves as a key stepping stone for rising tennis players — it’s where most young professionals begin to build their careers and rankings before breaking into higher-level ATP and Grand Slam events. By focusing on Challenger-level matches, we aim to capture performance patterns at the start of a player's journey.

##  Work Done So Far
- **Data Collection**: Merged historical ATP match data (1998–2024) from multiple sources.
- **Challenger Filtering**: Isolated Challenger-level matches to analyze early-career performance.
- **Data Cleaning**: Standardized column types, handled missing values, and removed inconsistencies using Pandas.
- **Player Feature Construction**: Engineered features such as player age, match outcomes, and recent performance metrics.
- **Grand Slam Results File**: Created a cleaned dataset of Grand Slam match results to identify players who reached the semi-finals — for use in future labeling and evaluation.

## Notebooks
All data exploration, cleaning, and preliminary analysis steps are documented in Jupyter notebooks for clarity and reproducibility.

You can browse them in the notebooks/ directory.
These notebooks provide an interactive view of how the datasets were prepared, cleaned, and analyzed step by step.

⚡ Tip: You can also open them directly in Google Colab for a quick interactive run in the cloud — no local setup required.
##  Next Steps
- Join Challenger-level data with Grand Slam outcomes to generate binary labels.
- Design and implement feature engineering to capture performance trends over time.
- Train and evaluate classification models to predict long-term success.

##  Tech Stack
Python · Pandas · NumPy · Git

---

⚠️ *This project is a work in progress and being actively developed.*
