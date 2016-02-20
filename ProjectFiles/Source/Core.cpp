#include <iostream>
using namespace std;


int main()
{
	cout << "Hello world" << endl;
	
#ifdef _WIN32
	system("PAUSE");
#endif

	return 0;
}