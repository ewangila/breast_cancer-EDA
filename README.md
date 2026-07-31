# Breast Cancer EDA with PySpark

Exploratory Data Analysis of the Wisconsin Breast Cancer dataset using **PySpark** and **Pandas**.

Part of a Big-Data analytics workflow that simulates how hospital systems load, inspect, and summarise patient-level features to support oncologists.

## Dataset
- Source: UCI / Wisconsin Diagnostic Breast Cancer
- 569 samples × 33 columns (id, diagnosis, 30 real-valued features + empty trailing column)
- Target: `diagnosis` — `M` (malignant) / `B` (benign)

## What the notebook does
| Step | Task |
|------|------|
| 0–1  | Create & verify SparkSession (`"Breast Cancer Analysis"`) |
| 2    | Load CSV → Spark DataFrame → convert to Pandas |
| 3    | Print schema, show first 5 rows, report shape |
| 4    | Extract 50th row & its `radius_mean` |
| 5    | Count Malignant / Benign + difference |
| 6    | Relative-frequency bar plot of class balance |
| 7    | `.describe()` + range between max fractal-dimension-mean and min symmetry-mean |
| 8    | Product of mean radius × texture × perimeter (Benign only) |
| 9    | Mean radius/perimeter ratio (Malignant only) |
| 10   | Stop Spark session |

Generated plots are saved under `presentation/`.

## Quick start
```bash
# Create environment (example)
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run the script
python breast_cancer.py

# Or open the notebook
jupyter notebook "breast_cancer analysis.ipynb"
