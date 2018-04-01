#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n,copy,k;cin>>n>>k;
    copy=n;
    int index=0,count=0;
    int power[100000]={0};
    while (copy)
    {
        power[64-index]=copy&1;
        count+=copy&1;
        copy >>= 1;
        index++;
    }
    if(k<count){
        cout<<"NO";   
    }
    else{
        int pow_index=0;
        while(count!=k){
            if(power[pow_index]>0){
                if(power[pow_index]>=k-count){
                    power[pow_index]-=k-count;
                    power[pow_index+1]+=2*(k-count);
                    count+=k-count;
                }
                else{
                    power[pow_index+1]+=2*power[pow_index];
                    count+=power[pow_index];
                    power[pow_index]=0;
                }
            }
            pow_index++;
        }
        cout<<"YES"<<"\n";
        for(int i=0;i<100000;i++){
            while(power[i]--){
                cout<<64-i<<" ";
            }
        }
    }
    return 0;
}
