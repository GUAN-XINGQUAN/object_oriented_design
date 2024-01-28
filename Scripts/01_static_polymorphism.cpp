#include <iostream>

using namespace std;

// Base class
class Animal {
public:
	Animal() {
		this->name = "";
	}
	Animal(string name) {
		this->name = name;
	}
	virtual void generateSound() {
		cout << "This animal generates the sound like TBD" << endl;
	}
private:
	string name;
};

// inherited class
class Dog : public Animal {
public:
	Dog() : Animal (){}
	Dog(string name, string sound) : Animal(name) {
		this->sound = sound;
	}
	void generateSound() {
		cout << "This dog generates the sound like " << this->sound << endl;
	}
private:
	string sound;
};


int main() {
	Animal animal("Cookie");
	Dog dog("Cookie", "wang wang");

	animal.generateSound();
	dog.generateSound();
}