Using Python lists:
As the number of iteration steps increase, the time taken to produce a tree increases exponentially. The performance plot shows exponential growth.

Comparing NumPy arrays and Python lists:
Using NumPy instead of append() improves performance. The times taken to plot a tree till about 6 iterations are slightly higher when using NumPy than append(). After this the time taken with using append() increases exponentially with number of iterations whereas time taken using NumPy increases almost linearly. This is because NumPy arrays require less memory than lists. This is more noticeable as you use data structures with more items.