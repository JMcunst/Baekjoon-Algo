#include<iostream>
#include<stack>    // 표준 라이브러리 stack을 사용하기 위함
#include<cstring>

using namespace std;

int main() {

    while (1) {
        char vps[500];       // 유저로 부터 문자열을 받을 변수 선언.
        stack<char> st;

        cin.getline(vps, 501);      // 값을 받는다. 

        if (vps[0] == '.' && strlen(vps) == 1) {
            break;
        }

        for (int j = 0; j < strlen(vps); j++) {
            if (vps[j] == '(' || vps[j] == '[') { //스택이 비었을때와 문자값이 '('일때
                st.push(vps[j]);
            }
            else if (vps[j] == ')') {       //스택이 비어있지 않고, 문자값이 ')'일때, 스택의 상단이 '('라면
                if (!st.empty() && st.top() == '(') {
                    st.pop();
                }
                else {
                    st.push(vps[j]);
                    break;
                }
            }
            else if (vps[j] == ']') {
                if (!st.empty() && st.top() == '[') {
                    st.pop();
                }
                else {
                    st.push(vps[j]);
                    break;
                }
            }
        }
        if (st.empty()) {
            cout << "yes" << endl;
        }
        else {
            cout << "no" << endl;
        }

    }
    return 0;
}
