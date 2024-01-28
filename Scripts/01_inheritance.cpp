#include<iostream>
#include<string>

using namespace std;

// Base class
class Vehicle {
public:
	Vehicle() {
		this->name = "";
		this->model = "";
	}
	Vehicle(string name, string model) {
		this->name = name;
		this->model = model;
	}
	void getCarInfo() {
		cout << "The car is " << this->name << " and the model is " << this->model << endl;
	}
private:
	string name;
	string model;
};

// Single inheritance
class FuelCar : public Vehicle {
public:
	FuelCar() : Vehicle() {
		this->combustType = "";
	}
	FuelCar(string name, string model, string combustType) : Vehicle(name, model) {
		this->combustType = combustType;
	}
	void getFuelCar() {
		Vehicle::getCarInfo();
		cout << "The car has a combust type = " << this->combustType << endl;
	}
private:
	string combustType;
};

// Single inheritance
class ElectricCar : public Vehicle {
public:
	ElectricCar() : Vehicle() {
		this->batteryPower = "";
	}
	ElectricCar(string name, string model, string batteryPower) : Vehicle(name, model) {
		this->batteryPower = batteryPower;
	}
	void getElectricCar() {
		Vehicle::getCarInfo();
		cout << "The car has a battery = " << this->batteryPower << endl;
	}
private:
	string batteryPower;
};

// Hierarchical inheritance
class GasCar : public FuelCar {
public:
	GasCar() : FuelCar() {
		this->gasNumber = "#91";
	}
	GasCar(string name, string model, string combustType, string gasNumber) 
		: FuelCar(name, model, combustType) {
		this->gasNumber = gasNumber;
	}
	void getGasCar() {
		FuelCar::getFuelCar();
		cout << "This car needs gas = " << this->gasNumber << endl;
	}
private:
	string gasNumber;
};

// Multiple inheritance
class HybridCar : public GasCar, public ElectricCar {
public:
	HybridCar() : GasCar(), ElectricCar() {
		this->chargeType = "by engine";
	}
	HybridCar(string name, string model, string combustType, string gasNumber, 
		string batteryPower, string chargeType) : GasCar(name, model, combustType, gasNumber), 
		ElectricCar(name, model, batteryPower) {
		this->chargeType = "by engine";
	}
	void getHybridCar() {
		GasCar::getGasCar();
		ElectricCar::getElectricCar();
		cout << "This hybrid car is charged by " << this->chargeType << endl;
	}
private:
	string chargeType;
};

int main() {
	cout << "Base class: \n";
	Vehicle veh("2024 Camry", "SE");
	veh.getCarInfo();

	cout << "Single inheritance \n";
	FuelCar fue("2024 Camry", "SE", "ENGINE-2024");
	fue.getFuelCar();

	cout << "Single inheritance \n";
	ElectricCar ele("2024 Camry", "SE", "BATTERY-2024");
	ele.getElectricCar();

	cout << "Multi-level inheritance \n";
	GasCar gas("2024 Camry", "SE", "ENGINE-2024", "#93");
	gas.getGasCar();

	cout << "Multiple inheritance \n";
	HybridCar hyb("2024 Camry", "SE", "ENGINE-2024", "#93", "BATTERY-2024", "by AC power cord");
	hyb.getHybridCar();
}

