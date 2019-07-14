#include <iostream>
#include <cmath>
#include<ctime>
using namespace std;
bool prime = true;
bool factor = true;
int start_s=clock() ;
long long number = 345634567;
int main() {
    if (number % 2 == 0){
        factor = true;
        while (factor == true){
            if (number % 2 != 0){factor = false;
                break;}
            number /= 2;
            cout << 2 << endl;
        }
    }
    if (number % 3 == 0){
        factor = true;
        while (factor == true){
            if (number % 3 != 0){factor = false;
                break;}
            number /= 3;
            cout << 3 << endl;
        }
    }
    for (long long x = 5; x <= number; x += 2 ){
        bool prime = true;
        long long y = 3;
        while (y <= sqrt(x)) {
            if (x % y == 0){
                prime = false;
                break;}
            y += 2;
        }
        if (prime == true){
            factor = true;
            while (factor == true){
                if (number % x != 0){factor = false;
                    break;}
                number /= x;
                cout << x << endl;
            }

        }
    }
    int stop_s=clock();
    cout<<(stop_s-start_s)/double(CLOCKS_PER_SEC);
}
