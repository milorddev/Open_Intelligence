#include <iostream>
#include <vector>
#include "../Headers/Node.h"
using namespace std;

#include "../Headers/LinuxPrePros.h"
#include "../Headers/WinPrePros.h"

#include <cstdio>
#include <memory>
#include <fstream>
#include <thread>

//prototypes
void Commands(string cinresult);
void GetCommand();
void StreamInputData(bool EndInput);

//variables
vector<Node> Nodes;
string cinresult;
bool EndLoop = false;




int main(int argc, char *argv[])
{

	//char* test = "../../../../../Python/Eyesight/Primitive_Eyesight.py";
	//char* test2 = "../../../../../Python/Hearing/AmplitudeTest.py";
	string PrimEye = PrintFullPath("../../../../../Python/Eyesight/Primitive_Eyesight.py");
	string AmpTest = PrintFullPath("../../../../../Python/Hearing/AmplitudeTest.py");

	cout << PrimEye << endl;
	cout << AmpTest << endl;


	//Open both Python Codes
#ifdef _WIN32
	string command1 = "start pythonw.exe ";
	command1 += "\"" + PrimEye + "\"";
	system(command1.c_str());

	string command2 = "start pythonw.exe ";
	command2 += "\"" + AmpTest + "\"";
	system(command2.c_str());
#endif


	thread StreamThread(StreamInputData, EndLoop);
	while (!EndLoop)
	{
		cout << flush;
		getline(cin, cinresult);
		Commands(cinresult);
	}
	StreamThread.join();




#ifdef _WIN32
	system("PAUSE");
#endif

	return 0;
}


void GetCommand()
{
	
	while (!EndLoop)
	{
		cin >> cinresult;
		Commands(cinresult);
	}
}


//not really necessary
void Commands(string cinresult)
{
	if (cinresult == "End" || cinresult == "end")
	{
		EndLoop = true;
	}
	else if (cinresult == "Create Node" || cinresult == "create node")
	{
		string nname;
		cout << "Name of Node: ";
		cin >> nname;
		Node temp;
		temp.NodeName = nname;
		Nodes.push_back(temp);
		cout << "List of node names: ";
		for (int i = 0; i < Nodes.size(); i++)
		{
			cout << Nodes[i].NodeName << ", ";
		}
		cout << endl;
	}
	/*else if (cinresult == "Add Link" || cinresult == "add link")
	{
		cout << "Start Node: ";
		cin >> BeginNode;
		cout << "End Node: ";
		cin >> EndNode;
	}*/
}

/*
void CSVMake()
{
	ofstream myfile;
	myfile.open("GUICSV.csv");

	

	for (int i = 0; i < Nodes.size(); i++)
	{
		string line = Nodes[i].NodeName;
		for (int j = 0; j < Nodes[i].NodeList.size(); j++)
		{
			line += "," + Nodes[i].NodeList[j]->NodeName;
		}

		cout << line << endl;
	}
}
*/