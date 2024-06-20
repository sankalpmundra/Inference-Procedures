import numpy as np
from scipy.stats import t

# Significance level for the test
alpha = 0.05

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

# Function to conclude the one-sample t test
def t_test_conclude(p_val, significance_level):
    """
    Checks if the P-value indicates a significant difference based on the given significance level.

    Args:
        p_val (float): The p-value calculated from the significance test.
        significance_level (float): The significance level for the same significance test.

    Returns:
        A message indicating whether the average Physics exam score is significantly greater from last year.
    """
    if p_val < significance_level:
        print("There is significant evidence that the average exam score has increased since last year.")
    else:
        print("There is no significant evidence that the average exam score has increased.")

# Conclude the test:
t_test_conclude(p_value, alpha)