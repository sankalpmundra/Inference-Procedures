# Conducting a One-Sample _z_ Significance Test

Significance tests are used to evaluate the strength of the evidence against some null hypothesis $(H_0)$. The alternative hypothesis $(H_a)$ is the claim we are trying to find statistically significant evidence in favor of. To setup a significance test for a population proportion, we start by creating a set of hypotheses.

The null hypothesis should always contain a statement of equality. It is often a statement of "no difference". The null hypothesis, for _z_ tests, are generally written in the form:

$$ H_0 : p = p_0 $$

The alternative hypothesis could take one of three forms, depending on the context of the test:

$$ H_a : p < p_0 $$

$$ H_a : p > p_0 $$

$$ H_a : p \neq p_0 $$

Once we have a clear view of the objectives of the test, we can craft a plan to gather the relevant data from the sample. However, a certain set of conditions need to be met in order to conduct a valid significance test about a proportion.

1. **Random:** Data needs to come from a random sample from the population of interest or a randomized experiment. This can be achieved through a simple random sample (SRS), or the more commonly used stratified random sampling technique.
2. **Normal:** The sampling distribution of the sample proportion statistic $(\hat{p})$ must be approximately normal. This can be achieved with more than 10 successes and failures each in the sample.

$$ np_0 \geq 10 \quad \text{and} \quad n(1 - p_0) \geq 10 $$

3. **Independence:** Each observation in the sample must be independent and can not be influenced by each other. When sampling without replacement, the sample size shouldn't exceed 10% of its population size.

$$ n \leq 0.1(N) $$

If **all** the conditions for inference on proportions are met, we can proceed to conduct a one-sample _z_ test.

The standardized test statistic for a significance test is calculated to determine how many standard errors the sample statistic is away from the hypothesized population parameter. The general formula for a standardized test statistic is:

$$ \text{standardized test statistic} = \frac{\text{statistic - parameter}}{\text{standard error of statistic}} $$

The test statistic for a one-sample _z_ test is denoted by $z$, and this statistic determines how many standard errors the sample proportion $(\hat{p})$ is away from the hypothesized population proportion $(p_0)$. The $z$ statistic is given by:

$$ z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}} \quad ; $$

$$
\begin{aligned}
& \hat{p} : \text{Sample proportion statistic} \\
& p_0 : \text{Hypothesized population proportion parameter} \\
& \sqrt{\frac{p_0(1 - p_0)}{n}} : \text{Standard error of the sample proportion statistic, where} \\
& p_0 : \text{population proportion parameter for a success} \\
& 1 - p_0 : \text{population proportion parameter for a failure} \\
& n : \text{sample size}
\end{aligned}
$$

A standardized test statistic is used to compute the _P-Value_ of a test. This value represents the probability of obtaining a value as extreme as the test statistic, given the null hypothesis $(H_0)$ is true. In the case of a one-sample _z_ test about a proportion, this value represents the chances of obtaining a standardized test statistic as extreme as the calculated $z$ statistic. However, the 'P-Value' also depends on the condition of the test's alternative hypothesis. 

For a one-tailed test, the alternative hypothesis claims that the population proportion parameter is simply greater than or lesser than the value proposed by the null hypothesis. As a result, the _P-Value_ is given by:

$$ H_a : p < p_0 \quad \text{or} \quad H_a : p > p_0 $$

$$ \Downarrow $$

$$ \text{P-Value} = P\left( Z \geq |z| \ \middle| \ H_0 \text{ is true} \right) $$

For a two-tailed test, the alternative hypothesis is claiming that the population proportion is different to the hypothesized proportion in the null hypothesis. As a result, the _P-Value_ is doubled, to account for both the left and right tails of the sampling distribution of the sample proportion $(\hat{p})$, and is given by:

$$ H_a : p \neq p_0 $$

$$ \Downarrow $$

$$ \text{P-Value} = 2 * P\left( Z \geq |z| \ \middle| \ H_0 \text{ is true} \right) $$

Once we know the _P-Value_ of our sample statistic, we can conclude the significance test by comparing the value to the pre-determined significance level $(\alpha)$ for the test. The significance level is the threshold probability for rejecting the null hypothesis, controlling the Type I error rate, and it is set before gathering data and conducting the test for the purpose of carrying out an ethical significance test. 

To conclude a one-sample _z_ test about a proportion, or any significance test for that matter, we compare the _P-Value_ to the $\alpha$ level, and there are two possible conclusions we can make.

When the P-Value is **lesser than** the significance level, there is statistically significant evidence to prove the claim of the alternative hypothesis. As such, we reject the null hypothesis and accept the alternative hypothesis.

$$ \text{P-Value} < \alpha \Rightarrow \text{Reject} H_0 \Rightarrow \text{Accept} H_a $$

However, in the case that the P-Value is **greater than or equal to** the significance level, there is not sufficient evidence to prove the alternative hypothesis. Hence, we fail to reject the null hypothesis, and for those reasons, we can not accept the alternative hypothesis.

$$ \text{P-Value} \geq \alpha \Rightarrow \text{Fail to reject} H_0 \Rightarrow \text{Can not accept} H_a $$

> Note: In this case, we are not **rejecting** the alternative hypothesis, we just fail to reject the null hypothesis, and it could very much be the case that the test had a Type II error, where the null hypothesis was indeed false but we wrongly failed to reject it.

---