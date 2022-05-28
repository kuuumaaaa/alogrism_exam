def main():
    h,w = map(int,input().split())
    s = [str(input()) for _ in range(h)]
    val_x = []
    val_y = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                val_x.append(i)
                val_y.append(j)
    val = abs(val_x[0] - val_x[1]) + abs(val_y[0] - val_y[1])
    print(val)
    return 
        
 
if __name__ == '__main__':
    main()