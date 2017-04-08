# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both tuples and lists are similar in that they are ordered values with specific positions. However, the elements of a list can be modified after the list is created - a property called mutability.  In contrast, tuples are not mutable.


>>Tuples can serve as keys in a dictionary because they are hashable.  This means tuples contain hash functions which allow for faster indexing by mapping keywords to positions.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists are similar in that they both organize data, and both are mutable.  In contrast, sets are unordered collections of unique hashable objects.


>> For example, a list of coffee producing regions could look like this: ` ["Ethiopia", "Nicaragua", "Nicaragua", "Kenya"]` whereas a set would be constructed like this: ` set(["Ethiopia", "Nicaragua", "Kenya"])`

>> As for performance, looking up elements in a list is slower than a set.  Calls across a list run on a foor loop, which iterates over all items in a list.  By contrast, items in a set are unique and hashable, which allows for jumping directly to the intended element without looping over the set.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda functions are used as quick anonymous functions in the context of other functions.  They simplify the writing of complex functions.  In the following example, `sorted` sorts by an alternate key across a list of numbers.

`sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: 5/x )
#[5, 4, 6, 3, 7, 2, 8, 1, 9]`

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a faster, simpler way to create lists (as opposed to for loops).

`evens = [x*2 for x in range(0,50)]

byfives = [x*5 for x in range(0,50)]`

>> `map` and `filter` can return list objects like list comprehension. In building the list, `map` loops a function over a given range. Similar to maps, `filter` builds the list by adding the subsets of a range for which a boolean returned true.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





