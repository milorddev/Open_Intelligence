#include <thread>
#include <memory>
#include <fstream>
#include <string>
#include <iostream>

using namespace std;

bool TurnOnVisuals = false;

void VisualStream(bool EndInput)
{
	ifstream VisualFile;
	VisualFile.open("EyePrim_output.txt");
	string visualline;

	if (VisualFile.is_open())
	{
		while (!EndInput)
		{
			if (TurnOnVisuals)
				cout << "Visual Input" << endl;
			if (VisualFile.eof())
			{
				VisualFile.clear();
				VisualFile.seekg(0, ios::beg);
			}
		}
		VisualFile.close();
	}
	else
	{
		cout << "File not found" << endl;
	}
}

void AudioStream(bool EndInput)
{
	ifstream SoundFile;
	SoundFile.open("Amp_output.txt");
	string soundline;

	if (SoundFile.is_open())
	{
		while (!EndInput)
		{
			getline(SoundFile, soundline);
			if (TurnOnVisuals)
				cout << "Sound Input: " << soundline << endl;
			if (SoundFile.eof())
			{
				SoundFile.clear();
				SoundFile.seekg(0, ios::beg);
			}
		}
		SoundFile.close();
	}
	else
	{
		cout << "File not found" << endl;
	}

}



void StreamInputData(bool EndInput)
{
	thread Thread1(AudioStream,EndInput);
	thread Thread2(VisualStream,EndInput);



	Thread1.join();
	Thread2.join();

}










