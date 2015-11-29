#include <Windows.h>
#include <iostream>
#include <string>

using namespace std;


void OpenClassCreator();
void PopulateHeader();


int main()
{
	PopulateHeader();
	for (int i = 0; i < 5; i++)
	{
		OpenClassCreator();
	}
	system("PAUSE");
	return 0;
}



void OpenClassCreator()
{
	//Open Class Creator
	LPSTR cmd = "C:/OpenIntelligence/Open_Intelligence/Visual_Studio_2013/Open_Intelligence/Debug/MemLayer.exe";
	STARTUPINFO info;
	PROCESS_INFORMATION processInfo;
	ZeroMemory(&info, sizeof(info));
	info.cb = sizeof(info);
	ZeroMemory(&processInfo, sizeof(processInfo));

	if (CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &info, &processInfo))
	{
		WaitForSingleObject(processInfo.hProcess, INFINITE);
		CloseHandle(processInfo.hProcess);
		CloseHandle(processInfo.hThread);
	}
	else
	{
		cout << "Process failed" << endl;
	}

}