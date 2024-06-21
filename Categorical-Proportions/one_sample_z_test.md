# Conducting a One-Sample _z_ Test for Proportions

## Question

Some boxes of a certain brand of breakfast cereal include a voucher for a free video rental inside the box. The company that makes the cereal claims that a voucher can be found in 20 percent of the boxes. However based, on their experiences eating this cereal at home, a group of students believe that the true proportion of boxes with vouchers is less than 20%. This group of students purchased 65 boxes of the cereal to investigate the company's claim. The students found a total of 11 vouchers for free video rentals in the 65 purchased boxes.

Suppose it is reasonable to assume that the 65 boxes purchased by the students are a random sample of all the boxes of this cereal. Based on this sample, is there support for the students' belief that the proportion of boxes with vouchers is truly less than 20%? Provide statistical evidence to support your answer, using a significance level of 5% in your significance test.

## Answer

We want to perform a significance test, at the $α = 0.05$ significance level, of:

$$ H_o: p = 0.2 $$
$$ H_a: p < 0.2 $$

_where 'p' represents the true proportion of cereal boxes that have a voucher for a free video rental_

#### Conditions for inference on proportions:

1. **Random**: As stated in the problem, we are assuming that the 65 cereal boxes bought by the students are a random sample of all boxes.
2. **Normal**: The sampling distribution of the sample proportion (p̂) needs to be approximately normal. Assuming the null hypothesis is true, the expected number of successes and failures each are greater than 10.

$$ np̂ ≥ 10 $$
$$ n(1 - p̂) ≥ 10 $$

3. **Independence**: When sampling without replacement, the sample size should be smaller than **10%** of the population. In this case, we will assume independence because there are likely more than 650 cereal boxes made by the company.

$$ n ≤ 0.1(N) $$

Since all the conditions for inference have been met, we will proceed to conduct a one-sample _z_ test. We will begin by extracting and noting down all the data from the question and calculating the sample statistics.

```python
import numpy as np
from scipy.stats import norm
```

```python
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
```

Now, we can calculate the standardized test statistic 'z':

```python
# Standardized Test Statistic (z statistic)
z = (p_statistic - p_parameter) / std_dev
```

Once we know the z-statistic, we can compute the 'P-value':

```python
# Calculate the P-Value (one-tailed)
p_value = norm.sf(abs(z))
```

Finally, we can compare the 'P-value' with our significance level and conclude the significance test:

```python
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
```

### Conclusion

Since the P-value was greater than the significance level of $α = 0.05$, we fail to reject the null hypothesis because there is no significant evidence to conclude that the true proportion of cereal boxes that contain the voucher is fewer than 20%

---