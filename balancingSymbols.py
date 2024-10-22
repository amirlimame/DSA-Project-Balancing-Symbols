# Balancing Symbols - Amir Limame

import sys

def isBalanced(symbols):
    # Dictionary to hold the pairs of matching brackets
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    
    # Iterate over each character in the input
    for char in symbols:
        # If the character is an opening symbol, push to the stack
        if char in '({[':
            stack.append(char)
        # If the character is a closing symbol
        elif char in ')}]':
            # If the stack is empty or the top of the stack doesn't match the closing symbol
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            # Pop the matching opening symbol from the stack
            stack.pop()
    
    # If the stack is empty, all symbols were matched correctly
    return not stack

def checkBalance(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the file content
            if isBalanced(content):
                print(f"No syntax errors")
            else:
                print(f"Syntax errors occurred")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the script has been provided with a file argument
    if len(sys.argv) != 2:
        print("Usage: python3 balancingSymbols.py <source_file>")
    else:
        # Get the file name from the command-line argument
        filename = sys.argv[1]
        checkBalance(filename)
