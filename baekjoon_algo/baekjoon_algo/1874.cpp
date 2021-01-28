#include<iostream>
#include<stack>    // 표준 라이브러리 stack을 사용하기 위함
#include<queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int sizeOfsequence;
    int num;
    stack<int> st;
    queue<int> que;
    string seq_completed;
    int stStartNum;
    bool isNo = false;

    cin >> sizeOfsequence;

    for (int i = 0; i < sizeOfsequence; i++) {
        cin >> num;
        que.push(num);
    }

    for (int i = 1; i <= que.front(); i++) {
        st.push(i);
        seq_completed += '+';
    }
    stStartNum = que.front();
    st.pop();
    que.pop();
    seq_completed += '-';

    while (1) {
        if (que.empty()) {
            break;
        }

        int nowNumFromQueue = que.front();

        if (st.empty() || st.top() < nowNumFromQueue) {
            st.push(++stStartNum);
            seq_completed += '+';
        }
        else if (st.top() == nowNumFromQueue) {
            st.pop();
            que.pop();
            seq_completed += '-';
        }
        else if (st.top() > nowNumFromQueue) {
            isNo = true;
            break;
        }

    }

    if (isNo) {
        cout << "NO\n";
    }
    else {
        for (int i = 0; i < seq_completed.size(); i++) {
            cout << seq_completed[i] << "\n";
        }
    }
    return 0;
}