#include<iostream>
#include<queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int numberOfCard;
	queue<int> que;

	cin >> numberOfCard;

	for (int i = 1; i <= numberOfCard; i++) {
		que.push(i);
	}

	while (que.size() > 1) {
		que.pop();
		que.push(que.front());
		que.pop();
	}

	cout << que.front();

	return 0;
}