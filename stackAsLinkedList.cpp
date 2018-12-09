#include<iostream>
using namespace std;

class Node
{
	public: int info;
	public: Node *link;
};

Node *TOP=NULL;

Node* createNode()
{
	Node *temp;
	temp=new Node();
	temp->link=NULL;
	return(temp);
}

void push(int data)
{
	Node *temp;
	temp=createNode();
	temp->info=data;
	if(TOP==NULL)
		TOP=temp;
	else
	{
		temp->link=TOP;
		TOP=temp;
	}
}

int pop()
{
	Node *t;
	int del;
	t=TOP;
	TOP=TOP->link;
	del=t->info;
	delete(t);
	return(del);
}

void displayStack()
{
	cout<<endl;
	Node *t;
	t=TOP;
	while(t!=NULL)
	{
		cout<<"| "<<t->info<<" |"<<endl;
		t=t->link;
	}
}

main()
{
	int n,data;
	cout<<"How many elemeent you want to push onto stack=";
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cout<<"enter element "<<i+1<<"=";
		cin>>data;
		push(data);
	}
	displayStack();
	cout<<endl;
	cout<<"how many element you want to pop out of stack=";
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++)
	{
		arr[i]=pop();
	}
	cout<<endl;
	cout<<"Elements popped out of stack=";
	for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl<<endl;
	cout<<"Stack after popping out the elements----->";
	displayStack();
}
