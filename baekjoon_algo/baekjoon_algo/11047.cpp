#include<iostream>  
#include <vector>
#include <algorithm>

using namespace std;

int cmp(int a, int b) { // 내림차순
	return a > b;
}
int main() {
	int kindOfCoin, targetAmount, minAmountOfCoint = 0;
	cin >> kindOfCoin >> targetAmount;
	vector<int> valueOfCoin(kindOfCoin);

	for (int i = 0; i < kindOfCoin; i++) {
		cin >> valueOfCoin[i];
	}
	sort(valueOfCoin.begin(), valueOfCoin.end(), cmp);

	for (int i = 0; i < kindOfCoin; i++) {
		while (targetAmount - valueOfCoin[i] >= 0) {
			minAmountOfCoint++;
			targetAmount -= valueOfCoin[i];
		}
	}
	cout << minAmountOfCoint << '\n';
}