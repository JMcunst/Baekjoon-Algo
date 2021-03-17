#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

typedef long long LL;

vector<LL> h; // height vector

LL calLargestSquare(int left, int right) {
    
    
    if (left == right) return h[left]; // n = 1 or end Of Div&coq
    
    int mid = (left + right) / 2;
    
    LL ret = max(calLargestSquare(left, mid), calLargestSquare(mid + 1, right));
   
    LL lo = mid;       // Á© ³·Àº ³ôÀÌ¿¡¼­ ÁÂÃø (Á© ³·Àº ³ôÀÌ Æ÷ÇÔ)
    LL hi = mid + 1;   // Á© ³·Àº ³ôÀÌ¿¡¼­ ¿ìÃø
    LL height = min(h[lo], h[hi]);

    ret = max(ret, height * 2);
   
    while (left < lo || hi < right) {
        
        if (hi < right && (lo == left || h[lo - 1] < h[hi + 1])) {
            ++hi;
            height = min(height, h[hi]);
        }
        else {
            --lo;
            height = min(height, h[lo]);
        }
        
        ret = max(ret, height * (hi - lo + 1));
    }
    return ret;
}

int main() {
    int n, tempH;
    cin >> n;
    while (n) {
        h.clear();
        for (int i = 0; i < n; i++) {
            cin >> tempH;
            h.push_back(tempH);
        }
        cout << calLargestSquare(0, n - 1) << endl;
        cin >> n;
    }
}