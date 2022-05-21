import collections
def main():
    n = int(input())
    A = list(map(int, input().split()))
    A_set = list(set(A))
    
    #リスト内包表記
    A = [str(input()) for _ in range(n)]
    tall = 0
    for i in range(1,10):
        a = []
        counter = 0
        t = 0
        for N in range(len(A)):
            xxx = A[N].index(str(i))
            a.append(xxx)
            if i in a:
                counter = xxx + 10
            else:
                counter = xxx
            if t < counter:
                t = counter
        if i == 1 or tall > t:
            tall = t
    print(tall)
    return 
        
 
if __name__ == '__main__':
    main()


