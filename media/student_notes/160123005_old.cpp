#include<iostream>
#include<cstdlib>
using namespace std;
						// math functions 
double abs(double a){
	if(a>0)return a;
	return -1*a;
}
double sqrt(double n){
	double low=0,high=n;
	double mid=(low+high)/2;
	int i=500;
	while(i--){
		if(abs(mid*mid-n)<=0.00001){
			break;
		}
		else if(mid*mid-n>0.00001){
			high=mid;
			mid=(low+high)/2;
		}
		else if(n-mid*mid>0.00001){
			low=mid;
			mid=(low+high)/2;
		}
	}
	return mid;
}
double minimum(double a,double b){
	if(a<b)return a;
	return b;
}
						// start class point
class Point
{
	double x,y;
public:
	void set_x(double);
	void set_y(double);
	double get_x();
	double get_y();
	double distance(Point,Point);
};
							// functions of class point
void Point:: set_x(double a){
	x=a;
}
void Point:: set_y(double b){
	y=b;
}
double Point:: get_x(){
	return x;
}
double Point:: get_y(){
	return y;
}
double Point:: distance(Point a, Point b){
	double x1=a.get_x(),x2=b.get_x();
	double y1=a.get_y(),y2=b.get_y();
	return (double)sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

							// end class point

							// start class plane
class Plane
{
	Point *cords;
	double x1,x2,y1,y2;
public:
	Plane(int); //constructor
	Point get_point(int );
	void set_point(int ,double ,double);
	int partition_x(Plane ,int ,int);
	void sort_x(Plane ,int ,int);
	int partition_y(Plane ,int ,int);
	void sort_y(Plane ,int ,int);
	double Closest(Plane ,Plane ,int  ,int  ,int );
	double strip_minimum_dist(Plane ,int ,int );
};
Plane::Plane(int n){
	srand((unsigned)time(0));
	x1=0;x2=0;y1=0;y2=0;
	cords=new Point[n];
	for(int i=0;i<n;i++){
		cords[i].set_x(((double)(rand()%100000)/100000.0)*100.0);
		cords[i].set_y(((double)(rand()%100000)/100000.0)*100.0);
	}
}
							// functions of class plane
Point Plane::get_point(int i){
	return cords[i];
}
void Plane::set_point(int i,double a,double b){
	cords[i].set_x(a);
	cords[i].set_y(b);
}
int Plane::partition_x(Plane cart,int l,int h){
	double p=cart.get_point(l).get_x();
	int k=l;
	for(int i=l+1;i<h+1;i++){
		if(cart.get_point(i).get_x()<p){
			double x=cart.get_point(i).get_x(),y=get_point(i).get_y();
			cart.set_point(i,cart.get_point(k+1).get_x(),cart.get_point(k+1).get_y());
			cart.set_point(k+1,x,y);
			k++;
		}
	}
	double x=cart.get_point(l).get_x(),y=get_point(l).get_y();
	cart.set_point(l,cart.get_point(k).get_x(),cart.get_point(k).get_y());
	cart.set_point(k,x,y);
	return k;
}
void Plane::sort_x(Plane cart,int l,int h){
	if(l<h){
		int p=cart.partition_x(cart,l,h);
		cart.sort_x(cart,l,p-1);
		cart.sort_x(cart,p+1,h);
	}
}
int Plane::partition_y(Plane cart,int l,int h){
	double p=cart.get_point(l).get_y();
	int k=l;
	for(int i=l+1;i<h+1;i++){
		if(cart.get_point(i).get_y()<p){
			double x=cart.get_point(i).get_x(),y=get_point(i).get_y();
			cart.set_point(i,cart.get_point(k+1).get_x(),cart.get_point(k+1).get_y());
			cart.set_point(k+1,x,y);
			k++;
		}
	}
	double x=cart.get_point(l).get_x(),y=get_point(l).get_y();
	cart.set_point(l,cart.get_point(k).get_x(),cart.get_point(k).get_y());
	cart.set_point(k,x,y);
	return k;
}
void Plane::sort_y(Plane cart,int l,int h){
	if(l<h){
		int p=cart.partition_y(cart,l,h);
		cart.sort_y(cart,l,p-1);
		cart.sort_y(cart,p+1,h);
	}
}
double Plane::strip_minimum_dist(Plane strip,int n,int d){
	double minimum=100000.0;
	for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n && (strip.get_point(j).get_y()-strip.get_point(i).get_y()<d);j++){
			double dist=strip.get_point(i).distance(strip.get_point(i),strip.get_point(j));			
			if(dist<minimum){
				minimum=dist;
			}
		}
	}
	return minimum;
}
double Plane::Closest(Plane cartesion_xsorted ,Plane cartesion_ysorted ,int l ,int h ,int n){
	if(h-l<3){
		double minimum_distance=100000.0;
		for(int i=l;i<h;i++){
			for(int j=i+1;j<=h;j++){
				double dist=cartesion_xsorted.get_point(i).distance(cartesion_xsorted.get_point(i),cartesion_xsorted.get_point(j));
				if(minimum_distance>dist){
					minimum_distance=dist;
				}
			}
		}
		return minimum_distance;
	}
	else{
		int mid=(l+h)/2;
		Plane cartesion_left_ysorted(mid-l+1);
		Plane cartesion_right_ysorted(h-mid);
		int index1=0,index2=0;
		for(int i=l;i<=h;i++){
			double x=cartesion_xsorted.get_point(i).get_x(),y=cartesion_xsorted.get_point(i).get_y();
			if(x<=cartesion_xsorted.get_point(mid).get_x()){
				cartesion_left_ysorted.set_point(index1,x,y);
				index1++;
			}
			if(x>cartesion_xsorted.get_point(mid).get_x()){
				cartesion_right_ysorted.set_point(index2,x,y);
				index2++;
			}
		}
		double d1=Closest(cartesion_xsorted,cartesion_left_ysorted,l,mid,n);
		double d2=Closest(cartesion_xsorted,cartesion_right_ysorted,mid+1,h,n);
		double d=minimum(d1,d2);
		double d3=100000.0;
		Plane strip(n);		
		int index=0;
		for(int i=l;i<=h;i++){
			double x=cartesion_ysorted.get_point(i-l).get_x();
			double y=cartesion_ysorted.get_point(i-l).get_y();
			if(x<=cartesion_xsorted.get_point(mid).get_x()+d || x>=cartesion_xsorted.get_point(mid).get_x()-d){
				strip.set_point(index,x,y);
				index++;
			}			
		}
		d3=strip.strip_minimum_dist(strip,index,d);
		return minimum(d,d3);
	}
}

							// end class plane

int main(){
	cout<<"Enter Number of Random Points You want: ";
	int n;cin>>n;
	Plane cartesion(n);
	Plane cartesion_xsorted(n);
	Plane cartesion_ysorted(n);
	for(int i=0;i<n;i++){
		double x=cartesion.get_point(i).get_x(),y=cartesion.get_point(i).get_y();
		cartesion_xsorted.set_point(i,x,y);
		cartesion_ysorted.set_point(i,x,y);
	}
	cartesion_xsorted.sort_x(cartesion_xsorted,0,n-1);
	cartesion_ysorted.sort_y(cartesion_ysorted,0,n-1);
	cout<<"Minimum distance between the closest pair is: "<<cartesion.Closest(cartesion_xsorted,cartesion_ysorted,0,n-1,n)<<"\n";
	/*for(int i=0;i<n;i++){
		cout<<cartesion.get_point(i).get_x()<<" "<<cartesion.get_point(i).get_y()<<"\n";
	}*/
	return 0;
}
