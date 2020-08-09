from lru_cache.lru_cache import SelectiveLRUCache
import cProfile

@SelectiveLRUCache(parameters=lambda x:(x[0],), maxsize=None)
def FibonacciWithLRU(n, cntr):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return FibonacciWithLRU(n-1, cntr)+FibonacciWithLRU(n-2, cntr)

def Fibonacci(n, cntr):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1, cntr)+Fibonacci(n-2, cntr)

cProfile.runctx("Fibonacci(40, 0)", globals(), locals())
cProfile.runctx("FibonacciWithLRU(40, 0)", globals(), locals())