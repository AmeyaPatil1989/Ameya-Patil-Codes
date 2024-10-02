# import libraries
import pandas as pd

# read the file
df = pd.read_csv('Student_Grades.csv')

# print(df)

sgScience = df['ScienceScore']
# print(sgScience)

# mean = sgScience.mean()
# median = sgScience.median()
# maximum = sgScience.max()
# minimum = sgScience.min()
# variance = sgScience.var()
# std_dev = sgScience.std()
# skewness = sgScience.skew()
# kurtosis = sgScience.kurtosis()
# modes = sgScience.mode()

# print(f"Mean = {mean}")
# print(f"Median = {median}")
# print(f"Max = {maximum}")
# print(f"Min = {minimum}")
# print(f"Variance = {variance}")
# print(f"SD = {std_dev}")
# print(f"Skewness = {skewness}")
# print(f"Kurtosis = {kurtosis}")
# print(f"Mode = {modes}")

# summary = sgScience.describe()
# print(summary)

# df_ffill = df.fillna(method='ffill')
# sgScience_ffill = sgScience.fillna(method='ffill')

# print("\nDataFrame after forward filling missing values:")
# # print(df_ffill)
# print(sgScience_ffill)

# # print(df_ffill.describe())
# print(sgScience_ffill.describe())

# variance_ffill = sgScience_ffill.var()
# skewness_ffill = sgScience_ffill.skew()
# kurtosis_ffill = sgScience_ffill.kurtosis()


# print(f"Variance = {variance}")
# print(f"Skewness = {skewness}")
# print(f"Kurtosis = {kurtosis}")
# print(f"Variance = {variance_ffill}")
# print(f"Skewness = {skewness_ffill}")
# print(f"Kurtosis = {kurtosis_ffill}")

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['ScienceScore'].quantile(0.25)
Q3 = df['ScienceScore'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(lower_bound)
print(upper_bound)

# Detect outliers
outliers = df[(df['ScienceScore'] < lower_bound) | (df['ScienceScore'] > upper_bound)]

print(f"\nOutliers detected in ScienceScore column (using IQR):\n{outliers}")
print(df.describe())

# Remove outliers
df_no_outliers = df[(df['ScienceScore'] >= lower_bound) & (df['ScienceScore'] <= upper_bound)]