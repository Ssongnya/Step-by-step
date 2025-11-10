#include <iostream>
using namespace std;


int main(void)
{
	int i;
	cin >> i;

	for (int num = 1; num < (i+1); num++)
	{
		int a;
		int b;
		cin >> a >> b;
		int result = a + b;
		cout << "Case " << "#" << num << ": " << result << "\n";
	}
}