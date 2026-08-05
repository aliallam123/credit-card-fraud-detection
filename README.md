# credit card fraud detection

data science project to build a machine learning model that identifies fraudulent credit card transactions. 

## project structure

this project uses a structured framework inspired by cookiecutter data science. separating raw data, processed data, notebooks, and production code helps keep the codebase clean.

```
├── data/
│   ├── processed/      # clean data ready for modelling
│   └── raw/            # raw dataset (ignored by git due to size)
├── notebooks/          # jupyter notebooks for eda and modelling
├── src/                # reusable source code
│   ├── data/           # loading and saving data
│   ├── features/       # feature engineering and preprocessing
│   ├── models/         # model training and evaluation
│   └── visualization/  # plotting utilities
├── requirements.txt    # python package dependencies
└── README.md           # project documentation
```

## setup

1. clone the repository
2. create virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. place `creditcard.csv` in `data/raw/` (dataset is excluded from git)
