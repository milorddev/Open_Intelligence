#include "../Headers/Node.h"



Node::Node(string Title)
{
	NodeName = Title;
}

string Node::getName()
{
	return NodeName;
}