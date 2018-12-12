#include<iostream>
using namespace std;

class Node
{
	int info;
	Node *prev,*link;	
};

Node *START=NULL;

Node* createNode()
{
	Node *temp;
	temp=new Node();
	temp->next=NULL;
	temp->prev=NULL;
	return(temp);
}

void insertNode(int data)
{
	Node *temp;
	temp=createNode();
	temp->info=data;
	if(START=NULL)
		START=temp;
	else
	{
		Node *t;
		t=START;
		while(t->next!=NULL)
		{
			t=t->link;
		}
		t->link=temp;
		temp->prev=t;
	}	
}

void insertAtBegn(int data)
{
	Node *temp;
	temp=createNode();
	temp->info=data;
	if(START==NULL)
		START=temp;
	else
	{
		temp->link=START;
		START=temp;
	}
}

void inserAtN(int data)
{
	Node *temp;
	temp=createNode();
	temp->info=data;
	cout<<"At which position you want yo enter the data=";
	cin>>n;
	if(n>size()+1)
		cout<<"OOPS!! no element is there at "<<n<<"th position"<<endl;
	else if(n==1)
	{
		temp->link=START;
		START=temp;
	}
	else
	{
		Node *t;
		t=START;
		for(i=0;i<n-2;i++)
		{
			t=t->link;
		}
		temp->link=t->link;
		temp->link->prev=temp;
		temp->prev=t;
		t->link=temp;
	}
}

void deleteAtN()
{
	int n;
	Node *t;
	t=START;
	cout<<"At which position you want to delete node=";
	cin>>n;
	for(int i=0;i<n-1;i++)
	{
		t=t->link;
	}
	t->prev->link=t->link;
	t->link->prev=t->prev;
	delete(t);
}
