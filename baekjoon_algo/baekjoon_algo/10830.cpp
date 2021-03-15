#include <iostream>

using namespace std;

long long matrix[6][6], result[6][6], matrixTemp[6][6], n, expo;

void func_mul_matrix(long long matrixA[6][6], long long matrixB[6][6])
{
    //����� ����
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
        {
            matrixTemp[i][j] = 0;
            for (int k = 1; k <= n; k++)
            {
                matrixTemp[i][j] += matrixA[i][k] * matrixB[k][j];
            }
            matrixTemp[i][j] %= 1000;
        }
    //������� matrixA�� �ֱ�
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            matrixA[i][j] = matrixTemp[i][j];

}
int main() {
    
    cin >> n >> expo;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> matrix[i][j];

        }
        result[i][i] = 1;
    }

    //������ �ٽ�
    while (expo > 0) 
    {
        if (expo % 2 == 1)//���� Ȧ��
        {
            func_mul_matrix(result, matrix);
        }
        func_mul_matrix(matrix, matrix);
        expo /= 2;
    }

    //��� ���
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            cout << result[i][j] << ' ';
        cout << '\n';
    }
}