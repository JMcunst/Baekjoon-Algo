#include<iostream>
#include<stack>    // 표준 라이브러리 stack을 사용하기 위함
#include<string>   // string 타입을 쓰기 위해 포함

using namespace std;

int main() {
    int numberOfCommand; // 명령어수 N 선언
    stack<int> st; //  int Data Type을 넣을 stack 선언
    string str_command;    // 명령어 push, pop, size, empty, top 등의 명령어를 받을 string 변수 선언

    cin >> numberOfCommand;  //명령어수 N을 유저로 부터 받는다. 

    for (int i = 0; i < numberOfCommand; i++) {
        cin >> str_command;       // 유저로 부터 명령어를 받는다. 

        if (str_command == "push") {  //push 일때 // 뒤에 오는 숫자를 st에 넣는다.
            int number_stack;
            cin >> number_stack;
            st.push(number_stack);
        }
        else if (str_command == "pop") {    //pop 일때 // st의 젤 위의 값을 뽑아 출력한다. 
            if (!st.empty()) {
                cout << st.top() << endl;
                st.pop();
            }
            else {
                cout << "-1" << endl;
            }
        }
        else if (str_command == "size") {   // size 일때 // st의 사이즈를 출력
            cout << st.size() << endl;
        }
        else if (str_command == "empty") {    // empty 일때 // st가 비었는지 아닌지, 비었으면 1, 않비었으면 0
            if (st.empty()) {
                cout << "1" << endl;
            }
            else {
                cout << "0" << endl;
            }
        }
        else if (str_command == "top") {    // top 일때 // st의 젤 위를 출력, pop은 젤 위의 값을 출력하고 st에서 지우는 반면, top은 젤 위를 출력만
            if (!st.empty()) {
                cout << st.top() << endl;
            }
            else {
                cout << "-1" << endl;
            }
        }
    }
    return 0;
}