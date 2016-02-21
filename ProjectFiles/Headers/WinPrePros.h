#ifndef WINPREPROS_H
#define WINPREPROS_H

#ifdef _WIN32
#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>


void PrintFullPath(char * partialPath)
{
	char full[_MAX_PATH];
	if (_fullpath(full, partialPath, _MAX_PATH) != NULL)
		printf("Full path is: %s\n", full);
	else
		printf("Invalid path\n");
}



#endif //_WIN32
#endif //WINPREPROS_H