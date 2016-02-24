#include "../Headers/Node.h"
#include <sstream>
#include <algorithm>
#include <iostream>

using namespace std;

Node::Node(){}


Node::Node(string Title)
{
	NodeName = Title;
}

string Node::getName()
{
	return NodeName;
}


vector<Node*> Node::getList()
{
	return NodeList;
}

Node * Node::getNodeInList(string node)
{
	transform(node.begin(), node.end(), node.begin(), ::tolower);
	for (int i = 0; i < NodeList.size(); i++)
	{
		string temp = NodeList[i]->NodeName;
		transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
		if (node == temp)
		{
			return NodeList[i];
		}
	}
	
}

bool Node::getChecked()
{
	return isSearched;
}


void Node::ShowAllList()
{
	for (int i = 0; i < NodeList.size(); i++)
	{
		cout << NodeList[i]->NodeName << endl;
	}
}

//mutators
void Node::setName(string name)
{
	NodeName = name;
}


void Node::addLink(Node * node)
{
	NodeList.push_back(node);
}


void Node::setChecked(bool checked)
{
	isSearched = checked;
}

bool Node::removeLink(string node)
{
	transform(node.begin(), node.end(), node.begin(), ::tolower);
	for (int i = 0; i < NodeList.size(); i++)
	{
		string temp = NodeList[i]->NodeName;
		transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
		if (node == temp)
		{
			NodeList.erase(NodeList.begin() + i);
			return true;
		}
	}
	return false;
}