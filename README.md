# AIML Lab Programs (1–10)

Python implementations prepared for practical-exam revision and GitHub.

## Folder structure

- `Program-01-Basic-Python/` – Programs 1(a) to 1(g)
- `Program-02-Supervised-Unsupervised/` – Decision Tree and K-Means
- `Program-03-ID3-Decision-Tree/`
- `Program-04-ANN-Backpropagation/`
- `Program-05-Naive-Bayes-Email/`
- `Program-06-Naive-Bayes-Document/`
- `Program-07-Heart-Disease/`
- `Program-08-KMeans-Employee-Clustering/`
- `Program-09-KNN-Iris/`
- `Program-10-Locally-Weighted-Regression/`

## Requirements

Install the libraries:

```bash
pip install pandas numpy scikit-learn matplotlib statsmodels tensorflow
```

Some programs use only Python's built-in features; install only the libraries needed for the program you are running.

## Dataset note

The CSV datasets are **not included**. Keep the required CSV file in the same folder as its Python program, or update the path in `pd.read_csv()`.

The column names in your actual CSV must match the names used in the code. If your faculty provides a different CSV filename or column names, use those exact names.

## Dataset mapping

| Program | Dataset | Main task |
|---|---|---|
| 2(a) | `emp_salary.csv` | Supervised Decision Tree – salary class |
| 2(b) | `customer_segmentation.csv` | Unsupervised K-Means – customer groups |
| 3 | `loan_approval.csv` | Entropy-based Decision Tree – loan approval |
| 4 | `diabetes.csv` | ANN – diabetes prediction |
| 5 | `emailspam.csv` | Naive Bayes – spam classification |
| 6 | `news_dataset.csv` | Naive Bayes – document classification |
| 7 | `heart_disease.csv` | Gaussian Naive Bayes – heart disease classification |
| 8 | `employee_salary.csv` | K-Means – employee clustering |
| 9 | `iris.csv` | KNN – Iris species classification |
| 10 | `house_price.csv` | LOWESS – locally weighted smoothing |

## Important implementation notes

1. Program 7's supplied implementation uses `GaussianNB`. This is Gaussian Naive Bayes, not a true Bayesian Network.
2. Program 10 uses `statsmodels` LOWESS as the locally weighted smoothing implementation.
3. K-Means cluster labels (0, 1, 2) are arbitrary. Do not assume they automatically mean Junior, Mid-Level, or Senior without checking cluster centres.
4. For text classification, `CountVectorizer` converts text into numeric word-count features.
5. The ANN program expects a binary target encoded as 0 and 1.
6. These are learning/practical-exam examples, not validated systems for real medical or financial decisions.
