import numpy as np
from scipy.stats import norm

# Significance level for the test
alpha = 0.05

# Known Data:

n = 65
successes = 11
failures = 54

# Calculations

p_parameter = 0.2
p_statistic = successes / n

std_dev = np.sqrt((p_parameter * (1 - p_parameter)) / n)

# Z Statistic

z = (p_statistic - p_parameter) / std_dev

# P-Value

p_value = 1 - norm.sf(z)

# Function to conclude the one-sample z test
def z_test_conclude(p_val, significance_level):
    """
    Checks if the P-value indicates a significant difference based on the given significance level.

    Args:
        p_val (float): The p-value calculated from the significance test.
        significance_level (float): The significance level for the same significance test.

    Returns:
        A message indicating if there is statistic evidence to prove that fewer than 20% of all cereal boxes contain the voucher.
    """
    if p_val < significance_level:
        print("There is significant evidence that the true proportion of cereal boxes that contain the voucher is fewer than 20%.")
    else:
        print("There is no significant evidence to suggest that the true proportion of cereal boxes that contain the voucher is fewer than 20%.")

# Conclude the test:
z_test_conclude(p_value, alpha)