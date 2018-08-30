#include<iostream>
#include<cstdlib>
#include<math.h>
using namespace std;
class point
{
	double x,y;
public:
	 void set_x(double a){
	 	x=a;
	 }
	 void set_y(double b){
	 	y=b;
	 }
	 double get_x(){
	 	return x;
	 }
	 double get_y(){
	 	return y;
	 }
	 void pri(){
	 	cout<<x<<" "<<y;
	 }
};
double minimum(double a,double b){
	if(a<b)return a;
	else return b;
}
int partition(point a[],int l,int h,int dire,int n){			//direction for sorting along x or y
	int p;
	int k=l;
	if(dire==0){
		p=a[l].get_x();
		for(int i=l+1;i<h+1;i++){
			if(a[i].get_x()<p){
				swap(a[k+1],a[i]);
				k++;
			}
		}
		swap(a[k],a[l]);
		return k;
	}
	else{
		p=a[l].get_y();
		for(int i=l+1;i<h+1;i++){
			if(a[i].get_y()<p){
				swap(a[k+1],a[i]);
				k++;
			}
		}
		swap(a[k],a[l]);
		return k;
	}
}
void quickSort(point a[],int l, int h, int dire, int n){
	if(l<h){
		int p=partition(a,l,h,dire,n);
		quickSort(a,l,p-1,dire,n);
		quickSort(a,p+1,h,dire,n);
	}
}
double closest(point a[],int l, int h,int n){
	if(h<=l){
		return 1000000.0;//as single point so for neglecting it take closet pair distance as infinite
	}
	else if(h-l==1){
		double x1=a[l].get_x(),x2=a[h].get_x();
		double y1=a[l].get_y(),y2=a[h].get_y();
		return (double)sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
	}
	else if(1<h-l){
		int mid=(l+h)/2;
		double d1=closest(a,l,mid,n);
		double d2=closest(a,mid+1,h,n);
		double d=minimum(d1,d2);
		int strip_l=mid,strip_h=mid;
		for(int i=l;i<=mid;i++){
			if(a[i].get_x()>=a[mid].get_x()-d){
				strip_l=i;
				break;
			}
		}
		for(int i=h;i>=mid;i--){
			if(a[i].get_x()<=a[mid].get_x()+d){
				strip_h=i;
				break;
			}
		}
		point strip[strip_h-strip_l+1],strip2[strip_h-strip_l+1];
		//cout<<"strip_l "<<strip_l<<" "<<"strip_h"<<strip_h<<"\n";
		for(int i=strip_l;i<=strip_h;i++){
			strip[i-strip_l].set_x(a[i].get_x());
			strip[i-strip_l].set_y(a[i].get_y());
			strip2[i-strip_l].set_x(a[i].get_y());
			strip2[i-strip_l].set_y(a[i].get_x());
		}	
		//quickSort(strip,0,strip_h-strip_l,1,strip_h-strip_l);
		// double d3=100000.0;
		// for(int i=0;i<strip_h-strip_l;i++){
		// 	for(int j=i+1;j<strip_h-strip_l+1;j++){
		// 		double x1=strip[i].get_x(),x2=strip[j].get_x();
		// 		double y1=strip[i].get_y(),y2=strip[j].get_y();
		// 		double dist=(double)sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
		// 		if(dist<d3)d3=dist;
		// 	}
		// }
		double d4=closest(strip2,0,strip_h-strip_l-1,n);
		//cout<<"d1 "<<d1<<" "<<"d2 "<<d2<<" "<<"d3 "<<d3<<"\n";
		return minimum(d4,d);
		//return 1;
	}
}
int main(){
	srand((unsigned)time(0));
	int n;cin>>n;
	point cord[n];
	for(int i=0;i<n;i++){
		double x=rand()%100;
		double y=rand()%100;
		//cin>>x>>y;
		cord[i].set_x(x);cord[i].set_y(y);
	}
	//for(int i=0;i<n;i++)cout<<cord[i].get_x()<<" "<<cord[i].get_y()<<"\n";
	quickSort(cord,0,n-1,0,n);  //fourth argument for direction 0 for x direction
	cout<<closest(cord,0,n-1,n)<<"\n";
	double raw=100000.0;
	for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n;j++){
			double x1=cord[i].get_x(),x2=cord[j].get_x();
			double y1=cord[i].get_y(),y2=cord[j].get_y();
			double dist=(double)sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
			//cout<<"dist "<<dist<<"\n";
			if(dist<raw){
				raw=dist;
				//cout<<"minim"<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<"\n";
				cout<<"dist "<<dist<<"\n";
			}
		}
	}
	cout<<"raw"<<raw;
	//for(int i=0;i<n;i++)cout<<cord[i].get_x()<<" "<<cord[i].get_y()<<"\n";
	return 0;
}