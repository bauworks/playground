# 入力ファイル名と出力ファイル名
input_file = "IN.txt"
output_file = "OUT.txt"

# 接続情報を格納するディクショナリ
connections = {}

# IN.txtから接続情報を読み込む
with open(input_file, "r") as infile:
    for line in infile:
        parts = line.strip().split()
        if len(parts) == 2:
            source, destination = parts
            if source not in connections:
                connections[source] = []
            connections[source].append(destination)

# ラダープログラムの命令に変換する関数
def convert_to_ladder_program(connections, current_point):
    ladder_program = []
    if current_point in connections:
        destinations = connections[current_point]
        for destination in destinations:
            ladder_program.extend(convert_to_ladder_program(connections, destination))
        if len(destinations) > 1:
            ladder_program.insert(0, "OR " + " OR ".join(destinations))
        ladder_program.insert(0, "AND " + current_point)
    else:
        ladder_program.append("LD " + current_point)
    return ladder_program

# 出力ファイルに変換結果を書き込む
with open(output_file, "w") as outfile:
    ladder_program = convert_to_ladder_program(connections, "ST")
    for instruction in ladder_program:
        outfile.write(instruction + "\n")
    # 最後のOUT命令を追加
    outfile.write("OUT ED")

print("変換が完了しました。OUT.txtに結果が保存されました。")

