﻿#include <stdio.h>

int ArithSum(int n)
{
	return n * (n + 1) >> 1;
}

int main()
{
	int row, col;
	scanf("%d %d", &row, &col);

	int mtx[3][2] = { {1, 3}, {2, 7}, {4, 5} };
	row--;
	col--;

	if (row < 3 && col < 2)
	{
		return mtx[row][col];
	}

	if (row == 0)
	{
		printf("%d\n", ArithSum(col + 1));
		return 0;
	}
	else
	{
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
		{
			printf("%d\n", mtx[2][col]);
			return 0;
		}
		int offset = 4 + ((row - 2 >> 1) << 2);

		int diff2[2] = { 7, 9 };
		int mtxRow[3] = { 0, mtx[2][0], mtx[2][1] };
		for (int i = 2; i <= col; i++)
		{
			mtxRow[0] = mtxRow[1];
			mtxRow[1] = mtxRow[2];
			mtxRow[2] = mtxRow[0] + diff2[i & 1] + offset;
			diff2[i & 1] += 4;
		}

		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 2; j++)
			{
				printf("%d ", mtx[i][j]);
			}
			putchar('\n');
		}
		printf("RES: %d\n", mtxRow[2]);
	}

	return 0;
}