#include <iostream>
using namespace std;

int Times(int a, int b)
{
	return a * b;
}

int Adder(int a, int b)
{
	return a + b;
}

int Minus(int a, int b)
{
	return a - b;
}

int mod(int a, int b)
{
	return a % b;
}

int R(int a, int b)
{
	return a/b;
}


int main(void)
{
	int a;
	int b;

	cin >> a >> b;
	cout << Adder(a, b) << '\n';
	cout << Minus(a, b) << '\n';
	cout << Times(a, b)<<'\n';
	cout << R(a, b) << '\n';
	cout << mod(a, b) << '\n';
}