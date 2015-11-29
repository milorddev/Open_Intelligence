#include <iostream>
#include "../MemLayer/AddClasses.h"
#include <string>

using namespace std;

void CreateClass();



int main()
{
	string classname;
	cout << "Check if Exists: ";
	cin >> classname;
	string fullname = classname + "::" + classname;

	__if_exists(Xam::Xam)
	{
		cout << "This exists!" << endl;
	}


	CreateClass();

	system("PAUSE");
	return 0;
}