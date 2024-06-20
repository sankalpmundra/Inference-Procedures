# Conducting a One-Sample _t_ Test for Means

## Question

Sankalp is a Physics teacher at Northeastern University and his 350 students just gave the 3rd year Physics exam. Last year, the same students obtained a mean score of 75%. Sankalp then made some changes to his teaching style and wants to determine whether his students have improved.

He takes a simple random sample (SRS) of 31 students from all the students who gave the exam and notes down their exam scores. 

```python
exam_scores = [82, 79, 83, 87, 78, 78, 80, 83, 79, 82, 77, 77, 81, 65, 71, 74, 74, 81, 75, 72, 87, 78, 80, 72, 67, 80, 74, 90, 76, 59, 76]
```

Conduct the appropriate significance test at the $α = 0.05$ significance level to conclude Sankalp's hypothesis.

## Answer

We want to perform a significance test, at the $α = 0.05$ significance level, of:

$$ H_o: µ = 75 $$
$$ H_a: µ > 75 $$

_where $µ$ represents the average score of the students on the Physics exam_

#### Conditions for inference on means:

1. **Random**: As stated in the question, Sankalp took a random sample of exam scores from all the students who gave the Physics exam.
2. **Normal**: The sampling distribution of the sample mean (x̄) needs to be approximately normal. Since the sample size was larger than 30, we can assume that the distribution is approximately normal.

$$ n >= 30 $$
$$ 31 >= 30 $$

3. **Independence**: When sampling without replacement, the sample size should be smaller than **10%** of the population. In this case, we can assume independence because the sample is indeed smaller than 10% of all Physics students giving the exam

$$ n <= 0.1(N) $$
$$ 31 <= 0.1(350) $$
$$ 31 <= 35 $$

Since all the conditions for inference have been met, we will proceed to conduct a one-sample _t_ test. We will begin by extracting and noting down all the data from the question and calculating the sample statistics.

```python
import numpy as np
from scipy.stats import t
```

```python
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
```

Now, we can calculate the standardized test statistic 't':

```python
# Calculate the t-statistic
t_statistic = (sample_mean - population_mean) / standard_error

# Calculate the degrees of freedom
df = sample_size - 1
```

Once we know the t-statistic and degrees of freedom, we can compute the 'P-value':

```python
# Calculate the p-value (one-tailed)
p_value = t.sf(abs(t_statistic), df)
```

Finally, we can compare the 'P-value' with our significance level and conclude the significance test:

```python
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
```

### Conclusion

Since the P-value was smaller than the significance level of $α = 0.05$, we can reject the null hypothesis because there is significant evidence to conclude that the average exam scores of the students improved after Sankalp changed his teaching method.

---