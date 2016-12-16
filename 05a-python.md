# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are immutable while lists are mutable. They can both be used to store a series of items. Only tuples will work as keys in dictionaries because the keys must be immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> They both can hold a series of items. Lists can have duplicates where the items in sets must all be unique. Finding an element in a set is much faster than a list because in a set they're stored in a hash but in a list each element must be compared.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is used to create a function without having to give it a name, so it generates "anonymous function". This is useful for using it in a function as an argument/parameter. So, for example, in the sorted function we can use lambda to allow the function to sort by a particular value. So for an array of string: sorted(array_of_strings, key = lambda word: word[-1]) will allow us to sort by the last letter of the word.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions can be used to make more readable code when building lists using for loops. For
>> example if you wanted an array of cubes from 1-10 that were less than 500 you could use map and
>> filter: cubes = map(lambda x:x**3, range(11)) and then filter(lambda x:x<500, cubes). Or using list
>> comprehension you can do [x**3 for x in range(11) if x**3 < 500]

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.
a.

```
date_start = '01-02-2013'
date_stop = '07-28-2015'
```

>> 937 days

b.
```
date_start = '12312013'
date_stop = '05282015'
```

>> 513 days

c.
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





