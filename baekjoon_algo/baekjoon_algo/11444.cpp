#include<iostream>
#include<vector>
using namespace std;

typedef long long LL;
typedef vector<vector<LL>> matrix;
LL p = 1000000007;
LL n;

matrix operator * (matrix& a, matrix& b)
{
	matrix temp(2, vector<LL>(2));

	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < 2; k++)
				temp[i][j] += a[i][k] * b[k][j];

			temp[i][j] %= p;
		}
	return temp;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;

	matrix result = { {1,0}, {0,1} };  // 이차단위행렬 E
	matrix poMat = { {1,1}, {1,0} };  //거듭제곱할 행렬

	while (n > 0)
	{
		if (n % 2 == 1)
			result = result * poMat;
		poMat = poMat * poMat;
		n /= 2;
	}

	cout << result[0][1] << '\n';
}

