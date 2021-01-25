#include<iostream>
#include<stack>    // 표준 라이브러리 stack을 사용하기 위함
#include<string>

using namespace std;

int main() {
    int numberOfVPS; // VPS 문자열 개수 K 선언

    cin >> numberOfVPS;  //K 값을 받는다. 

    for (int i = 0; i < numberOfVPS; i++) {
        string vps;       // 유저로 부터 문자열을 받을 변수 선언.
        stack<char> st;

        cin >> vps;       // 문자열(VPS)을 받는다. 

        for (int j = 0; j < vps.length(); j++) {
            if (st.empty() || vps[j] == '(') { //스택이 비었을때와 문자값이 '('일때
                st.push(vps[j]);
            }
            else if (st.top() == '(') {       //스택이 비어있지 않고, 문자값이 ')'일때, 스택의 상단이 '('라면
                st.pop();
            }
        }

        if (st.empty()) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }

    }
    return 0;
}