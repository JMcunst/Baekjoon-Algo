#include<iostream>

using namespace std;

typedef long long ll;
const ll p = 1000000007;

ll divconqs(ll a, ll b)
{
    ll r = 1;
    while (b > 0) {
        if (b % 2) {
            r *= a;
            r %= p;
        }
        a *= a;
        a %= p;
        b /= 2;
    }
    return r;
}

ll bino(ll n, ll k)
{
    ll nf = 1, a = 1;

    for (ll i = n; i >= 1; i--) {
        nf *= i;
        nf %= p;
    }
    for (ll i = k; i >= 1; i--) {
        a *= i;
        a %= p;
    }
    for (ll i = n - k; i >= 1; i--) {
        a *= i;
        a %= p;
    }

    return (nf * divconqs(a, p - 2)) % p;


}

int main(void)
{
    ll n, k;

    cin >> n >> k;
    cout << bino(n, k);

    return 0;
}