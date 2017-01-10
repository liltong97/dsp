[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)  
About 34% of the male population can apply for the Blue Man Group.  

Below is the code used for this problem:
```python
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

ft_to_cm = 30.48
in_to_cm = 2.54
lower_bound = 5 * ft_to_cm + 10 * in_to_cm
upper_bound = 6 * ft_to_cm + 1 * in_to_cm
dist.cdf(upper_bound) - dist.cdf(lower_bound)
```
