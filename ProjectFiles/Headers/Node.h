#ifndef NODE_H
#define NODE_H

#include <vector>
#include <string>
#include <string.h>

using namespace std;

/*
struct Node
{
	vector<Node*> NodeList;
	string NodeName;
	bool isSearched;
};
*/


class Node
{


public:
	//construtor
	Node();
	Node(string Title);


	//inspector

	string getName();
	vector<Node*> getList();
	Node * getNodeInList(string node);
	bool getChecked();
	void ShowAllList();

	//mutators
	void setName(string name);
	void addLink(Node * node);
	bool removeLink(string node);
	void setChecked(bool checked);


	//facilitator


private:
	vector<Node*> NodeList;
	string NodeName;
	bool isSearched;

};





#endif //NODE_H