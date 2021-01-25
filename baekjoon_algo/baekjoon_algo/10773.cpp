#include<iostream>
#include<stack>    // 표준 라이브러리 stack을 사용하기 위함

using namespace std;

int main() {
    int numberOfRecord; // 명령어수 N 선언
    stack<int> st; //  int Data Type을 넣을 stack 선언
    int record;
    int sum = 0;
    int stack_size = 0;

    cin >> numberOfRecord;  //명령어수 N을 유저로 부터 받는다. 

    for (int i = 0; i < numberOfRecord; i++) {
        cin >> record;       // 유저로 부터 명령어를 받는다. 

        if (record == 0) {  //push 일때 // 뒤에 오는 숫자를 st에 넣는다.
            st.pop();
        }
        else {    //pop 일때 // st의 젤 위의 값을 뽑아 출력한다. 
            st.push(record);
        }

    }

    stack_size = st.size();  // stack의 size를 저장한다. 

    for (int j = 0; j < stack_size; j++) {   // stack의 사이즈 만큼 반복. st.size()를 쓸수 없다. 반복문을 돌면서 stack의 사이즈가 변하기 때문.
        sum += st.top();     // 제일 위의 값을 sum에 더한다. 
        st.pop();            // 스택에서 제일 위의 값을 지운다. 
    }

    cout << sum << endl;

    return 0;
}