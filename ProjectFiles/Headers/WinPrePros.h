#ifndef WINPREPROS_H
#define WINPREPROS_H

#ifdef _WIN32
#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>


string PrintFullPath(char * partialPath)
{
	char full[_MAX_PATH];
	if (_fullpath(full, partialPath, _MAX_PATH) == NULL)
	{
		cout << "invalid!" << endl;
		return "nope";
	}
	return full;
}



#endif //_WIN32
#endif //WINPREPROS_H