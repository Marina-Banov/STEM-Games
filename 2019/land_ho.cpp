#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>

#include <vector>
#include <queue>

int BFS4(bool* mtx, bool* visited, int m, int n, int i, int j)
{
    int dx4[4] = { 1, 0, -1, 0 };
    int dy4[4] = { 0, 1, 0, -1 };

    int land = 0;

    std::queue<std::pair<int, int>> coords;
    coords.push({ i, j });
    while (!coords.empty())
    {
        auto [y, x] = coords.front();
        coords.pop();
        bool& vis = visited[y * n + x];
        if (vis)
            continue;
        vis = true;
        land = 1;
        for (int i = 0; i < 4; i++)
        {
            std::pair<int, int> newCoord = { y + dy4[i], x + dx4[i] };
            if ((unsigned)newCoord.first >= m || (unsigned)newCoord.second >= n)
                continue;
            if (!mtx[newCoord.first * n + newCoord.second])
                continue;
            coords.push(newCoord);
        }
    }
    return land;
}


int BFS8(bool* mtx, bool* visited, int m, int n, int i, int j)
{
    int dx8[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };
    int dy8[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };

    int sea = 0;

    std::queue<std::pair<int, int>> coords;
    coords.push({ i, j });
    while (!coords.empty())
    {
        auto [y, x] = coords.front();
        coords.pop();
        bool& vis = visited[y * n + x];
        if (vis)
            continue;
        vis = true;
        sea = 1;
        for (int i = 0; i < 8; i++)
        {
            std::pair<int, int> newCoord = { y + dy8[i], x + dx8[i] };
            if ((unsigned)newCoord.first >= m || (unsigned)newCoord.second >= n)
                continue;
            if (mtx[newCoord.first * n + newCoord.second])
                continue;
            coords.push(newCoord);
        }
    }
    return sea;
}

int main()
{
    int m, n, h;
    scanf("%d %d %d", &m, &n, &h);

    bool *mtx = new bool[m * n];
    bool *visited = new bool[m * n];
    for (int i = 0; i < m; i++)
    {
        int tmp;
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &tmp);
            mtx[i * n + j] = tmp > h;
        }
    }

    memset(visited, 0, m * n);
    int nLand = 0, nSea = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (mtx[i * n + j])
                nLand += BFS4(mtx, visited, m, n, i, j);
        }
    }
    memset(visited, 0, m * n);

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!mtx[i * n + j])
                nSea += BFS8(mtx, visited, m, n, i, j);
        }
    }
    printf("%d %d", nLand, nSea);
    return 0;
}
