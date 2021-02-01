#include<iostream>
#include<queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int numberOfCard;
	int lastOfCard = 0;
	queue<int> que;

	cin >> numberOfCard;

	for (int i = 1; i <= numberOfCard; i++) {
		que.push(i);
	}

	while (que.size() > 1) {
		que.pop();
		if (que.size() == 1) {
			lastOfCard = que.front();
			break;
		}
		int topOfCard;
		topOfCard = que.front();
		que.push(topOfCard);
		que.pop();
	}

	cout << lastOfCard;

	return 0;
}