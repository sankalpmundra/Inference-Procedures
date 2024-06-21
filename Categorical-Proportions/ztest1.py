import numpy as np
from scipy.stats import norm

"""
Some boxes of a certain brand of breakfast cereal include a voucher for a free video rental inside the box. The company that makes the cereal claims 
that a voucher can be found in 20 percent of the boxes. However based, on their experiences eating this cereal at home, a group of students believe
that the true proportion of boxes with vouchers is less than 20%. This group of students purchased 65 boxes of the cereal to investigate the 
company's claim. The students found a total of 11 vouchers for free video rentals in the 65 purchased boxes.

Suppose it is reasonable to assume that the 65 boxes purchased by the students are a random sample of all the boxes of this cereal. Based on this sample,
is there support for the students' belief that the proportion of boxes with vouchers is truly less than 20%? Provide statistical evidence to support 
your answer, using a significance level of 5% in your significance test.
"""

# Significance level for the test
alpha = 0.05

# Known Data
n = 65
successes = 11
failures = 54

# Calculations

p_parameter = 0.2
p_statistic = successes / n

std_dev = np.sqrt((p_parameter * (1 - p_parameter)) / n)

# Standardized Test Statistic (z statistic)
z = (p_statistic - p_parameter) / std_dev

# P-Value (one-tailed)
p_value = norm.sf(abs(z))

# Function to conclude the one-sample z test
def conclude_ztest1(p_val, significance_level):
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
                       "the true proportion of cereal boxes that contain the voucher is fewer than 20%."]))
    else:
        print("".join(["Since the P-value is not smaller than the significance level (", 
                       str(p_val), " >= ", str(significance_level), "), ", 
                       "we fail to reject the null hypothesis because there is no significant evidence to suggest that ", 
                       "the true proportion of cereal boxes that contain the voucher is fewer than 20%."]))

# Conclusion
conclude_ztest1(p_value, alpha)