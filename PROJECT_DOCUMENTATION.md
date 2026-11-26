
# Mobile Price Prediction

### Machine Learning-Based Mobile Phone Price Classification and Estimation

---

## 1. Project Overview

Mobile Price Prediction is a Machine Learning project designed to classify mobile phones into appropriate price brackets based on their hardware specifications.

The project focuses on analyzing important mobile features such as RAM, battery capacity, camera specifications, and processor-related attributes to develop an intelligent price prediction system.

The solution integrates data analysis, statistical reasoning, feature engineering, machine learning classification, and an interactive Streamlit application.

## 2. Problem Statement

Clean RAM, battery, camera, and processor specs, train KNN & Logistic Regression price-bracket classifiers, and build an interactive phone price estimator.

## 3. Project Objectives

- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Identify patterns and relationships among mobile specifications.
- Apply appropriate statistical analysis.
- Perform feature engineering and feature selection.
- Develop KNN and Logistic Regression classification models.
- Evaluate and compare model performance.
- Build an interactive mobile price prediction application using Streamlit.

## 4. Dataset Description

The project uses a real-world mobile phone dataset containing hardware specifications and corresponding price categories.

Important features include:

- RAM
- Battery Capacity
- Camera Specifications
- Processor Specifications
- Price Range (Target Variable)

Dataset Source: [(https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)]

Note: Refer to the dataset documentation for complete feature definitions, units, and preprocessing details.

## 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Jupyter Notebook | Development Environment |
| Pandas | Data Manipulation |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| Streamlit | Interactive Application |

## 6. Project Methodology

The project follows a structured Data Science workflow.

### Phase 1: Data Wrangling & Exploratory Data Analysis
- Data inspection and cleaning
- Missing value and duplicate analysis
- Outlier detection
- Descriptive statistics
- Exploratory visualizations
- Correlation analysis

### Phase 2: Statistical Reasoning & Feature Engineering
- Statistical analysis and hypothesis testing
- Feature selection
- Feature engineering
- Data transformation and preparation

### Phase 3: Modelling & Evaluation
- Data splitting and validation
- K-Nearest Neighbors (KNN)
- Logistic Regression
- Model performance comparison
- Confusion Matrix and Classification Report

### Phase 4: Tangible Working Output
- Streamlit application development
- Interactive feature inputs
- Machine learning-based price bracket prediction
- Display of prediction results

## 7. Machine Learning Models

The following classification algorithms are implemented:

1. K-Nearest Neighbors (KNN)
2. Logistic Regression

The models are evaluated using appropriate classification metrics.

## 8. Model Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Cross-Validation Scores

Actual evaluation results will be documented after final validation.

## 9. Application

An interactive Streamlit application allows users to enter mobile hardware specifications and obtain a predicted mobile price bracket.

### Application Features
- Interactive input controls
- Mobile specification selection
- Price bracket prediction
- Easy-to-understand prediction output

## 10. Repository Structure

```text
Mobile-Price-Prediction/
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── Project_Notebook.ipynb
│
├── src/
│   ├── app.py
│   └── README.md
│
├── docs/
│   ├── Project_Report.pdf
│   └── Project_Presentation.pptx
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 11. Installation & Execution

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run src/app.py
```

## 12. Expected Outcome

The project aims to provide a data-driven approach for classifying mobile phones into price brackets using their hardware specifications.

The final application provides an interactive interface for exploring mobile specifications and generating price bracket predictions.

## 13. Limitations & Future Scope

- Prediction quality depends on dataset quality and feature availability.
- Additional real-world mobile specifications can improve analysis.
- Future work may include testing additional classification algorithms.
- The application can be enhanced with updated mobile datasets and improved user experience.

## 14. Author

**Student Name:** [ESWARI]

**Department:** Data Science

**Program:** B.Tech

**Project:** Mobile Price Prediction

---

*Developed as an individual academic Data Science project.*
