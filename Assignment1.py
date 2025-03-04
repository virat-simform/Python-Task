### Question 1: Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.


# Importing the reduce function from the functools module for iterating over the numbers with a for loop
# Reduce is not a built-in function in python3 anymore
from functools import reduce
import sys


def word_to_num(word: str) -> int:
    """
    Convert a string of number words to an integer.
    
    Args:
        word (str): The word to convert
    Returns:
        int: The number representation of the word
    """
    d: dict[str, str] = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    word = word.lower()
    ans: str = reduce(lambda x, y: x.replace(y, d[y]), d, word)
    if ans.isnumeric():
        return int(ans)
    else:
        raise ValueError("Input must be a numbers in word")

def num_to_word(num: int) -> str:
    """
    Converts a number to a word
    Args:
        num (int): The number to convert
    Returns:
        str: The word representation of the number
    """
    d: dict[int, str] = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    return reduce(lambda x, y: x + y, map(lambda i: d[int(i)], str(num)))


def gcd(a: int, b: int) -> int:
    """
    Compute the GCD of two numbers using Euclidean algorithm
    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The GCD of the two numbers
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1: str = input("Enter no 1 in word: ")
        num2: str = input("Enter no 2 in word: ")
        
        if not num1.strip() or not num2.strip():
            raise ValueError("Input cannot be empty")   
        if not num1.isalpha() or not num2.isalpha():  
            raise ValueError("Input must be string")
            
        num1: int = word_to_num(num1)
        num2: int = word_to_num(num2)
        
        result: str = num_to_word(gcd(num1, num2))
        print(f"Result: {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    
