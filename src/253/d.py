def main():
    n, a, b = map(int,input().split())
    ax = n / a
    bx = n / b
    cx = n / (a * b)
    print(n-ax-bx+cx)
    return 
        
 
if __name__ == '__main__':
    main()