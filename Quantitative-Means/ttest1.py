import numpy as np
from scipy.stats import t

# Population mean parameter (µ)
population_mean = 75

# Sample data (exam scores of a class)
sample_scores = [82, 79, 83, 87, 78, 78, 80, 83, 79, 82, 77, 77, 81, 65, 71, 74, 74, 81, 75, 72, 87, 78, 80, 72, 67, 80, 74, 90, 76, 59, 76]

# Calculate the mean and standard deviation of the sample
sample_mean = np.mean(sample_scores)
sample_std = np.std(sample_scores, ddof=1)  # Using ddof=1 for sample standard deviation

# Calculate the standard error of the sample mean
sample_size = len(sample_scores)
standard_error = sample_std / np.sqrt(sample_size)

# Calculate the t-statistic
t_statistic = (sample_mean - population_mean) / standard_error

# Calculate the degrees of freedom
df = sample_size - 1

# Calculate the p-value (one-tailed)
p_value = t.sf(abs(t_statistic), df)

# Comparing P-value and α to conclude the test
if p_value < 0.05:
    print("The average exam score is significantly different from the population mean.")
else:
    print("There is no significant difference in the average exam score.")