#include<iostream>

using namespace std;
long long int a;
long long int b;
int c;

long long int APowerB(long long int a, long long int b) {
	if (b == 0) // °ÅµìÁ¦°öÀÌ 0ÀÏ¶§´Â ¹«Á¶°Ç 1
		return 1;
	else if (b == 1)  // °ÅµìÁ¦°öÀÌ 1ÀÏ¶§´Â °è¼ÓÇØ¼­ a ¹ÝÈ¯
		return a;
	if (b % 2 > 0)   // °ÅµìÁ¦°öÀ» 2·Î ³ª´« ³ª¸ÓÁö.
		return APowerB(a, b - 1) * a;
	long long int binarySquaring = APowerB(a, b / 2);
	binarySquaring %= c;

	return (binarySquaring * binarySquaring) % c;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> a >> b >> c;

	cout << APowerB(a, b) % c;


	return 0;
}