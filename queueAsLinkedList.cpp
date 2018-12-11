#include<iostream>
using namespace std;

class Node
{
	public: int info;
	public: Node *link;
};

Node *front=NULL,*rear=NULL;

Node* createNode()
{
	Node *t;
	t=new Node();
	t->link=NULL;
	return(t);
}

void enQueue(int data)
{
	Node *temp;
	temp=createNode();
	temp->info=data;
	if(front==NULL && rear==NULL)
	{
		front=rear=temp;
	}
	else
	{
		rear->link=temp;
		rear=rear->link;
	}
}

int deQueue()
{
	if(fron)
	int data;
	Node *t=front;
	front=front->link;
	data=t->info;
	return(data);
}

void dislayQueue()
{
	cout<<endl;
	Node *t;
	t=front;
	while(t!=NULL)
	{
		cout<<t->info<<"-";
		t=t->link;
	}
	cout<<endl;
}

main()
{
	int n,data,m;
	cout<<"How many elemets you want to enter in Queue=";
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cout<<"enter data "<<i+1<<"=";
		cin>>data;
		enQueue(data)
	}
	cout<<endl;
	cout<<"elements you entered in queue=";
	displayQueue();
	cout<<"How many elements you want to delete from queue=";
	cin>>m
	if(m>l)
	{
		cout<<"OOps!! wrong input"<<endl;
	}
	else
	{
		
	}
}
