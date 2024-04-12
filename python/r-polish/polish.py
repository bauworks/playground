def infix_to_rpn(expression):
    # 演算子の優先順位を定義
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(token):
        return token in "+-*/^"

    def higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    def infix_to_postfix(expression):
        output = []
        operator_stack = []
        tokens = expression.split()

        for token in tokens:
            if token.isnumeric():
                output.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    output.append(operator_stack.pop())
                operator_stack.pop()  # "(" をスタックから取り除く
            elif is_operator(token):
                while (
                    operator_stack
                    and is_operator(operator_stack[-1])
                    and higher_precedence(operator_stack[-1], token)
                ):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        return " ".join(output)

    return infix_to_postfix(expression)


infix_expression = "3 + 4 * 2 / (1 - 5)^2"
rpn_expression = infix_to_rpn(infix_expression)
print("中置記法:", infix_expression)
print("ポーランド記法:", rpn_expression)

