'''
cd examples
python -m math_cli --factorial 3
python -m math_cli --fibonacci 3

# displays autogenerated documentation
python -m pydoc -p 1234 -b
'''
from argparse import ArgumentParser, Namespace

from pydoctrace.doctrace import trace_to_puml

from math_cli.factorial import factorial_reduce
from math_cli.fibonacci import fibonacci_recurse
from math_cli.validation import validate_positive_int


@trace_to_puml
def fibonacci(value: int):
    value = validate_positive_int(value)
    result = fibonacci_recurse(value)
    print(f'fibonacci {value} = {result}')

@trace_to_puml
def factorial(value: int):
    try:
        result = factorial_reduce(value)
    except ValueError as ve:
        result = str(ve)
    print(f'factorial {value} = {result}')

def math_cli():
    '''Cli entrypoint'''
    parser = ArgumentParser(description='Math CLI')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--factorial', type=int, help='a positive integer')
    group.add_argument('--fibonacci', type=int, help='a positive integer')
    args = parser.parse_args()
    if args.factorial is not None:
        factorial(args.factorial)
    elif args.fibonacci is not None:
        fibonacci(args.fibonacci)

if __name__ == '__main__':
    math_cli()
