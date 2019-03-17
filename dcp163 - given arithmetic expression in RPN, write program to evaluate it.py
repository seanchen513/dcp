"""
dcp#163

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

# RPN, aka postfix notation

# Python stack: use list with append(), pop()
# Evaluates from left to right; it's also possible to evaluate right to left.
def evaluate_rpn_exp(rpn_exp):
    stack = []

    for token in rpn_exp:
        if token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            stack.append(result)
        else: # must be operand since we assume expression is always valid
            stack.append(token)

    return stack.pop()


rpn_exp = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']

result = evaluate_rpn_exp(rpn_exp)

print("result = {}".format(result))

