#include <iostream>
#include <string>
#include <fstream>
#include <locale>

using namespace std;


void PopulateHeader()
{
	ifstream readfile;
	readfile.open("MemList.txt"); // , ios::ate | ios::app);
	int InheritNumber;
	string Name;
	int ItemNumber;

	ofstream file;
	file.open("AddClasses.h");
	if (file.is_open())
	{
		file << "#ifndef ADDCLASSES_H" << endl;
		file << "#define ADDCLASSES_H" << endl;
		file << endl << endl;
		
		while (readfile >> ItemNumber >> Name)
		{
			file << "#include \"" << Name << ".h\"" << endl;
		}

		file << endl << "#endif" << endl;
	}
	

	readfile.close();
}