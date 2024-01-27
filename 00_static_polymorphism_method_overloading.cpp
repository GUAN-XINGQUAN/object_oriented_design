#include <iostream>

// Method overloading
using namespace std;
class Sum {
public:
    int addition(int a, int b) {
        return a + b;
    }

    int addition(int a, int b, int c) {
        return a + b + c;
    }
};

int main(void) {
    Sum sum;
    cout << sum.addition(14, 35) << endl;
    cout << sum.addition(31, 34, 43) << endl;
}