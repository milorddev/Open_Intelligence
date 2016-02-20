#include <iostream>
#include <vector>
#include "../Headers/Node.h"
using namespace std;

#include "../Headers/LinuxPrePros.h"
#include "../Headers/WinPrePros.h"





//prototypes
void Commands(string cinresult);

//variables
Node node("node");
string cinresult;
bool EndLoop = false;



int main()
{
	while (!EndLoop)
	{
		cin >> cinresult;
		Commands(cinresult);
		

	}
	
	







#ifdef _WIN32
	system("PAUSE");
#endif

	return 0;
}



void Commands(string cinresult)
{
	if (cinresult == "End")
	{
		EndLoop = true;
	}
}


