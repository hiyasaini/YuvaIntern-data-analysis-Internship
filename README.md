# Week 1 - Data Acquisition, Cleaning, and Exploratory Analysis

**Name:** Hiya Saini  


## Dataset
Breast Cancer Wisconsin (Diagnostic), UCI Machine Learning Repository.

Official UCI page:
https://archive.ics.uci.edu/dataset/17/breast

DOI: https://doi.org/10.24432/C5DW2B

## Project contents
- `Week1_Data_Acquisition_Cleaning_EDA.ipynb` - notebook
- `week1_analysis.py` - Python script
- `breast_cancer_wisconsin_diagnostic_source.csv` - source representation used for analysis
- `working_copy_before_cleaning.csv` - controlled messy working copy
- `cleaned_breast_cancer_dataset.csv` - final cleaned dataset
- `figures/` - six visualizations
- `Week1_Data_Acquisition_Cleaning_EDA_Report.docx` - final report
- `portal_description_200_words.txt` - submission description

## Cleaning approach
The original public dataset has no missing values and no duplicate rows. To demonstrate the required Week 1 cleaning workflow transparently, a small controlled amount of missingness and five duplicate rows were introduced only into a working copy. The source dataset was not modified.

Missing numerical values were filled using the median because the median is robust to outliers. Exact duplicate rows were removed. Numerical columns were verified, and the diagnosis field was converted to categorical type.

## Reproducibility
Install the packages in `requirements.txt`, then open the notebook or run:

```bash
python week1_analysis.py
```
