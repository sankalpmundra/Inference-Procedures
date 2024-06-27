# Conducting a Two-Sample _z_ Significance Test

Significance tests are used to evaluate the strength of the evidence against some null hypothesis $(H_0)$. The alternative hypothesis $(H_a)$ is the claim we are trying to find statistically significant evidence in favor of. To setup a significance test for a difference in population proportions, we start by creating a set of hypotheses.


### Constructing the Hypotheses

The null hypothesis should always contain a statement of equality. It is often a statement of "no difference". The null hypothesis, for two-sample _z_ tests, are generally written in the form:

$$ H_0 : p_1 - p_2 = 0 $$

The alternative hypothesis could take one of three forms, depending on the nature of the test:

$$ H_a : p_1 - p_2 < 0 $$

$$ H_a : p_1 - p_2 > 0 $$

$$ H_a : p_1 - p_2 \neq 0 $$

> **Interlude:** When the null hypothesis assumes that there is no difference between the two population proportions $(p_1 = p_2)$, we use a combined proportion statistic for the sample proportion statistics:
> 
> $$ \hat{p}_{c} = \frac{x_1 + x_2}{n_1 + n_2} \quad ; $$
> 
> $$ 
\begin{aligned}
& x_1 : \text{number of successes in the first sample} \\
& x_2 : \text{number of successes in the second sample} \\
& n_1 : \text{sample size of the first sample} \\
& n_2 : \text{sample size of the second sample}
\end{aligned}
$$


### Conditions for Inference

Once we have a clear view of the objectives of the test, we can craft a plan to gather the relevant data from the sample. However, a certain set of conditions need to be met in order to conduct a valid significance test about a difference in proportions.

1. **Random:** Data needs to come from a two random samples, each from the respective population of interest, or randomized experiments. This can be achieved through a variety of random sampling techniques, like simple random samples (SRS) or stratified random sampling, but the technique should be consistent across both samples.
2. **Normal:** The sampling distribution of the difference in the sample proportions $(\hat{p_1} - \hat{p_2})$ must be approximately normal. This can be achieved if the expected number of successes and failures from both samples are greater than or equal to 10.

$$ n_1\hat{p_c} \geq 10 \quad \text{and} \quad n_1(1 - \hat{p_c}) \geq 10 $$

$$ n_2\hat{p_c} \geq 10 \quad \text{and} \quad n_2(1 - \hat{p_c}) \geq 10 $$

3. **Independence:** Each observation in both samples must be independent and can not be influenced by each other. When sampling without replacement, each sample size shouldn't exceed 10% of its respective population size.

$$ n_1 \leq 0.1(N_1) \quad \text{and} \quad n_2 \leq 0.1(N_2) $$

If **all** the conditions for inference on proportions are met, we can proceed to conduct a two-sample _z_ test for a difference in proportions.


### Calculating the Standardized Test Statistic $(z)$

The standardized test statistic for a significance test is calculated to determine how many standard errors the sample statistic is away from the hypothesized population parameter. The general formula for a standardized test statistic is:

$$ \text{standardized test statistic} = \frac{\text{statistic - parameter}}{\text{standard error of statistic}} $$

The test statistic for a two-sample _z_ test is denoted by $z$, and this statistic determines how many standard errors the difference in the sample proportions $(\hat{p_1} - \hat{p_2})$ is away from the hypothesized difference in the population proportions $(p_1 - p_2)$. The $z$ statistic is given by:

$$ 
z = \frac{(\hat{p_1} - \hat{p_2}) - 0}{\sqrt{\frac{\hat{p_c}(1 - \hat{p_c})}{n_1} + \frac{\hat{p_c}(1 - \hat{p_c})}{n_2}}} \quad ; 
$$

$$
\begin{aligned}
& \hat{p_1} : \text{Sample proportion statistic for the first sample} \\
& \hat{p_2} : \text{Sample proportion statistic for the second sample} \\
& \hat{p_c} : \text{Combined sample proportion} \\
& \sqrt{\frac{\hat{p_c}(1 - \hat{p_c})}{n_1} + \frac{\hat{p_c}(1 - \hat{p_c})}{n_2}} : \text{Standard error of the difference in the sample proportions} \\
& n_1 : \text{Sample size for the first sample} \\
& n_2 : \text{Sample size for the second sample}
\end{aligned}
$$


### Computing the P-Value

A standardized test statistic is used to compute the _P-Value_ of a test. This value represents the probability of obtaining a value as extreme as the test statistic, given the null hypothesis $(H_0)$ is true. In the case of a two-sample _z_ test for a difference in proportions, this value represents the chances of obtaining a standardized test statistic as extreme as the calculated $z$ statistic. However, the 'P-Value' also depends on the condition of the test's alternative hypothesis. 

For a one-tailed test, the alternative hypothesis claims that the difference in the population proportions is greater than or lesser than the value proposed by the null hypothesis. As a result, the _P-Value_ is given by:

$$ H_a : p_1 - p_2 < 0 \quad \text{or} \quad H_a : p_1 - p_2 > 0$$

$$ \Downarrow $$

$$ \text{P-Value} = P\left( Z \geq |z| \ \middle| \ H_0 \text{ is true} \right) $$

For a two-tailed test, the alternative hypothesis is claiming that the difference in the population proportions is simply different to the hypothesized difference in proportions in the null hypothesis. As a result, the _P-Value_ is doubled, to account for both the left and right tails of the sampling distribution of the difference in the sample proportions $(\hat{p_1} - \hat{p_2})$, and is given by:

$$ H_a : p_1 - p_2 \neq 0 $$

$$ \Downarrow $$

$$ \text{P-Value} = 2 * P\left( Z \geq |z| \ \middle| \ H_0 \text{ is true} \right) $$


### Concluding the Test

Once we know the _P-Value_ of the difference in sample proportion statistic, we can conclude the significance test by comparing the value to the pre-determined significance level $(\alpha)$ for the test. The significance level is the threshold probability for rejecting the null hypothesis, controlling the Type I error rate, and it is set before gathering data and conducting the test for the purpose of carrying out an ethical significance test. 

To conclude a two-sample _z_ test for a difference in proportions, we compare the _P-Value_ to the $\alpha$ level, and there are two possible conclusions we can make.

When the P-Value is **lesser than** the significance level, we have found statistically significant evidence to prove the claim of the alternative hypothesis. As such, we reject the null hypothesis and accept the alternative hypothesis.

$$ \text{P-Value} < \alpha \Longrightarrow \text{Reject} H_0 \Longrightarrow \text{Accept} H_a $$

However, in the case that the P-Value is **greater than or equal to** the significance level, there is not sufficient evidence to prove the alternative hypothesis. Hence, we fail to reject the null hypothesis, and for those reasons, we can not accept the alternative hypothesis.

$$ \text{P-Value} \geq \alpha \Longrightarrow \text{Fail to reject} H_0 \Longrightarrow \text{Can not accept} H_a $$

> **Note:** In this case, we are not **rejecting** the alternative hypothesis, we just fail to reject the null hypothesis, and it could very much be the case that the test had a Type II error, where the null hypothesis was indeed false but we wrongly failed to reject it.

---