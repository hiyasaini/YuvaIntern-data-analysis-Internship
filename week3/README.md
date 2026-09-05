# Week 3 – Statistical Analysis and Hypothesis Testing

## Overview

Week 3 focuses on applying statistical analysis and hypothesis testing techniques using Python.

The Breast Cancer Wisconsin Diagnostic Dataset used in Week 1 was reused in this week to investigate whether the observed differences and relationships in the data are statistically significant.

The analysis includes hypothesis formulation, statistical testing, confidence intervals, visualization, and interpretation of results.

---

## Objectives

- Formulate meaningful statistical hypotheses.
- Apply statistical hypothesis testing using Python.
- Perform an independent two-sample t-test.
- Perform a chi-square test of independence.
- Perform one-way ANOVA.
- Perform Tukey HSD post-hoc analysis.
- Calculate and interpret a 95% confidence interval.
- Visualize statistical results.
- Interpret p-values and statistical significance.
- Draw scientific conclusions from the analysis.

---

## Dataset

**Dataset:** Breast Cancer Wisconsin Diagnostic Dataset

The dataset contains measurements of breast tumor characteristics along with the diagnosis of each tumor.

### Target Variable

- `diagnosis`
  - `benign`
  - `malignant`

### Important Features Used

- `mean radius`
- `mean perimeter`
- `mean texture`
- Other tumor-related measurements

### Class Distribution

- Benign: 357 cases
- Malignant: 212 cases

---

## Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Statsmodels
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Statistical Analysis Performed

### 1. Independent Two-Sample t-Test

**Research Question:**

Is the mean tumor radius significantly different between malignant and benign tumors?

**Null Hypothesis (H₀):**

There is no significant difference in mean tumor radius between malignant and benign tumors.

**Alternative Hypothesis (H₁):**

There is a significant difference in mean tumor radius between malignant and benign tumors.

Welch's independent two-sample t-test was used.

### Result

The null hypothesis was rejected at the 5% significance level.

The analysis indicates that malignant and benign tumors have a statistically significant difference in their mean tumor radius.

---

### 2. Chi-Square Test of Independence

**Research Question:**

Is tumor radius category associated with tumor diagnosis?

The `mean radius` variable was divided into two categories:

- Low Radius
- High Radius

**Null Hypothesis (H₀):**

Tumor radius category and diagnosis are independent.

**Alternative Hypothesis (H₁):**

Tumor radius category and diagnosis are associated.

### Result

- Chi-square statistic: **236.528**
- Degrees of freedom: **1**
- p-value: **< 0.001**

The null hypothesis was rejected.

Therefore, there is a statistically significant association between tumor radius category and diagnosis.

---

### 3. One-Way ANOVA

**Research Question:**

Does mean tumor perimeter differ significantly among different tumor-radius groups?

The tumors were divided into three groups based on mean radius:

- Small
- Medium
- Large

**Null Hypothesis (H₀):**

There is no significant difference in mean tumor perimeter among the three groups.

**Alternative Hypothesis (H₁):**

At least one group has a significantly different mean tumor perimeter.

### Result

The null hypothesis was rejected.

There is a statistically significant difference in mean tumor perimeter among the three tumor-radius groups.

---

### 4. Tukey HSD Post-Hoc Test

Tukey's HSD test was performed after ANOVA to determine which specific groups differed significantly.

All three pairwise comparisons were statistically significant:

- Large vs Medium
- Large vs Small
- Medium vs Small

All comparisons had **p < 0.001**.

This indicates that tumor perimeter differs significantly across all three tumor-radius groups.

---

## Confidence Interval Analysis

A 95% confidence interval was calculated for the difference in mean tumor radius between malignant and benign tumors.

### Results

**Mean Difference:**

5.3163

**95% Confidence Interval:**

4.8452 to 5.7874

Since the entire confidence interval is above zero, the result supports the conclusion that malignant tumors have a higher mean radius than benign tumors in this dataset.

---

## Visualizations

The following visualizations were created to support the statistical analysis:

1. Comparison of mean tumor radius by diagnosis
2. Distribution of mean tumor radius by diagnosis
3. Diagnosis distribution by tumor radius category
4. Tumor perimeter across tumor-radius groups
5. 95% confidence interval for the difference in mean tumor radius

All visualization files are stored in the `visualizations/` folder.

---

## Key Findings

- Malignant and benign tumors show a statistically significant difference in mean tumor radius.
- Tumor radius category has a significant association with diagnosis.
- Mean tumor perimeter differs significantly across small, medium, and large radius groups.
- Tukey HSD confirms that every pair of radius groups differs significantly.
- The 95% confidence interval for the difference in mean radius does not include zero.
- Overall, tumor size-related features show strong statistical differences across tumor diagnosis and radius groups.

---

## Limitations

- Statistical significance does not necessarily imply causation.
- The analysis is based on a single publicly available dataset.
- The radius categories were created using the median/quantile-based grouping approach for statistical testing.
- Other tumor characteristics may also influence diagnosis.
- Further analysis with additional datasets would improve the generalizability of the findings.

---

## Conclusion

Week 3 demonstrated how statistical hypothesis testing can be used to validate patterns observed during exploratory data analysis.

Using t-tests, chi-square testing, ANOVA, Tukey HSD, and confidence intervals, the analysis found statistically significant relationships between tumor measurements and diagnosis.

The results provide statistical support for the differences observed between benign and malignant tumors and demonstrate the importance of statistical methods in data-driven scientific analysis.

---


