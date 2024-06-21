import numpy as np
from scipy.stats import t

"""
Sankalp is a Physics teacher at Northeastern University and his 350 students just gave the 3rd year Physics exam. Last year, 
the same students obtained a mean score of 75%. Sankalp then made some changes to his teaching style and wants to determine whether 
his students have improved.

He takes a simple random sample (SRS) of 31 students from all the students who gave the exam and notes down their exam scores. 

exam_scores = [82, 79, 83, 87, 78, 78, 80, 83, 79, 82, 77, 77, 81, 65, 71, 74, 74, 81, 75, 72, 87, 78, 80, 72, 67, 80, 74, 90, 76, 59, 76]

Conduct the appropriate significance test at the α = 0.05 significance level to conclude Sankalp's hypothesis.
"""

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
def conclude_ttest1(p_val, significance_level):
    """
    Checks if the P-value indicates a significant difference based on the given significance level.

    Args:
        p_val (float): The p-value calculated from the significance test.
        significance_level (float): The significance level for the same significance test.

    Returns:
        A message indicating if there is statistical evidence to reject the test's null hypothesis.
    """
    if p_val < significance_level:
        print("".join(["Since the P-value is smaller than the significance level (",
                       str(p_val), " < ", str(significance_level), "), ", 
                       "we reject the null hypothesis because there is significant evidence to suggest that ",
                       "the average exam score has increased since last year."]))
    else:
        print("".join(["Since the P-value is not smaller than the significance level (", 
                       str(p_val), " >= ", str(significance_level), "), ", 
                       "we fail to reject the null hypothesis because there is no significant evidence to suggest that ", 
                       "the average exam score has increased."]))

# Conclusion:
conclude_ttest1(p_value, alpha)