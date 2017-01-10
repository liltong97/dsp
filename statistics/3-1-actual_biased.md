[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
The mean of the real distribution is 1.024 but of the biased distribution is 2.40
Below is the code used for this problem as outlined in chap03ex.ipynb:
```python
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf
import thinkplot
import thinkstats2
import chap01soln
resp = chap01soln.ReadFemResp()
numkdhh = resp['numkdhh']

pmf = thinkstats2.Pmf(numkdhh)

thinkplot.Hist(pmf)
thinkplot.Show(xlabel = 'Children under 18 in household', ylabel = 'pmf')

biased_pmf = BiasPmf(pmf, label='observed')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='class size', ylabel='PMF')

print('mean', pmf.Mean())
print('biased mean', biased_pmf.Mean())
```
