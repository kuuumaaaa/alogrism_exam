#include <iostream>
#include <vector> //可変長配列
using namespace std;
int main()
{
    int r , c;
    cin>>r>>c;
    int a[2][2];
    for (int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            cin >> a[i][j];
        }
    }
    cout<<a[r-1][c-1]<<endl;
}