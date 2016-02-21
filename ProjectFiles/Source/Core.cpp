#include <iostream>
#include <vector>
#include "../Headers/Node.h"
using namespace std;

#include "../Headers/LinuxPrePros.h"
#include "../Headers/WinPrePros.h"





//prototypes
void Commands(string cinresult);
void GetCommand();

//variables
vector<Node> Nodes;
string cinresult;
bool EndLoop = false;




int main()
{
	
	/*while (!EndLoop)
	{
		getline(cin, cinresult);
		Commands(cinresult);
	}*/
        
        char* test = "../../../../../Python/Eyesight/Primitive_Eyesight.py";
        char* test2 = "../../../../../Python/Hearing/AmplitudeTest.py";
	cout << PrintFullPath(test) << endl;
	cout << PrintFullPath(test2) << endl;






#ifdef _WIN32
	system("PAUSE");
#endif

	return 0;
}



void Commands(string cinresult)
{
	if (cinresult == "End" || cinresult == "end")
	{
		EndLoop = true;
	}
	else if (cinresult == "Create Node" || cinresult == "create node")
	{
		string nodename;
		cout << "Name of Node: ";
		cin >> nodename;
		Node temp(nodename);
		Nodes.push_back(temp);
		cout << "List of node names: ";
		for (int i = 0; i < Nodes.size(); i++)
		{
			cout << Nodes[i].getName() << ", ";
		}
		cout << endl;
		
	}
}


