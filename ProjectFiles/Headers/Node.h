#ifndef NODE_H
#define NODE_H

#include <vector>
#include <string>

using namespace std;


class Node
{


public:
	//construtor
	Node(string Title);


	//inspector


	//facilitator


private:
	vector<Node*> NodeList;
	string NodeName;
	bool isSearched;

};





#endif //NODE_H