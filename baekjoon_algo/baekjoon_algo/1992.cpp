#include<iostream>

using namespace std;

int paper[64][64];

void quadTree(int x, int y, int N) {
	int blackCount = 0;
	for (int i = x; i < x + N; i++) {
		for (int j = y; j < y + N; j++) {
			if (paper[i][j]) {
				blackCount++;
			}
		}
	}
	if (!blackCount) cout << "0"; // 하얀색
	else if (blackCount == N * N) cout << "1"; // 검은색
	else {   // 쪼갬=재귀
		cout << "("; // 쪼개면서 (로 열어준다.
		quadTree(x, y, N / 2);  // 왼쪽 위 사각형
		quadTree(x, y + N / 2, N / 2); // 오른쪽 위 사각형
		quadTree(x + N / 2, y, N / 2); // 왼쪽 아래 사각형
		quadTree(x + N / 2, y + N / 2, N / 2); // 오른쪽 아래 사각형
		cout << ")"; // 재귀가 끝나면 )로 닫아준다.
	}
	return;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	char tmp;

	cin >> n;
	cin.get();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin.get(tmp);
			paper[i][j] = tmp - 48;
		}
		cin.get();
	}
	/*int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> paper[i][j];
		}
	}*/

	quadTree(0, 0, n);

	return 0;
}