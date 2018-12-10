#include<iostream>
using namespace std;

class QueueArray
{
	public: int front,rear;
	public: unsigned capacity;
	public: int *array;
};

QueueArray* createQueue(unsigned capacity)
{
	QueueArray *Q;
	Q=new QueueArray();
	Q->front=Q->rear=-1;
	Q->capacity=capacity;
	Q->array=new int[capacity];
	return(Q);
}

int queueIsEmpty(QueueArray *Q)
{
	return(Q->front==-1);
}

int queueIsFull(QueueArray *Q)
{
	return(Q->rear+1 % Q->capacity == Q->front);
}
void enQueue(QueueArray *Q,int data)
{
	if(queueIsFull(Q))
		cout<<"Overflow";
	else
	{
		Q->rear=Q->rear+1 % Q->capacity;
		Q->array[Q->rear]=data;
		if(queueIsEmpty(Q))
			Q->front=Q->rear;
	}
}

int deQueue(QueueArray *Q)
{
	int data;
	if(queueIsEmpty(Q))
		cout<<"Queue is empty"<<endl;
	else
	{
		data=Q->array[Q->front];
		if(Q->front == Q->rear)
			Q->front=Q->rear=-1;
		else
			Q->front=Q->front+1 % Q->capacity;
		return(data);
	}
}

void deleteQueue(QueueArray *Q)
{
	if(Q)
	{
		if(Q->array)
			delete(Q->array);
		delete(Q);
	}
}

int QueueSize(QueueArray* Q)
{
	return(Q->front > Q->rear  ?  Q->capacity - Q->front + Q->rear +1  :  1 + Q->rear - Q->front);
}

void displayQueue(QueueArray *Q)
{
	cout<<endl;
	if(queueIsEmpty(Q))
		cout<<"Queue is Empty!!"<<endl;
	else
	{
		if(Q->front > Q->rear)	
		{
			for(int i = Q->front ;i < Q->capacity ;i++)
			{
				cout<<Q->array[i]<<"-"<<" ";
			}
			for(int i=0 ;i < Q->rear+1 ;i++)
			{
				cout<<Q->array[i]<<"-"<<" ";
			}
		
		}
		else
		{
			for(int i=Q->front ; i < Q->rear+1 ;i++)
			{
				cout<<Q->array[i]<<"-"<<" ";
			}
		}
	}
	cout<<endl;
}

main()
{
	int n,k,data;
	unsigned l;
	QueueArray *Q;
	cout<<"Enter the capacity for overall queue=";
	cin>>l;
	Q=createQueue(l);
	cout<<endl;
	cout<<"How many elements you want to enter in Queue=";
	cin>>n;
	if(n>l)
		cout<<"OOps!!..data can't be accomaodated";
	else
	{
		for(int i=0;i<n;i++)
		{
			cout<<"Enter data "<<i+1<<"=";
			cin>>data;
			enQueue(Q,data);
		}
	}
	displayQueue(Q);
	cout<<endl;
	cout<<"How many elements you want to delete in Queue=";
	cin>>k;
	int arr[k];
	for(int i=0;i<k;i++)
	{
		arr[i]=deQueue(Q);
	}
	cout<<endl;
	cout<<"Deleted elements of queue are=";
	for(int i=0;i<k;i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	cout<<"Queue after deleteing elements=";
	displayQueue(Q);
	
}
