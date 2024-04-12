def infix_to_prefix(expression):
    def is_operator(char):
        return char in "+-*/^"

    def precedence(operator):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence.get(operator, 0)

    def infix_to_prefix(expression):
        output = []
        operator_stack = []
        tokens = expression.split()

        for token in reversed(tokens):
            if token.isnumeric():
                output.append(token)
            elif token == ")":
                operator_stack.append(token)
            elif token == "(":
                while operator_stack and operator_stack[-1] != ")":
                    output.append(operator_stack.pop())
                operator_stack.pop()  # ")" をスタックから取り除く
            elif is_operator(token):
                while (
                    operator_stack
                    and is_operator(operator_stack[-1])
                    and precedence(operator_stack[-1]) > precedence(token)
                ):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        return " ".join(reversed(output))

    return infix_to_prefix(expression)

# テスト
infix_expression = "3 + 4 * 2 / (1 - 5)^2"
prefix_expression = infix_to_prefix(infix_expression)
print("中置記法:", infix_expression)
print("逆ポーランド記法 (Prefix Notation):", prefix_expression)

