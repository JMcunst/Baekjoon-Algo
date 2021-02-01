#include<iostream>  
#include<queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int numOfSeq;
	int numOfExit;
	queue<int> que;

	cin >> numOfSeq;
	cin >> numOfExit;

	for (int i = 1; i <= numOfSeq; i++) {
		que.push(i);
	}

	cout << "<";
	while (que.size() > 0) {
		for (int i = 0; i < numOfExit - 1; i++) {
			que.push(que.front());
			que.pop();
		}
		cout << que.front();
		que.pop();

		if (!que.empty()) {
			cout << ", ";
		}
	}
	cout << ">";

	return 0;
}