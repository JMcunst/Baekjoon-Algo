#include<iostream>

using namespace std;

int paper[129][129];
int whitePaper = 0;
int bluePaper = 0;

void paperColorDecisionByDivdeConquer(int x, int y, int N) {
	int tempBlueCount = 0; // 
	//2중 for문으로 0인지 1인지 탐색
	for (int i = x; i < x + N; i++) {
		for (int j = y; j < y + N; j++) {
			if (paper[i][j]) {  //파란색일때
				tempBlueCount++;  // 파란색 개수 count
			}
		}
	}
	if (!tempBlueCount) whitePaper++; // 하얀색
	else if (tempBlueCount == N * N) bluePaper++; // 파란색
	else {   // 쪼갬
		paperColorDecisionByDivdeConquer(x, y, N / 2);  // 왼쪽 위 사각형
		paperColorDecisionByDivdeConquer(x, y + N / 2, N / 2); // 오른쪽 위 사각형
		paperColorDecisionByDivdeConquer(x + N / 2, y, N / 2); // 왼쪽 아래 사각형
		paperColorDecisionByDivdeConquer(x + N / 2, y + N / 2, N / 2); // 오른쪽 아래 사각형
	}
	return;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> paper[i][j];
		}
	}
	paperColorDecisionByDivdeConquer(0, 0, n);

	cout << whitePaper << "\n";
	cout << bluePaper;
	return 0;
}