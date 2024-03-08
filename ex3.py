import operator

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(tokens):
    if len(tokens) == 1:
        return Node(tokens[0])
    
    min_precedence = float('inf')
    min_index = -1
    paren_count = 0
    for i in range(len(tokens)-1, -1, -1):
        token = tokens[i]
        if token == ')':
            paren_count += 1
        elif token == '(':
            paren_count -= 1
        elif token in OPERATORS and paren_count == 0:
            precedence = get_precedence(token)
            if precedence <= min_precedence:
                min_precedence = precedence
                min_index = i
    
    operator_node = Node(tokens[min_index])
    operator_node.left = build_tree(tokens[:min_index])
    operator_node.right = build_tree(tokens[min_index+1:])
    return operator_node

def get_precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    return 0

def evaluate_tree(root):
    if root.value.isdigit():
        return int(root.value)
    else:
        left_val = evaluate_tree(root.left)
        right_val = evaluate_tree(root.right)
        return OPERATORS[root.value](left_val, right_val)

def evaluate_expression(expression):
    tokens = expression.split()
    root = build_tree(tokens)
    return evaluate_tree(root)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <expression>")
        sys.exit(1)
    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print("Result:", result)
