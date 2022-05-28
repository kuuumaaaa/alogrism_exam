

def input_data():
    """
    Input data
    """
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    return n, a, k

def partical_sum(n, a, k):
    """
    Partical sum
    """
    sum_ = 0
    for i in range(n):
        sum_ += a[i]
        if sum_ >= k:
            return i + 1
    return n + 1

if __name__ == '__main__':
    n, a, k = input_data()
    print(partical_sum(n, a, k))