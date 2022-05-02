
def input_data():
    """
    Input data
    """
    n, m = map(int,input().split())
    field = [list(input()) for _ in range(n)] 
    return n, m, field

def dfs(x:int, y:int):
    """
    Cont Lake
    """
    field[x][y] = '.'
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and field[nx][ny] == 'W':
            dfs(nx, ny)
    return

if __name__ == '__main__':
    n, m, field = input_data()
    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 'W':
                dfs(i, j)
                count += 1
    print(count)

