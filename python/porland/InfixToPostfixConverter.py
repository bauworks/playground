class InfixToPostfixConverter:
    def __init__(self):
        # 演算子の優先順位を定義
        self.operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # 中置記法からポーランド記法への変換メソッド
    def convert_to_postfix(self, infix_expression):
        operator_stack = []
        postfix_expression = []

        for token in infix_expression:
            if token.isdigit():
                postfix_expression.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    postfix_expression.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()  # '(' を捨てる
            elif token in self.operator_precedence:
                while operator_stack and self.operator_precedence[token] <= self.operator_precedence[operator_stack[-1]]:
                    postfix_expression.append(operator_stack.pop())
                operator_stack.append(token)

        # スタックに残った演算子をポーランド記法に追加
        while operator_stack:
            postfix_expression.append(operator_stack.pop())

        return ''.join(postfix_expression)

# 実行例と解説
if __name__ == "__main__":
    # 中置記法の式を入力
    infix_expression = input("中置記法の式を入力してください: ")

    # 中置記法からポーランド記法へ変換
    converter = InfixToPostfixConverter()
    postfix_expression = converter.convert_to_postfix(infix_expression)

    # 結果を出力
    print("ポーランド記法:", postfix_expression)



