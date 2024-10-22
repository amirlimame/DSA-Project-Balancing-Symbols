# DSA Project Balancing Symbols

## Description

This program uses the stack data structure to check for syntax errors in a source file, specifically balanced symbols. This works by appending a new opening symbol to a stack once found, and popping a pair from the stack when the respective closing symbol is found. If no syntax errors are found in the source file, or the stack is empty on completion, the program will output "No syntax errors". If syntax errors are found in the source file, or the stack is not empty on completion, the program will output "Syntax errors occurred".

## Usage

Run the source file with Python and pass the input source file in-line.

```bash
python3 balancingSymbols.py (HelloWord.java/HelloWorld_wrong.java)
```

## Sample Output

```bash
python3 balancingSymbols.py HelloWorld.java
No syntax errors
```
```bash
python3 balancingSymbols.py HelloWorld_wrong.java
Syntax errors occurred
```