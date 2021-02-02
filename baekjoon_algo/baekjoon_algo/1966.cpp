#include<iostream>
#include<queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int numOfTest;

	cin >> numOfTest;

	for (int i = 1; i <= numOfTest; i++) {
		int numOfSeq;
		int idxOfDocument;
		int answer = 0;
		queue<pair<int, int>> que;
		priority_queue<int> pq;

		cin >> numOfSeq;
		cin >> idxOfDocument;
		for (int j = 0; j < numOfSeq; j++) {
			int pri;
			cin >> pri;
			que.push({ j,pri });
			pq.push(pri);
		}

		while (!que.empty()) {
			int nowIdx = que.front().first;
			int nowPri = que.front().second;
			que.pop();

			if (pq.top() == nowPri) {
				answer++;
				pq.pop();
				if (idxOfDocument == nowIdx) {
					cout << answer << "\n";
					break;
				}
			}
			else {
				que.push({ nowIdx, nowPri });
			}
		}
	}

	return 0;
}