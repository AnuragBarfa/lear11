#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;cin>>x;
    int h,m;cin>>h>>m;
    long long ans=0;
    while(h!=7 && h!=17 && m!=7 && m!=17 && m!=27 && m!=37 && m!=47 && m!=57){
        if(m>=x){
            m=m-x;
            ans++;
        }
        else{
            if(h>0){
                h=h-1;m=m+60;
                m=m-x;
                ans++;
            }
            else{
                h=23;m=m+60;
                m=m-x;
                ans++;
            }
        }
    }
    cout<<ans;
	return 0;
}
