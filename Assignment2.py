# 2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


def parenthesis_generator(n: int, combo_result: str = '', open_brackets: int = 0, close_brackets: int = 0, final_result: list = None) -> list | None:
    """
    Generates all combinations of well-formed parentheses for a given number of pairs.

    Args:
        n (int): The number of pairs of parentheses.
        combo_result (str, optional): The current combination of parentheses. Defaults to ''.
        open_brackets (int, optional): The number of open parentheses used so far. Defaults to 0.
        close_brackets (int, optional): The number of close parentheses used so far. Defaults to 0.
        final_result (list, optional): The list to store all valid combinations. Defaults to None.

    Returns:
        list: A list of all valid combinations of parentheses.
    """
    if final_result is None:
        final_result = []

    if open_brackets == close_brackets == n:
        final_result.append(combo_result)
        return
    
    if open_brackets < n:
        parenthesis_generator(n, combo_result + '(', open_brackets + 1, close_brackets, final_result)
    
    if close_brackets < open_brackets:
        parenthesis_generator(n, combo_result + ')', open_brackets, close_brackets + 1, final_result)
    
    return final_result

if __name__ == "__main__":
    n: int = int(input("Enter the number of pairs of parentheses: "))
    print(parenthesis_generator(n))