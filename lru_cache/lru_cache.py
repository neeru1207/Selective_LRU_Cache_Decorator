from collections import OrderedDict
import sys
class SelectiveLRUCache:
    
    def __init__(self, parameters = lambda x:x, maxsize=128):
        """Selective LRU Cache
        Args:
            parameters ([lambda], optional): [The lambda that outputs a tuple of selected parameters]. Defaults to lambda x:x.
            maxsize (int, optional): [The maximum size of the LRU Cache]. Defaults to 128.
        Raises:
            Exception: [description]
        """
        #A function to check if a variable is a lambda
        def islambda(v):
            LAMBDA = lambda:0
            return isinstance(v, type(LAMBDA)) and v.__name__ == LAMBDA.__name__
        #Set maxsize to INF if it is None
        self.maxsize = maxsize if maxsize is not None else sys.maxsize
        if self.maxsize < 0:
            raise Exception("VALUE ERROR, Negative Max Size")
        # Check if parameters is a lambda
        if not islambda(parameters):
            raise Exception("ILLEGAL ARGUMENT for parameters, Expected lambda")
        self.parameters = parameters
        #The cache is an ordered dictionary
        self.cache = OrderedDict()

    def get(self, key):
        """Get the key
        Args:
            key ([tuple]): [A tuple of the values of the selected parameters]
        Returns:
            [None]: [If KeyError occurs]
            [Cached Value] : [If the key:value pair exists in the LRU Cache]
        """        
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

    def set(self, key, value):
        """Add the key:value pair and it's timestamp to the LRU cache
        Args:
            key ([type]): [description]
            value ([type]): [description]
        """        
        try:
            self.cache.pop(key)
        except KeyError:
            #If the cache is full, evict the least recently used item
            if len(self.cache) >= self.maxsize:
                self.cache.popitem(last=False)
        self.cache[key] = value

    def __call__(self, func):
        """Call function that makes an instance of this class callable
        Args:
            func (function): [The function to be decorated by the cache]
        """        
        #The decorated function
        def cached_func(*args):
            #Get the tuple of selected parameters
            selected_args = self.parameters(args)
            #Make it a tuple if it isn't a tuple
            if not isinstance(selected_args, tuple):
                #Make it a tuple if it is a list
                try:
                    selected_args = tuple(selected_args)
                #Wrap in a tuple if it isn't an iterable
                except:
                    selected_args = (selected_args,)
            #Check if the present function call is stored in the cache
            if self.get(selected_args) is None:
                self.set(selected_args, func(*args))
            return self.get(selected_args)
        return cached_func

# @SelectiveLRUCache(parameters=lambda x:(x[0],), maxsize=None)
# def Fibonacci(n, cntr):
#     if n<0:
#         print("Incorrect input")
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return Fibonacci(n-1, cntr)+Fibonacci(n-2, cntr)
# print(Fibonacci(40, 0))