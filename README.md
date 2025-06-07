# NextGen Tennis Prediction 🎾

This project aims to identify promising young tennis players based on their early-career performance in ATP Challenger tournaments and predict whether they are likely to reach a Grand Slam semi-final in the future.

---

## Objective

Build a supervised machine learning pipeline that uses Challenger-level match data (under age 25) to model long-term player potential, specifically whether a player will reach the semi-final stage of a Grand Slam.

---

## 🏆 Why Challenger Tournaments?

The ATP Challenger Tour is the primary launchpad for young professional tennis players. Most top players begin their careers in Challenger events before breaking into ATP Tour and Grand Slam levels.  
By focusing on matches played before age 25, we aim to capture performance signals **early in a player's career**, when predictions are most impactful.

---

## What done so far?

### Data Pipeline

- **Data Collection**: Used ATP match datasets (1998–2025) including player metadata.
- **Cleaning**: Removed matches with missing serve stats, standardized formats using `pandas`.
- **Filtering**: Focused only on Challenger-level matches involving players age ≤ 24.

### Feature Engineering

For each player:
- Average serve statistics during wins and losses
- First and second serve effectiveness
- Break point save percentages
- Entry age into Challenger matches
- Average opponent rank in wins and losses
- Dominant hand and height (from ATP player file)

**Feature Selection Philosophy**  
All features were carefully selected to reflect *only what would be known at the time of the match*, in order to avoid **data leakage**.  
No retrospective performance or future outcomes were used during feature construction or labeling.  
This ensures that the model simulates real-world decision-making based on available data at the moment.

### Labeling

- Players who reached at least **one Grand Slam semi-final** during their career were labeled as `1`.
- A control group of similar-aged players who never reached that stage were labeled as `0`.

### Modeling

- Applied `SMOTE` to balance the dataset (label 1 was underrepresented).
- Trained and compared multiple classifiers:
  - Logistic Regression
  - Random Forest (with GridSearchCV tuning)
  - XGBoost (best performance overall)

---

## Key Insights

- Features such as **Avg Opponent Rank in Wins**, **Height**, and **2nd Serve Performance in Losses** showed the strongest correlation with reaching a Grand Slam semi-final.
- **XGBoost** yielded the best predictive performance with a **ROC AUC of 0.92**.
- **Logistic Regression** offered solid results and interpretability, making it useful as a baseline.
- **Random Forest** underperformed slightly compared to expectations — possibly due to **mild overfitting**.

   We suspect that the model may be too flexible given the current dataset size and feature space. Future work will include regularization, more aggressive hyperparameter tuning, and potentially simpler tree-based ensembles.

 _Note: Correlation does not imply causation. These features are statistically associated with higher future performance but should be investigated further before drawing definitive conclusions._

---

##  Notebooks

All steps — from cleaning to modeling — are documented in modular Jupyter notebooks in the [`colab_notebooks/`](colab_notebooks/) directory.  
Each notebook includes inline comments and visualizations to support reproducibility.

---

##  Next Steps

- Add more players to improve generalization.
- Evaluate model calibration and confidence thresholds.
- Explore temporal validation to reflect real-time forecasting.
- Visualize feature importance across models (e.g., Random Forest, XGBoost).

---

##  Tech Stack

Python · pandas · NumPy · scikit-learn · imbalanced-learn · XGBoost · Google Colab · Git/GitHub

---

##  Disclaimer

This project is intended for exploratory and educational purposes.  
While it leverages real tennis data, predictions should not be treated as definitive player evaluations.
