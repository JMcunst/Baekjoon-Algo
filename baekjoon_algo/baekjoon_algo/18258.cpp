#include<iostream>
#include<queue>
#include<string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int numberOfCommand;
	queue<int> que;
	string str_command;

	cin >> numberOfCommand;

	for (int i = 0; i < numberOfCommand; i++) {
		cin >> str_command;

		if (str_command == "push") {
			int number_queue;
			cin >> number_queue;
			que.push(number_queue);
		}
		else if (str_command == "pop") {
			if (!que.empty()) {
				cout << que.front() << "\n";
				que.pop();
			}
			else {
				cout << -1 << "\n";
			}
		}
		else if (str_command == "size") {
			cout << que.size() << "\n";
		}
		else if (str_command == "empty") {
			if (que.empty()) {
				cout << 1 << "\n";
			}
			else {
				cout << 0 << "\n";
			}
		}
		else if (str_command == "front") {
			if (!que.empty()) {
				cout << que.front() << "\n";
			}
			else {
				cout << -1 << "\n";
			}
		}
		else if (str_command == "back") {
			if (!que.empty()) {
				cout << que.back() << "\n";
			}
			else {
				cout << -1 << "\n";
			}
		}
	}

	return 0;
}