#include<iostream>

using namespace std;

class ComplexNumber {
public:
	// Constructor
	ComplexNumber(int r = 0, int i = 0) { real = r; imaginary = i; }

	// Overloading function for + operator
	ComplexNumber operator + (ComplexNumber const& c) {
		ComplexNumber addResult;
		addResult.real = real + c.real;
		addResult.imaginary = imaginary + c.imaginary;
		return addResult;
	}

	// display results
	void display() {
		cout << "( " << real << " + " << imaginary << " i )" << '\n';
	}
private:
	int real, imaginary;
};

int main() {
	ComplexNumber c1(11, 5), c2(2, 6);
	ComplexNumber c3 = c1 + c2;
	c3.display();
}
