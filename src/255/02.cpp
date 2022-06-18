#include <iostream>
#include <vector> //可変長配列
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    int n , k;
    cin>>n>>k;
    vector<int> vec(k);
    for(int i=0;i<k;i++){
        cin >> vec[i];
    }
    int a[n][2];
    for (int i=0;i<n;i++){
            cin >> a[i][0];
            cin >> a[i][1];
    }
    long tmp1,tmp2,tmp3;
    long ans[k];
    long ans1[n];
    for (int i=0;i<n;i++){
        for(int j=0;j<k;j++){
            tmp1 = (a[i][0] - a[vec[j]-1][0]);
            tmp2 = (a[i][1] - a[vec[j]-1][1]);
            tmp3 = tmp1*tmp1 + tmp2*tmp2;
            ans[j] = pow(tmp3,0.5);
            cout << tmp3 <<endl;
            cout << ans[j] <<endl;
        }
        long *min= std::min_element(ans, ans+k);
        ans1[i] = *min;
    }
    long *max = std::max_element(ans1, ans1+n);
    cout<< *max <<endl;
}