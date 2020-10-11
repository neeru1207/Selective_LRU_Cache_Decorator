# Selective_LRU_Cache_Decorator
A Python Decorator similar to but much simpler than functools.lru_cache with the extra ability to select parameters. It can be used to memoize recursive functions.

## Usage
* Clone this repository and place the lru_cache module in the working directory.
* Import the LRU Cache in your Python code by typing the below command.

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
 
## Performance
 * When tested on the recursive fibonacci function, a **46000 times** faster execution and a **29000 times** reduction in the number of function calls was achieved.
 * Fibonacci(40) without the cache took *331160289* function calls and *92.686* seconds as shown below:
 
    ![](https://github.com/neeru1207/Selective_LRU_Cache_Decorator/blob/master/Without_Cache_Speed.png)
  
 * Fibonacci(40) with the cache took *1140* function calls and only *0.002* seconds to execute as shown below:
 
    ![](https://github.com/neeru1207/Selective_LRU_Cache_Decorator/blob/master/With_Cache_Speed.png)
  
## Contributing
 * Feel free to open an issue if any bug is found.
 * Pull requests are welcome. Just make sure to contribute readable, well commented, and tested code.
