# Selective_LRU_Cache_Decorator
A Python Decorator similar to but simpler than functools.lru_cache with the extra ability to select parameters. It can be used to memoize recursive functions.

## Usage
* Clone this repository and place the lru_cache module in the working directory.
* Import the LRU Cache by typing the below command.

  ```python
  from lru_cache.lru_cache import SelectiveLRUCache
  ```
* Decorate a function with the cache by placing the below command just above the function definition. The decorator takes two parameters - maxsize (the maximum size of the LRU Cache) and parameters. The "parameters" parameter is a lambda function which decides which parameters to select. In the below example, the "parameters" lambda selects only the first parameter.

  ```python
  @SelectiveLRUCache(parameters=lambda x:(x[0],), maxsize=None)
  def fibonacci(n, cntr):
  ```
 * The "parameters" lambda function takes the list of parameters as input and outputs a tuple of the selected list of parameters. Here the lambda selects the first and third parameters from the list of parameters.
 
 ```python
 @SelectiveLRUCache(parameters=lambda x:(x[0], x[2]))
 ```
 
## Results
