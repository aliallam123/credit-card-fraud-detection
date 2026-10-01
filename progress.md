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
