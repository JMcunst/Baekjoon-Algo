#include<iostream>
#include<stack>
#include<vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int sizeOfsequence;
    int num;
    int firstNum;
    stack<int> st;
    vector<int> stNum;
    vector<int> rightFirstBig;

    cin >> sizeOfsequence;

    for (int i = 0; i < sizeOfsequence; i++) {
        cin >> num;

        st.push(num);
        stNum.push_back(num);
    }

    for (int i = 0; i < sizeOfsequence; i++) {
        stack tst;
        tst = st;
        int rightNum = tst.top();
        int rightBigNum = -1;
        firstNum = stNum[i];
        for (int j = sizeOfsequence - 1 - i; j > 0; j--) {
            if (firstNum < rightNum) {
                rightBigNum = rightNum;
            }
            tst.pop();
            rightNum = tst.top();
        }

        rightFirstBig.push_back(rightBigNum);
    }

    for (int x : rightFirstBig) {
        cout << x << " ";
    }

    return 0;
}