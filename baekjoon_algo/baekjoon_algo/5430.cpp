#include<iostream>
#include<deque>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int numOfTest;

	cin >> numOfTest;

	for (int i = 0; i < numOfTest; i++) {
		string funRD;
		int numOfSeq;
		string seq;
		bool isFront = true;
		bool isError = false;
		deque<int> deq;

		cin >> funRD;
		cin >> numOfSeq;
		cin >> seq;

		int indexOfseq = 1;
		while (seq[indexOfseq] != '\0') {
			bool isNum = false;
			int num = 0;

			while ((seq[indexOfseq] >= '0') && (seq[indexOfseq] <= '9')) {
				num *= 10; // 자리수 올려주기
				num += int(seq[indexOfseq] - '0'); // char형->int형 변환
				isNum = true;
				indexOfseq++;
			}
			if (isNum) {
				deq.push_back(num);
			}
			indexOfseq++;
		}

		for (int j = 0; j < funRD.size(); j++) {
			if (funRD[j] == 'R') {
				isFront = !isFront;
			}
			else if (funRD[j] == 'D') {
				if (deq.empty()) {
					isError = true;
					break;
				}
				else if (isFront) {
					deq.pop_front();
				}
				else {
					deq.pop_back();
				}
			}
		}


		if (!isError) {
			int resultDeqSize = deq.size();
			cout << "[";
			for (int i = 0; i < resultDeqSize; i++) {
				if (isFront) {
					cout << deq.front();
					deq.pop_front();
				}
				else {
					cout << deq.back();
					deq.pop_back();
				}

				if (i != resultDeqSize - 1) {
					cout << ",";
				}
			}
			cout << "]\n";
		}
		else {
			cout << "error\n";
		}

	}

	return 0;
}