#include<iostream>
#include<deque>
#include<queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int sizeOfDeque;
    int numOfSearch;
    int countOfOperation = 0;
    deque<int> deque;
    queue<int> que;

    cin >> sizeOfDeque;
    for (int i = 1; i <= sizeOfDeque; i++) {
        deque.push_back(i);
    }

    cin >> numOfSearch;
    for (int i = 0; i < numOfSearch; i++) {
        int num;
        cin >> num;
        que.push(num);
    }

    for (int k = 0; k < numOfSearch; k++) {
        int nowIndex = 0;
        int nowFind = que.front();
        int nowDequeValue;
        for (int i = 0; i < deque.size(); i++) {
            if (nowFind == deque[i]) {
                nowIndex = i;
                break;
            }
        }

        if (nowIndex >= deque.size() - nowIndex) {
            while (true) {
                nowDequeValue = deque.back();
                if (deque.front() == nowFind) {
                    que.pop();
                    deque.pop_front();
                    break;
                }
                countOfOperation++;
                deque.push_front(nowDequeValue);
                deque.pop_back();
            }

        }
        else {
            while (true) {
                nowDequeValue = deque.front();
                if (deque.front() == nowFind) {
                    que.pop();
                    deque.pop_front();
                    break;
                }
                countOfOperation++;
                deque.push_back(nowDequeValue);
                deque.pop_front();
            }
        }
    }

    cout << countOfOperation;

    return 0;
}