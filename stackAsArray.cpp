#include<iostream>
using namespace std;

class StackArray
{
	public: int top;
	public: unsigned capacity;	
	public: int *array;
};

*StackArray createStack(int capacity)
{
	StackArray *S;
	S->top=-1;
	S->capacity=capacity;
	S->array=new int[capacity];
	return(S);
}

int stackIsFull(StackArray *S)
{
	return(top==capacity-1);
}

int stackisEmpty(StackArray *S)
{
	return(top==-1);
}

void Push(StackArray *S,int data)
{
	if(stackIsFull())
		cout<<"Stack is Full!!"<<endl;
	else
	{
		S->top++;
		S->array[top]=data;
	}
}

int Pop(StackArray *S)
{
	if(stackIsEmpty())
		cout<<"Stack is Empty!!"<<endl;
	else
	{
		int data=S->array[top];
		S->top--;
		return(data);
	}
}
