
# project progress tracker

## phase 1: setup and data ingestion
- [x] initialise directory structure (data/raw, data/processed, notebooks, src)
- [x] configure requirements and gitignore to exclude large data files
- [x] load raw credit card transactions dataset
- [x] check shape, columns and data types
- [x] check for missing/null values (none found)

## phase 2: exploratory data analysis & preprocessing
- [x] analyse class imbalance (~99.83% legitimate vs ~0.17% fraud)
- [x] visualise transaction amount and time distributions
- [x] create stratified 80/20 train test split
- [x] configure RobustScaler for Amount and Time
- [x] create 50/50 balanced sub-sample for exploratory analysis only
- [x] create correlation heatmap and identify strongest negative correlations with fraud (V14, V12, V10)
- [x] investigate outliers using IQR (decided to retain them to preserve potential fraud signals)
- [x] build preprocessing and sampling pipeline to prevent data leakage
- [x] configure 3-fold stratified cross validation

## phase 3: baseline modelling & hyperparameter tuning
- [x] train baseline classifiers (Logistic Regression, KNN, SVC, Decision Tree)
- [x] evaluate initial models using F1, precision, recall and average precision
- [x] execute GridSearchCV hyperparameter tuning on all 4 models:
  - [x] Logistic Regression (CV F1: 0.1243)
  - [x] Decision Tree (CV F1: 0.1366)
  - [x] Support Vector Classifier (CV F1: 0.3854)
  - [x] K-Nearest Neighbours (CV F1: 0.1869)
- [x] extract best estimators
- [x] select SVC as the best baseline classifier
- [x] evaluate baseline SVC on holdout set (F1: 0.4291)

## phase 4: advanced resampling & model optimisation
- [x] configure partial random undersampling (1:10 fraud to legitimate ratio)
- [x] configure SMOTE oversampling to achieve a 1:1 ratio
- [x] build Hybrid SMOTE pipeline
- [x] compare random undersampling against Hybrid SMOTE using cross validation
- [x] improve CV F1 from 0.3854 to 0.6518
- [x] tune Hybrid SMOTE SVC hyperparameters using GridSearchCV
- [x] achieve tuned CV F1 of 0.6849 (C=0.1, polynomial kernel)
- [x] generate out-of-fold decision scores
- [x] optimise decision threshold (~0.1792)
- [x] achieve threshold-optimised validation F1 of 0.6947

## phase 5: final model evaluation
- [x] evaluate final model on original imbalanced 20% holdout dataset
- [x] calculate final performance metrics:
  - [x] Precision: 0.6698
  - [x] Recall: 0.7245
  - [x] F1: 0.6961
  - [x] Average Precision: 0.6654
- [x] generate confusion matrix (71 frauds detected, 27 missed, 35 false positives)
- [x] achieve approximately 62% relative improvement in test F1 over baseline
- [x] select Hybrid SMOTE + SVC as final model
- [x] document results and methodological limitations

## phase 6: model serialisation & notebook clean-up (current phase)
- [x] save trained pipeline using joblib
- [x] save optimised decision threshold
- [x] reload model and threshold
- [x] verify identical predictions after loading
- [x] consolidate library imports
- [x] remove unused libraries
- [x] remove redundant code and debugging cells
- [x] improve markdown documentation throughout notebook
- [x] fix Seaborn and Logistic Regression deprecation warnings
- [ ] complete final code and comment review
- [ ] restart kernel and run entire notebook
- [ ] verify final results and check for remaining warnings
- [ ] commit completed notebook to GitHub

## phase 7: FastAPI development
- [ ] organise model artefacts and application directory
- [ ] configure application dependencies
- [ ] create FastAPI application
- [ ] implement transaction input validation using Pydantic
- [ ] load saved model and threshold into application
- [ ] build fraud prediction endpoint
- [ ] build health check endpoint
- [ ] test API locally
- [ ] write automated tests for predictions and invalid inputs

## phase 8: Docker containerisation
- [ ] create Dockerfile
- [ ] configure .dockerignore
- [ ] build Docker image
- [ ] run container locally
- [ ] test prediction endpoint inside container
- [ ] verify reproducibility across environments

## phase 9: AWS cloud deployment
- [ ] select appropriate AWS deployment service
- [ ] configure cloud infrastructure
- [ ] deploy containerised application
- [ ] test live prediction endpoint
- [ ] configure logging and monitoring
- [ ] implement basic API security

## phase 10: portfolio & project finalisation
- [ ] create comprehensive GitHub README
- [ ] create system architecture diagram
- [ ] document API usage and deployment instructions
- [ ] document model performance and limitations
- [ ] record project demonstration
- [ ] finalise GitHub repository
- [ ] add completed project to CV and LinkedIn
