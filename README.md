# Insurance Risk Analytics & Predictive Modeling

## Project Overview

This project focuses on end-to-end insurance risk analytics for AlphaCare Insurance Solutions (ACIS), a South African auto-insurance company seeking to optimize pricing strategies, improve profitability, and identify low-risk customer segments using data-driven methods.

The analysis uses 18 months of historical insurance claims data to explore portfolio risk patterns, validate statistical hypotheses, and build predictive machine learning models for claim severity and premium optimization.

The project also emphasizes reproducibility, version control, and modern MLOps practices using GitHub Actions and Data Version Control (DVC).

---

# Business Objective

The primary objectives of this project are:

- Analyze insurance claim patterns and profitability.
- Identify low-risk customer segments for targeted premium reductions.
- Validate business assumptions using statistical hypothesis testing.
- Build predictive models for:
  - Claim Severity Prediction
  - Risk-Based Premium Pricing
- Improve pricing strategies using interpretable machine learning models.
- Create a reproducible and auditable analytics pipeline suitable for regulated industries.

---

# Dataset Description

The dataset contains:

- Client information
- Vehicle details
- Policy and plan information
- Geographic information
- Premium values
- Claim values

Key metrics used throughout the analysis:

## Loss Ratio

:contentReference[oaicite:0]{index=0}

## Margin

:contentReference[oaicite:1]{index=1}

---

# Project Structure

```text
insurance-risk-analytics/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
├── reports/
│   └── final_report.md
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── tests/
├── .dvc/
├── .gitignore
├── dvc.yaml
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- SciPy
- DVC
- GitHub Actions

---

# Installation Steps

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/insurance-risk-analytics.git
cd insurance-risk-analytics
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Notebooks

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open notebooks from the `notebooks/` directory:

- `01_eda.ipynb`
- `02_hypothesis_testing.ipynb`
- `03_modeling.ipynb`

---

# Data Version Control (DVC)

This project uses DVC to track datasets and maintain reproducible data pipelines.

## Initialize DVC

```bash
dvc init
```

## Add Dataset to DVC

```bash
dvc add data/insurance_data.csv
```

## Push Data to Local Remote

```bash
dvc push
```

## Pull Data

```bash
dvc pull
```

---

# CI/CD Pipeline

GitHub Actions is used for Continuous Integration.

The CI pipeline automatically:

- Installs dependencies
- Runs linting checks using flake8
- Runs tests using pytest

Pipeline configuration is located in:

```text
.github/workflows/ci.yml
```

The workflow runs on every:

- Push
- Pull Request

---

# Exploratory Data Analysis (EDA)

The EDA phase includes:

- Data quality assessment
- Missing value analysis
- Univariate analysis
- Multivariate analysis
- Geographic risk analysis
- Temporal trend analysis
- Outlier detection
- Loss ratio analysis

---

# Hypothesis Testing

The following hypotheses are tested:

- Risk differences across provinces
- Risk differences across zip codes
- Margin differences across zip codes
- Risk differences between genders

Statistical methods used:

- Chi-Squared Test
- T-Test
- Z-Test

---

# Predictive Modeling

Models implemented:

- Linear Regression
- Random Forest
- XGBoost

Evaluation metrics:

## Regression Metrics

- RMSE
- R² Score

## Classification Metrics

- Accuracy
- Precision
- Recall
- F1-Score

---

# Model Interpretability

SHAP and LIME are used to explain model predictions and identify the most influential features affecting insurance risk and pricing.

---

# Key Deliverables

- Reproducible analytics pipeline
- Statistical hypothesis testing framework
- Predictive risk models
- Business recommendations
- Professional final report

---

# Future Improvements

Potential future enhancements include:

- Deployment of prediction APIs
- Real-time pricing systems
- Deep learning approaches
- Fraud detection integration
- Automated retraining pipelines

---

# Author

Betelhem Alemu
