#include <iostream>
#include <string>
#include <locale>
#include <fstream>

using namespace std;

void MakeClass(string name);

void main()
{
	string ClassName;
	bool isInMemory = false;

	cout << "What's the class?: ";
	cin >> ClassName;

	ifstream file;
	file.open("MemList.txt");
	while (!file.eof())
	{
		string temp;
		getline(file, temp);
		std::size_t found = temp.find(ClassName);
		if (found != std::string::npos)
		{
			cout << "Already in memory" << endl;
			isInMemory = true;
		}	
	}

	if (!isInMemory)
	{
		MakeClass(ClassName);
	}


	system("PAUSE");

}

void MakeClass(string name)
{
	ofstream file;

	string UpperName;
	locale loc;
	for (int i = 0; i < name.length(); i++)
	{
		UpperName += toupper(name[i], loc);
	}
	
	string temp = name + ".h";

	file.open(temp);	
	if (file.is_open())
	{
		// Creates the bare bones class structure for "Name" in header file
		file << "#ifndef " << UpperName << "_H" << endl;
		file << "define " << UpperName << "_H" << endl;
		file << endl << endl;
		file << "class " << name << endl << "{" << endl;
		file << "public:" << endl << endl << "private:" << endl << endl << "};" << endl << endl << "#endif" << endl;
		file.close();
	}

	temp = name + ".cpp";
	file.open(temp);
	if (file.is_open())
	{
		// Creates the bare bones class structure for "Name" in cpp file
		file << "#include " << name + ".h" << endl;
		file << endl << endl << "//Constructors" << endl;
		file << name << "::" << name << "() {}" << endl << endl;
		file << "//Inspectors" << endl << endl << "//Mutators" << endl << endl << "//Facilitators" << endl;
		file.close();
	}
	
	file.open("MemList.txt",ios::ate | ios::app);
	if (file.is_open())
	{
		file << name << endl;
	}
	cout << "Class made!" << endl;
}