# project progress tracker

## phase 1: setup and data ingestion
- [x] initialise directory structure (data/raw, data/processed, notebooks, src)
- [x] configure requirements and gitignore to exclude large data files
- [x] load raw credit card transactions dataset
- [x] check shape, columns, and data types
- [x] check for missing/null values (none found)

## phase 2: exploratory data analysis & preprocessing
- [x] analyse class imbalance (~99.83% legitimate vs ~0.17% fraud)
- [x] scale unscaled features (`Amount` and `Time`) using `RobustScaler`
- [x] create stratified split (`original_Xtrain`, `original_Xtest`) to prevent data leakage
- [x] create 50/50 balanced sub-sample via under-sampling to address accuracy paradox
- [x] check feature correlations on balanced sub-sample

## phase 3: baseline modeling & hyperparameter tuning
- [x] train baseline classifiers (Logistic Regression, KNN, SVC, Decision Tree)
- [x] evaluate initial models using F1-score, Precision, and Recall
- [x] execute `GridSearchCV` hyperparameter tuning on all 4 models:
  - [x] **Logistic Regression** (CV F1: ~94.2%)
  - [x] **Decision Tree Classifier** (CV F1: ~93.5%)
  - [x] **Support Vector Classifier (SVC)** (CV F1: ~89.4%)
  - [x] **K-Nearest Neighbors (KNN)** (CV F1: ~62.6%)
- [x] extract and save top-performing `best_estimator_` models

## phase 4: outlier removal & advanced resampling (upcoming)
- [ ] identify and eliminate extreme outliers using IQR method on key features ($V14$, $V12$, $V10$)
- [ ] implement and test oversampling technique (SMOTE) during cross-validation
