[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)  

Since the CDF is approximately a straight line, this implies that the distribution is uniform.  
Below is the code used to do this problem:
```python
import random
import thinkstats2
import thinkplot

random_array = []
for i in range(1000):
    random_array.append(random.random())
pmf = thinkstats2.Pmf(random_array)
thinkplot.Pmf(pmf, linewidth = 0.2)
thinkplot.Show(xlabel='weeks', axis=[-0.02, 1.02, 0, 0.0012])

cdf = thinkstats2.Cdf(random_array)
thinkplot.Cdf(cdf)
thinkplot.Show()
```
