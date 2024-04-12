import csv

class Node:
    def __init__(self, id, name, isBlock, andor, parent, line1, line2):
        self.id = id
        self.name = name
        self.isBlock = isBlock
        self.andor = andor
        self.parent = parent
        self.line1 = line1
        self.line2 = line2

# CSVデータ
csv_data = [
    (1, 'X0', False, None, None, 'PC1', '301'),
    (2, 'X1', False, None, None, 'PC1', '301'),
    (3, 'T1', False, None, None, 'PC1', '302'),
    (4, 'T0', False, None, None, '301', '302'),
    (5, 'T0K5', False, None, None, '301', 'NC1')
]

# Nodeのインスタンス生成
nodes = [Node(*row) for row in csv_data]

# ノード情報の表示（例）
for node in nodes:
    print(f"Node {node.id}: Name={node.name}, Line1={node.line1}, Line2={node.line2}")


