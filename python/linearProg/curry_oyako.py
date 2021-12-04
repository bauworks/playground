import pulp

#線形計画の定義
problem = pulp.LpProblem('Curry_Oyako', pulp.LpMaximize)

#変数の定義
Curry = pulp.LpVariable('Curry', 0, 10, 'Integer') 
Oyako = pulp.LpVariable('Oyako', 0, 10, 'Integer') 

#目的関数の定義
problem += 2*Curry + 3*Oyako

#制約条件の定義
problem += Curry + 2*Oyako <= 10
problem += 2*Curry + Oyako <= 8

#解く
status = problem.solve()
print(pulp.LpStatus[status])

#結果表示
print("Result")
print("Curry:",Curry.value())
print("Oyako:",Oyako.value())
