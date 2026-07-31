# Step 0
from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1
spark = SparkSession.builder \
    .appName("Breast Cancer Analysis") \
    .getOrCreate()

if (spark.getActiveSession()):
    print('yes')
else:
    print('no')

# Step 2
spark_df = spark.read.csv("breast_cancer.csv", header=True, inferSchema=True)
df_pandas = spark_df.toPandas()

# Step 3
spark_df.printSchema()
spark_df.show(5)

num_rows = spark_df.count()
num_cols = len(spark_df.columns)
print(num_rows)
print(num_cols)

# Step 4
row_50 = spark_df.collect()[49]
radius_mean_value = row_50['radius_mean']

# Step 5
m_count = spark_df.filter(spark_df.diagnosis == 'M').count()
b_count = spark_df.filter(spark_df.diagnosis == 'B').count()
diagnosis_diff = m_count - b_count

# Step 6
import os
os.makedirs('presentation', exist_ok=True)

diagnosis_counts = df_pandas['diagnosis'].value_counts()
relative_frequencies = diagnosis_counts / len(df_pandas)

plt.figure(figsize=(8, 6))
relative_frequencies.plot(kind='bar')
plt.title("Diagnosis Class Balance")
plt.xlabel("Diagnosis")
plt.ylabel("Relative Frequency")
plt.savefig('presentation/diagnosis_class_balance.png')
plt.close()

print(relative_frequencies['M'])

# Step 7
spark_df.describe().show()

max_fractal_dimension_mean = df_pandas['fractal_dimension_mean'].max()
min_symmetry_mean = df_pandas['symmetry_mean'].min()
range_diff = round(abs(max_fractal_dimension_mean - min_symmetry_mean), 4)

# Step 8
benign_df = df_pandas[df_pandas['diagnosis'] == 'B']
radius_mean_b = round(benign_df['radius_mean'].mean(), 2)
texture_mean_b = round(benign_df['texture_mean'].mean(), 2)
perimeter_mean_b = round(benign_df['perimeter_mean'].mean(), 2)

product = radius_mean_b * texture_mean_b * perimeter_mean_b

# Step 9
malignant_df = df_pandas[df_pandas['diagnosis'] == 'M']
ratios = (malignant_df['radius_mean'] / malignant_df['perimeter_mean']).mean()
mean_radius_perimeter_ratio = round(ratios, 2)

# Step 10
spark.stop()

if (spark.getActiveSession()):
    print('no')
else:
    print('yes')