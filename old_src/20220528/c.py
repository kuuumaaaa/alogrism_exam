def main():
    q = int(input())
    # s = [list(map(int, input().split())) for _ in range(q)]
    ans = {}
    # for _query in s:
    #     if _query[0] == 1:
    #         ans.append(_query[1])
    #     elif _query[0] == 2:
    #         ss = sum(x==_query[0] for x in ans)
    #         for _ in range(min(ss, _query[2])):
    #             ans.remove(_query[1])
    #     elif _query[0] == 3:
    #         ans_max = max(ans)
    #         ans_min = min(ans)
    #         print(ans_max - ans_min)
    for _ in range(q):
        _query = list(map(int, input().split()))
        if _query[1] not in ans:
            ans[_query[1]] = 0
        if _query[0] == 1:
            if  _query[1] not in ans:
                ans[_query[1]] = 1
            elif  _query[1] in ans:
                ans[_query[1]] += 1
        elif _query[0] == 2:
            ss = ans[_query[1]]
            ans[_query[1]] -= min(ss, _query[2])
            if ans[_query[1]] == 0:
                del ans[_query[1]]
        elif _query[0] == 3:
            ans_max = max(ans)
            ans_min = min(ans)
            print(ans_max - ans_min)
    return 
        
 
if __name__ == '__main__':
    main()