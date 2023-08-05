# threadLRU
Thread-Safe LRU Cache in Python
[![Build Status](https://travis-ci.com/mattpaletta/pqdict.svg?branch=master)](https://travis-ci.com/mattpaletta/pqdict)

## Instalation
Thread LRU has no external dependencies.
To install threadlru: 
```
pip install threadlru
```

## Getting Started
You can see examples in `tests/`.

To create a new instance (with a maximum size of 10 elements):
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 10)
```

You can put elements in/out as follows:
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 10)
my_dict.set(key = "cat", value = 1) # Returns 1
my_dict.get(key = "cat") # Returns 1
my_dict.get(key = "dog") # Returns None

my_dict.contains(key = "cat") # Returns True
my_dict.contains(key = "dog") # Returns False
```

You must specify a `max_size` when creating a new instance.  At this time, this cannot be resized afterwards.
Everytime you get/set a value, that value is automatically moved to the front of the internal priority-queue.
Anything that exceeds the `max_size` is automatically removed from the cache.


### Computing Values
You can also use it as a cache for any function.  Here, we are calling a function, `F`, 
with the parameter `n = 10`, only if the value does not already exist in our cache.
Subsequent values will use this same value.
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 10)

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

my_dict.compute_if_not_exists(key = "mouse", fun = fib, n = 10) # Returns 55 (computed)
my_dict.compute_if_not_exists("mouse", fib, 10) # Returns 55 (cached)
```

There are a few other methods available for computing values:
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 10)

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

my_dict.compute_if_not_exists(key = "mouse", fun = fib, n = 10) # Returns 55 (computed)
my_dict.compute_if_not_value(key = "mouse", fun = fib, value = 55, n = 10) # Returns 55 (cached)
my_dict.compute_and_set(key = "mouse", fun = fib, n = 10) # Returns 55 (computed)
```

- `compute_if_not_exists` will only call the function `fun` if there is no value in the dictionary with that key
- `compute_if_not_value` will only call `fun` if the key does not exist, or the value at that key does not equal `value`.
- `compute_and_set` calls the function everytime, and caches it's value.
Even if you set the value with one of the `compute_*`, you can still access them via 
`get`, and check if they exist with `contains`.  The function used to compute the value is not stored internally.

### Using accessors
If you use the same function throughout your program to give to the cache, there are also accessors available.
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 10)
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
    
not_exists = my_dict.compute_if_not_exists_accessor(fun = fib) # Returns function
not_value = my_dict.compute_if_not_value_accessor(fun = fib, stored_value = 55) # Returns function
compute_and_set = my_dict.compute_and_set_accessor(fun = fib) # Returns function

# Now we can use our `accessors`, using the function passed in earlier.
not_exists(key = "mouse", n = 10) # Returns 55 (computed)

# We can override stored_value (which is optional) with value.
not_value(key = "mouse", n = 10) # Returns 55 (cached)
not_value(key = "mouse", value = 2, n = 10) # Returns 55 (computed), since the value does not match.

compute_and_set(key = "mouse", n = 10) # Returns 55 (computed)
```

### Transactions
The Thread LRU is also thread-safe.  You can start and end transactions (atomic operations) in two ways.
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 10)

with my_dict as safe_dict:
    safe_dict.set(key = "cat", value = 1) # Returns 1
```

```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 10)

my_dict.begin_transaction()
my_dict.set(key = "cat", value = 1) # Returns 1
my_dict.end_transaction()
```

### Callbacks
The LRU Cache allows callbacks, that can be involved at certain internal events through the lifetime of the object.
- `on_insert` will only call the function `fun` if there is no value in the dictionary with that key.
- `on_update` will only call `fun` if the key already exists on an update.
- `on_upsert` will only call `fun` on a update or an insert, replaces the current function for `update` and `insert`.
- `on_remove` will only call `fun` when the cache is full, with the contents of the value being removed.

Each of these functions must accept at least two parameters: `key` and `value`, followed by any other parameters you might want.
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 2)

def f(key, value):
    print("A1", value)
    
def g(key, value):
    print("B1", value)
    
def h(key, value):
    print("C1", value)

my_dict.on_insert(fun = f)
my_dict.on_update(fun = g)
my_dict.on_remove(fun = h)

my_dict.set(key = "cat", value = "A2")   # Prints: A1 A2
my_dict.set(key = "cat", value = "B2")   # Prints: A1 A2
my_dict.set(key = "dog", value = "C2")   # Prints: A1 C2
my_dict.set(key = "mouse", value = "D2") # Prints: A1 D2
#                                                  C1 B2
```
The last line prints two steps because mouse is inserted, and cat is removed, because the max_size is 2, so the
remaining 2 keys are `dog` and `mouse`.  You may notice that the update prints `A1 A2` not `A1 B1`.  This is because
by default on an update, we will pass the old value to the callback function, so you can evaluate the item being replaced.

If instead, you want to receive the new value in our callback, or be more explicit, there are the following extended functions as well:
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 2)

def f(key, value):
    print("A1", value)
    
my_dict.on_update_old(fun = f)
my_dict.on_update_new(fun = f)

my_dict.on_upsert_old(fun = f)
my_dict.on_upsert_new(fun = f)
```
On an insert, you will always get the new value, since no value currently exists.

If we want to clear the `update`, `insert`, `upsert`, or `remove` functions, we can use the following convenience functions:
```python
from threadlru import LRUCache
my_dict = LRUCache(max_size = 2)

my_dict.clear_insert()    
my_dict.clear_update()
my_dict.clear_upsert()
my_dict.clear_remove()
```

Note, that `clear_upsert` will remove the callback for both `insert` and `update`.

## Information

### Questions, Comments, Concerns, Queries, Qwibbles?

If you have any questions, comments, or concerns please leave them in the GitHub
Issues tracker:

https://github.com/mattpaletta/theadlru/issues

### Bug reports

If you discover any bugs, feel free to create an issue on GitHub. Please add as much information as
possible to help us fixing the possible bug. We also encourage you to help even more by forking and
sending us a pull request.

https://github.com/mattpaletta/threadlru/issues

## Maintainers

* Matthew Paletta (https://github.com/mattpaletta)

## License

GPL-3.0 License. Copyright 2019 Matthew Paletta. http://mrated.ca
