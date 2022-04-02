#include <stdio.h>

int SumFirstN(int n)
{
    return n * (n + 1) >> 1;
}

int BoxIndex(int row, int col)
{
    row--; col--;
    int mtx[3][2] = { {1, 3}, {2, 7}, {4, 5} };

    if (row < 3 && col < 2)
        return mtx[row][col];

    if (row == 0)
        return SumFirstN(col + 1);
    
    int diff0 = 4;
    int diff1[2] = { 8, 10 };
    for (int i = 3; i <= row; i++)
    {

        for (int j = 1; j < 3; j++)
        {
            mtx[j - 1][0] = mtx[j][0];
            mtx[j - 1][1] = mtx[j][1];
        }
        const int odd = i & 1;
        mtx[2][0] = mtx[1][0] + diff0;
        diff0 += 2 * (1 - odd);
        mtx[2][1] = mtx[0][1] + diff1[odd];
        diff1[odd] += 4;
    }
    if (col < 2)
        return mtx[2][col];
    
    int offset = 4 + ((row - 3 >> 1) << 2);
    int diff2[2] = { 7, 9 };
    int mtxRow[3] = { 0, mtx[2][0], mtx[2][1] };
    for (int i = 2; i <= col; i++)
    {
        mtxRow[0] = mtxRow[1];
        mtxRow[1] = mtxRow[2];
        mtxRow[2] = mtxRow[0] + diff2[i & 1] + offset;
        diff2[i & 1] += 4;
    }
    return mtxRow[2];
}

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);
    printf("%d\n", BoxIndex(m, n));
}
