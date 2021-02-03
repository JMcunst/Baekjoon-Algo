#include<iostream>
#include<deque>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int numberOfCommand;
    deque<int> deque;
    string str_command;

    cin >> numberOfCommand;

    for (int i = 0; i < numberOfCommand; i++) {
        cin >> str_command;

        if (str_command == "push_front") {
            int num;
            cin >> num;
            deque.push_front(num);
        }
        else if (str_command == "push_back") {
            int num;
            cin >> num;
            deque.push_back(num);
        }
        else if (str_command == "pop_front") {
            if (!deque.empty()) {
                cout << deque.front() << "\n";
                deque.pop_front();
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (str_command == "pop_back") {
            if (!deque.empty()) {
                cout << deque.back() << "\n";
                deque.pop_back();
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (str_command == "size") {
            cout << deque.size() << "\n";
        }
        else if (str_command == "empty") {
            if (deque.empty()) {
                cout << 1 << "\n";
            }
            else {
                cout << 0 << "\n";
            }
        }
        else if (str_command == "front") {
            if (!deque.empty()) {
                cout << deque.front() << "\n";
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (str_command == "back") {
            if (!deque.empty()) {
                cout << deque.back() << "\n";
            }
            else {
                cout << -1 << "\n";
            }
        }
    }

    return 0;
}