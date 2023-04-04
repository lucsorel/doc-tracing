'''
python -m trace --trace 01_trace_factorial.py 2
python -m trace --count 01_trace_factorial.py 2
python -m trace --listfuncs 01_trace_factorial.py 2
'''
from sys import argv

def factorial(n: int) -> int:
    assert n > 0
    if n == 1:
        return 1
    return n * factorial(n - 1)

factorial(int(argv[1]))
