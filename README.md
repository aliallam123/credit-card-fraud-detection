
# Credit Card Fraud Detection

An end-to-end machine learning project to identify fraudulent credit card transactions, from exploratory data analysis and model optimisation to API development, Docker containerisation and AWS cloud deployment.

## Project progress

![Project Progress](https://img.shields.io/badge/Progress-60%25-brightgreen?style=for-the-badge)

**████████████░░░░░░░░ 60%**

| Phase | Status |
|---|---|
| 1. Setup and data ingestion | ✅ Complete |
| 2. Exploratory data analysis and preprocessing | ✅ Complete |
| 3. Baseline modelling and hyperparameter tuning | ✅ Complete |
| 4. Advanced resampling and model optimisation | ✅ Complete |
| 5. Final model evaluation | ✅ Complete |
| 6. Model serialisation and notebook clean-up | ✅ Complete |
| 7. FastAPI development | 🟡 In progress |
| 8. Docker containerisation | ⬜ Pending |
| 9. AWS cloud deployment | ⬜ Pending |
| 10. Portfolio and project finalisation | ⬜ Pending |

**Current focus:** Integrating the trained machine learning model into FastAPI and developing the fraud prediction endpoint.

[View detailed project progress tracker](progress.md)

## Model performance

The dataset contains 284,807 credit card transactions, of which only 492 (0.17%) are fraudulent.

The final model uses a combination of random undersampling, SMOTE oversampling, a Support Vector Classifier and decision threshold optimisation.

| Metric | Baseline SVC | Final model |
|---|---:|---:|
| Precision | 0.3246 | 0.6698 |
| Recall | 0.6327 | 0.7245 |
| F1 score | 0.4291 | 0.6961 |
| Average precision | 0.4454 | 0.6654 |
| False positives | 129 | 35 |
| Fraudulent transactions detected | 62 | 71 |

The final model achieved approximately a **62% relative improvement in F1 score** over the baseline model.

## Technology stack

### Machine learning
- Python
- NumPy
- Pandas
- Scikit-learn
- Imbalanced-learn
- Joblib

### Data analysis and visualisation
- Jupyter Notebook
- Matplotlib
- Seaborn

### Application development
- FastAPI
- Uvicorn
- Pydantic

### Deployment (planned)
- Docker
- AWS

### Version control
- Git
- GitHub

## Project structure

This project uses a structured framework inspired by Cookiecutter Data Science, separating datasets, experimentation, trained model artefacts and application source code.

```text
├── data/
│   ├── processed/
│   └── raw/
├── models/
│   ├── best_smote.joblib
│   └── best_threshold.joblib
├── notebooks/
│   └── my-notebook.ipynb
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── visualisation/
│   ├── __init__.py
│   └── main.py
├── tests/
├── .gitignore
├── GIT_WORKFLOW.md
├── LICENSE
├── progress.md
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/aliallam123/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Prepare the dataset

Place `creditcard.csv` in `data/raw/` if reproducing the model training notebook.

The raw dataset is excluded from Git due to its size. The trained model artefacts are included in the repository, so retraining is not required to load the saved model.

## Running the API locally

From the project root, run:

```bash
python -m uvicorn src.main:app --reload
```

### API endpoints

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | `/` | API information | Available |
| GET | `/health` | Application health check | Available |
| POST | `/predict` | Fraud prediction | In development |

### API documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Limitations

- The dataset contains only 492 fraudulent transactions.
- Anonymised features limit model interpretability.
- The holdout dataset was previously evaluated during development.
- Random splitting does not measure generalisation to future fraud patterns.
- Further testing is required before deployment in a real financial environment.

## Project status

This project is currently under active development.

The machine learning development stage is complete, with application development currently in progress. Docker containerisation, AWS deployment and automated testing will follow.
