#include <iostream>

#define MAX 100

using namespace std;

int matrixA[MAX][MAX], matrixB[MAX][MAX];
int result[MAX][MAX];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N, M, K;

    cin >> N >> M;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> matrixA[i][j];

    cin >> M >> K;
    for (int i = 0; i < M; i++)
        for (int j = 0; j < K; j++)
            cin >> matrixB[i][j];

    for (int i = 0; i < N; i++)
        for (int j = 0; j < K; j++)
            for (int k = 0; k < M; k++)
                result[i][j] += (matrixA[i][k] * matrixB[k][j]);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < K; j++)
            cout << result[i][j] << " ";
        cout << "\n";
    }

    return 0;
}