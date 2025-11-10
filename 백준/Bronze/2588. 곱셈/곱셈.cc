#include <iostream>
using namespace std;

int times(int a, int b)
{
	return a * b;
}



int main(void)
{
	int a;
	int b;
	
	cin >> a;
	cin >> b;

	int result;
	result = a * b;

	while (b > 0)
	{
		int now = b % 10;
		b = b / 10;
		cout << a * now<<'\n';
	}

	cout << result<<'\n';
}