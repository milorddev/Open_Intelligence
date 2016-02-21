#ifndef LINUXPREPROS_H
#define LINUXPREPROS_H

#ifdef __linux__ 



string PrintFullPath(char * partialPath)
{
	char *real_path = realpath(partialPath, NULL);
	return real_path;
}





#endif //__linux__
#endif //LINUXPREPROS_H