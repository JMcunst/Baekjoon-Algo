# 트리 tree_a와 트리 tree_b가 주어집니다.
# tree_a는 n개의 정점으로 이루어져 있고 각 정점들은 1~n 번호를 겹치지 않게 가지고 있습니다.
# tree_b도 n개의 정점으로 이루어져 있고 각 정점들은 1~n 번호를 겹치지 않게 가지고 있습니다.

# 당신은 tree_b를 tree_a와 똑같이 만들고 싶습니다.

# 당신은 두 가지 작업을 할 수 있습니다.

# tree_b에 존재하는 간선 하나를 삭제하고 새로운 간선 하나를 추가합니다.
# tree_b에 존재하는 두 정점의 번호를 바꿉니다.
# 1번 작업은 무제한으로 할 수 있지만 2번 작업은 최대 m번까지 밖에 할 수 없습니다.

# tree_a의 간선 정보를 담고 있는 2차원 정수 배열 a, tree_b의 간선 정보를 담고 있는 2차원 정수 배열 b, 2번 작업을 할 수 있는 횟수 m이 매개변수로 주어집니다. 이때, tree_b를 tree_a와 똑같이 만들기 위해 해야 하는 1번 작업의 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 1 ≤ a의 길이 = b의 길이 ≤ 12
# a의 원소는 [x, y] 형태이며, tree_a에서 x번 정점과 y번 정점이 양방향 간선으로 연결되어 있다는 뜻입니다.
# b의 원소는 [x, y] 형태이며, tree_b에서 x번 정점과 y번 정점이 양방향 간선으로 연결되어 있다는 뜻입니다.
# 1 ≤ x, y ≤ 1 + a의 길이
# x ≠ y
# 동일한 간선에 대한 정보가 중복해서 주어지지 않습니다.
# 항상 하나의 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없습니다.
# 0 ≤ m ≤ 3
# 입출력 예
# a	b	m	result
# [[1, 2], [2, 3]]	[[1, 3], [3, 2]]	1	0
# [[1, 2], [3, 1], [2, 4], [3, 5]]	[[2, 1], [4, 1], [2, 5], [3, 2]]	1	1
# [[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]]	[[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]]	2	2