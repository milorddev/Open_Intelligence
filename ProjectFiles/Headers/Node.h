#ifndef NODE_H
#define NODE_H

#include <vector>
#include <string>

using namespace std;


struct Node
{
	vector<Node*> NodeList;
	string NodeName;
	bool isSearched;
};


/*
class Node
{


public:
	//construtor
	Node(string Title);


	//inspector

	string getName();

	int get
	//facilitator


private:
	vector<Node*> NodeList;
	string NodeName;
	bool isSearched;

};

*/



#endif //NODE_H