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

# 修正されたCSVデータ
csv_data = [
    (1, 'X0', False, None, None, 'PC1', '301'),
    (2, 'X1', False, None, None, 'PC1', '301'),
    (3, 'T1', False, None, None, 'PC1', '302'),
    (4, 'T0', False, None, None, '301', '302'),
    (5, 'T0K5', False, None, None, '301', 'NC1')
]

# Nodeのインスタンス生成
nodes = [Node(*row) for row in csv_data]

# ブロックノードの生成
block_nodes = {}

# ANDブロックとORブロックの判定用の辞書
and_block_dict = {}
or_block_dict = {}

# ブロックノードへの子ノードの追加とparentの設定
for node in nodes:
    if not node.isBlock and node.parent is None:
        # ブロックノードが存在しない場合は新しく作成
        if node.id not in block_nodes:
            parent_block_node = Node(id=node.id, name=f'B{node.id}', isBlock=True, andor=None, parent=None, line1=set(), line2=set())
            block_nodes[node.id] = parent_block_node

        # ノード情報を取得
        block_node = block_nodes[node.id]

        # ANDブロックかどうかを判定
        if (node.line1, node.line2) in and_block_dict or (node.line2, node.line1) in and_block_dict:
            # すでにANDブロックがある場合
            block_node.andor = "AND" if block_node.andor is None else "OR"
            block_node.line1.add(node.line1)
            block_node.line2.add(node.line2)
            # ノードのparentをブロックノードに設定
            node.parent = block_node.id
        else:
            # ANDブロックでない場合はORブロックかどうかを判定
            if (node.line1, node.line2) in or_block_dict or (node.line2, node.line1) in or_block_dict:
                # すでにORブロックがある場合
                block_node.andor = "OR" if block_node.andor is None else "AND"
                block_node.line1.add(node.line1)
                block_node.line2.add(node.line2)
                # ノードのparentをブロックノードに設定
                node.parent = block_node.id
            else:
                # ANDブロックでもORブロックでもない場合
                block_node.andor = None
                # 新たなANDブロックかORブロックの開始
                and_block_dict[(node.line1, node.line2)] = node.id
                or_block_dict[(node.line1, node.line2)] = node.id
                block_node.line1.add(node.line1)
                block_node.line2.add(node.line2)
                # ノードのparentをブロックノードに設定
                node.parent = block_node.id

# ブロックノードの情報を表示
for node in block_nodes.values():
    print(f"Node {node.id}: Name={node.name}, isBlock={node.isBlock}, andor={node.andor}, parent={node.parent}, Line1={node.line1}, Line2={node.line2}")

# ノード情報の表示
for node in nodes:
    print(f"Node {node.id}: Name={node.name}, isBlock={node.isBlock}, parent={node.parent}, Line1={node.line1}, Line2={node.line2}")

